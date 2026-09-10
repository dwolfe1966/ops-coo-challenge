# Risk Decision Tree

```mermaid
flowchart TD
    A[Automation output] --> B{Source/entity state valid?\nFresh? Not duplicate?}
    B -- No --> Y[Operator review / YELLOW]
    B -- Yes --> C{Legal, contract, sensitive data,\nor high-value customer exposure?}
    C -- Yes --> R[Senior / executive review / RED]
    C -- No --> D{External action?}
    D -- No --> E{Reversible + low downside +\nconfidence above threshold?}
    E -- Yes --> G[Auto-execute / GREEN]
    E -- No --> Y
    D -- Yes --> F{Reversible + low downside +\nvalidated identity/context +\nproven reliability?}
    F -- Yes --> G
    F -- No --> Y
    G --> H[Log action + completion evidence + outcome]
    Y --> I[Operator approve / edit / reject]
    R --> J[Evidence packet + recommended decision]
    H --> K[Measure outcome + monitor exceptions]
    I --> K
    J --> K
    K --> L{Failure or drift?}
    L -- No --> A
    L -- Yes --> M[Contain → recover → diagnose → patch → replay]
    M --> A
```

## Principle
Automation earns autonomy through measured reliability and bounded downside. The policy should reduce review as evidence improves, while immediately tightening controls after a material failure.
