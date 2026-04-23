# iOS Project Skeleton

```text
MyApp/
├─ App/
│  ├─ MyAppApp.swift
│  ├─ AppBootstrap.swift
│  ├─ AppEnvironment.swift
│  ├─ AppRouter.swift
│  └─ AppSession.swift
├─ Core/
│  ├─ Networking/
│  ├─ Storage/
│  ├─ Logging/
│  ├─ Analytics/
│  ├─ DesignSystem/
│  └─ Configuration/
├─ Features/
│  ├─ Auth/
│  │  ├─ Presentation/
│  │  ├─ Domain/
│  │  └─ Data/
│  ├─ Home/
│  └─ Settings/
├─ Shared/
├─ Resources/
├─ Config/
└─ Tests/
```

## Notes
- Start simple; do not turn every folder into a module.
- Keep `Shared/` small and intentional.
- Keep feature code close to feature ownership.
