# Kingfisher Evaluation

Status: draft
Last reviewed: 2026-04-24
Confidence: low

## Official sources
- https://github.com/onevcat/Kingfisher
- https://swiftpackageindex.com/onevcat/Kingfisher

## Default recommendation
Do not add Kingfisher unless remote image loading, caching, placeholder handling, and image pipeline concerns are real enough that rolling your own would be worse.

## Use when
- image-heavy product surfaces exist
- caching and async image handling are repeated concerns
- downsampling, placeholder handling, prefetching, or cache control are now real product needs
- the built-in path is becoming verbose or inconsistent

## Avoid when
- image usage is light and straightforward
- product scale does not justify a separate image dependency

## Official repository signal
The official README emphasizes hybrid memory/disk cache, processors, prefetching, placeholder/indicator handling, SwiftUI support, and image-pipeline options. That makes it a stronger candidate when image handling is a product surface, not just a utility concern.

## Related skills
- ios-feature-bootstrap
- ios-library-selection
