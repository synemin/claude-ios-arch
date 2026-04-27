# Network Service Template — URLSession

```swift
import Foundation

// MARK: - Protocol

protocol NetworkService: Sendable {
    func request<T: Decodable>(
        endpoint: Endpoint,
        responseType: T.Type
    ) async throws -> T
}

// MARK: - Endpoint

struct Endpoint: Sendable {
    let path: String
    let method: HTTPMethod
    let queryItems: [URLQueryItem]
    let body: Encodable?
    let headers: [String: String]

    init(
        path: String,
        method: HTTPMethod = .get,
        queryItems: [URLQueryItem] = [],
        body: Encodable? = nil,
        headers: [String: String] = [:]
    ) {
        self.path = path
        self.method = method
        self.queryItems = queryItems
        self.body = body
        self.headers = headers
    }
}

enum HTTPMethod: String, Sendable {
    case get = "GET"
    case post = "POST"
    case put = "PUT"
    case patch = "PATCH"
    case delete = "DELETE"
}

// MARK: - Implementation

final class URLSessionNetworkService: NetworkService {

    private let session: URLSession
    private let baseURL: URL
    private let decoder: JSONDecoder
    private let encoder: JSONEncoder

    init(
        baseURL: URL,
        session: URLSession = .shared,
        decoder: JSONDecoder = .init(),
        encoder: JSONEncoder = .init()
    ) {
        self.baseURL = baseURL
        self.session = session
        self.decoder = decoder
        self.encoder = encoder

        // TODO: configure decoder/encoder defaults
        // decoder.dateDecodingStrategy = .iso8601
        // decoder.keyDecodingStrategy = .convertFromSnakeCase
        // encoder.keyEncodingStrategy = .convertToSnakeCase
    }

    func request<T: Decodable>(
        endpoint: Endpoint,
        responseType: T.Type
    ) async throws -> T {
        let request = try buildRequest(for: endpoint)

        let (data, response) = try await session.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse else {
            throw NetworkError.invalidResponse
        }

        guard (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.httpError(
                statusCode: httpResponse.statusCode,
                data: data
            )
        }

        do {
            return try decoder.decode(T.self, from: data)
        } catch {
            throw NetworkError.decodingFailed(error)
        }
    }

    private func buildRequest(for endpoint: Endpoint) throws -> URLRequest {
        var components = URLComponents(
            url: baseURL.appendingPathComponent(endpoint.path),
            resolvingAgainstBaseURL: true
        )!
        if !endpoint.queryItems.isEmpty {
            components.queryItems = endpoint.queryItems
        }

        guard let url = components.url else {
            throw NetworkError.invalidURL(endpoint.path)
        }

        var request = URLRequest(url: url)
        request.httpMethod = endpoint.method.rawValue
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        for (key, value) in endpoint.headers {
            request.setValue(value, forHTTPHeaderField: key)
        }

        if let body = endpoint.body {
            request.httpBody = try encoder.encode(AnyEncodable(body))
        }

        return request
    }
}

// MARK: - Errors

enum NetworkError: LocalizedError {
    case invalidURL(String)
    case invalidResponse
    case httpError(statusCode: Int, data: Data)
    case decodingFailed(Error)

    var errorDescription: String? {
        switch self {
        case .invalidURL(let path):
            "Invalid URL for path: \(path)"
        case .invalidResponse:
            "Invalid server response"
        case .httpError(let code, _):
            "HTTP error \(code)"
        case .decodingFailed(let error):
            "Failed to decode response: \(error.localizedDescription)"
        }
    }
}

// MARK: - Type Erasure Helper

private struct AnyEncodable: Encodable {
    private let encode: (Encoder) throws -> Void

    init(_ value: Encodable) {
        self.encode = value.encode(to:)
    }

    func encode(to encoder: Encoder) throws {
        try encode(encoder)
    }
}
```

## Usage Notes
- Replace `baseURL` with your API base URL.
- Configure decoder strategies (snake_case, dates) in the init.
- Add auth token injection via a request interceptor or by extending `buildRequest`.
- For multipart uploads, add a separate method — don't overload `request()`.
- This is intentionally simple. Add retry/caching/logging as separate concerns when needed.
