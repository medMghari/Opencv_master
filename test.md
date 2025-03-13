```mermaid
graph LR
    A[Start: Binary Image Input] --> B{Choose K};
    B --> C{Calculate Distance to Training Images};
    C --> D{Find K Nearest Neighbors};
    D --> E{Count Neighbors' Labels (0 or 1)};
    E --> F{Majority Vote: Predict Class};
    F --> G[Output: Predicted Class (0 or 1)];
    G --> H[End];

    subgraph Training Phase
        I[Training Images & Labels]
    end

    I --> C;

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#ccf,stroke:#333,stroke-width:2px
    style F fill:#9f9,stroke:#333,stroke-width:2px
    style G fill:#9f9,stroke:#333,stroke-width:2px
    style H fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#eee,stroke:#333,stroke-width:2px
