[🏠 Home](../slide-deck.md) | [⬆️ Up](../slide-deck.md) | [⬅️ Prev](slide-08-simple-example.md) | [➡️ Next](slide-10-conclusion.md)

---

# Slide 9: Small, Complete Example (Complex)

## Full-Stack Web Application

### Project Scope
**Enterprise-grade application with modern architecture**

### Architecture Overview

```mermaid
graph TB
    subgraph "Client Layer"
        A[React/Vue Frontend]
        B[Mobile App<br/>Optional]
    end
    
    subgraph "API Gateway"
        C[NGINX<br/>Load Balancer]
    end
    
    subgraph "Service Layer"
        D[.NET Core API<br/>Auth Service]
        E[Node.js API<br/>Business Logic]
    end
    
    subgraph "Data Layer"
        F[(PostgreSQL<br/>Primary DB)]
        G[(Redis<br/>Cache)]
    end
    
    subgraph "Infrastructure"
        H[Docker<br/>Containers]
        I[GitHub Actions<br/>CI/CD]
    end
    
    A --> C
    B --> C
    C --> D
    C --> E
    D --> F
    D --> G
    E --> F
    E --> G
    D --> H
    E --> H
    H --> I
    
    style A fill:#E6FFE6
    style B fill:#E6FFE6
    style C fill:#FFE4B5
    style D fill:#E6E6FF
    style E fill:#E6E6FF
    style F fill:#FFE6E6
    style G fill:#FFE6E6
```

### Features Delivered
- **Authentication**: JWT tokens, OAuth2
- **User Management**: Registration, profiles, roles
- **API**: RESTful, OpenAPI documented
- **Database**: Migrations, seed data
- **Testing**: 80% code coverage
- **CI/CD**: GitHub Actions pipeline
- **Monitoring**: Logging, health checks

### Development Metrics
- **Timeline**: 2 weeks (vs 2-3 months traditional)
- **Code Quality**: A-rated on all metrics
- **Cost**: $3,000 (vs $50,000+ traditional)

---

[🏠 Home](../slide-deck.md) | [⬆️ Up](../slide-deck.md) | [⬅️ Prev](slide-08-simple-example.md) | [➡️ Next](slide-10-conclusion.md)