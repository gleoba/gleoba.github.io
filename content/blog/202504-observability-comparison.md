---
title: 'Beyond Observability: Exploring the Future of Long-Term Metric Storage'
date: 2025-04-04T14:38:33+02:00
draft: false
type: 'blog'
tags: 
  - observability
  - Thanos
  - Cortex
  - Prometheus
  - VictoriaMetrics

---

![banner](/images/blog/compare-tools-header.png "What is your choise?")

## TL;DR
This article compares three popular CNCF observability platforms (**Thanos**, **Cortex**, and **VictoriaMetrics**) for building an "observability lake" - a system that not only handles real-time metrics but also extracts long-term value from metrics data through analytics and machine learning. Each platform has different approaches to long-term storage, analytics integration, and data lake use cases, with their own strengths and weaknesses.

## Introduction

In today's rapidly evolving tech ecosystem, observability has become essential for understanding system health, performance, and reliability. But what happens when your metrics data needs to outlive traditional observability use cases? What if you need to leverage historical observability metrics for analytics, machine learning training, or integrate this data into your broader data ecosystem such as data lakes or a data mesh?

In this blog, we'll compare the leading long-term storage solutions for observability metrics: `Thanos`[^1], `Cortex`[^2], and `VictoriaMetrics`[^3]. We'll examine their suitability for extended use cases, specifically how each integrates with broader data ecosystems and analytics workflows.

### A Quick Look at the Tools

- **Thanos** extends Prometheus by storing metrics in immutable TSDB blocks in object storage (S3, GCS, Azure), offering cost-effective long-term retention.
- **Cortex** (and its successor Grafana Mimir) offers multi-tenant capabilities and can store metrics either as compressed chunks or blocks similar to Thanos.
- **VictoriaMetrics** features a custom LSM-tree storage optimized for high-performance queries but traditionally stores data locally rather than directly integrating with object storage.

### Extending Metrics Beyond Observability

#### Storage Formats and Data Lake Integration

A common challenge for platform teams is integrating observability data into data lakes for analytics or machine learning purposes. Let's look at how each tool fares:

- **Thanos** and **Cortex** (block storage) store data in Prometheus TSDB blocks. While efficient for time-series querying, these blocks aren't directly readable by analytical tools like Spark or Athena without conversion. Converting these blocks into analytics-friendly formats like Parquet or Arrow currently requires external tools or custom scripting.

- **VictoriaMetrics**, on the other hand, stores metrics in a proprietary, highly optimized format. While excellent for real-time queries, VictoriaMetrics doesn't directly integrate with data lakes. However, it provides built-in APIs to export data into CSV or JSON, and there are plans to add Parquet export capability, making future integrations smoother.

### ML and Historical Data Analysis

As companies increasingly turn to machine learning for operational insights, historical observability data becomes a valuable asset.

- **Thanos and Cortex** provide PromQL and remote-read APIs, allowing data extraction for ML jobs. However, large-scale exports can be challenging due to the overhead of JSON or protobuf responses.
- **VictoriaMetrics** excels here with its dedicated `/export` API, providing CSV or JSON Lines, simplifying data extraction significantly for ML pipelines. Its efficient storage format also helps speed up large-scale historical queries.

### Building Bridges to Analytics

The industry trend is clear: observability metrics need integration into broader analytics ecosystems. Tools like `Trino Prometheus connector`[^4] and experimental Apache Spark connectors show promise, allowing metrics data to be queried alongside traditional business data, albeit still relying on external conversion from TSDB formats.

### Where are the tools being used?

As the technology evolves, vendors may switch their selection; however, for large setups, such a switch scenario could be considered a rare event. The below report is definitely not exhaustive and mentions only a few vendors worth noting.

- **Thanos** Cloudflare, Reddit, RedHat (OpenShift), eBay, Nubank, Disney, Adobe, Logz - source[^5]
- **Cortex** AWS, Grafana Labs, Weaveworks, Electronic Arts (EA), REWE - source[^6], source[^7]
- **VictoriaMetrics** Grammarly, Wix, Adidas, Brandwatch, CERN, Criteo and Roblox - source[^8], source[^9]

### Which tool fits your ecosystem?

Your choice might depend on existing infrastructure and use-cases:

- **Thanos** suits environments already leveraging cloud object storage and seeking scalable, cost-effective metric retention.
- **Cortex** is ideal if you require multi-tenancy and the scalability offered by its distributed architecture.
- **VictoriaMetrics** is your go-to if you need high-performance real-time queries and straightforward API-driven integration with external analytics systems.

However, regardless of your choice, integration into data lakes for advanced analytics currently involves additional steps - typically external ETL pipelines or conversion tools like `prometheus-tsdb-parquet`[^10].

For more detail comparison and selection criterias, go the [next blog post on the subject](202504-observability-comparison-table/).

### Looking Forward

The gap between observability platforms and broader analytics ecosystems is shrinking. Future developments like native Arrow/Parquet export, deeper integration with SQL engines, and community-driven tooling will further simplify leveraging long-term metrics for more than traditional observability.

What tools are you using in your projects? Are you facing challenges in integrating observability data into your analytics pipelines or ML workflows? *Let’s discuss in the comments!*

## References

- Thanos design docs on storage format and object store usage ([Thanos - Highly available Prometheus setup with long term storage capabilities](https://thanos.io/tip/thanos/storage.md/#:~:text=Thanos%20supports%20writing%20and%20reading,storage%20using%20range%20GET%20API))
- Cortex documentation and AWS blog on chunks vs. blocks storage ([How AWS and Grafana Labs are scaling Cortex for the cloud | AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/how-aws-and-grafana-labs-are-scaling-cortex-for-the-cloud/#:~:text=The%20chunks%20storage%20engine%2C%20which,TSDB%20storage%2C%20the%20same%20blocks))
- Cortex API/compatibility (PromQL, remote read) described in AWS OSS post ([How AWS and Grafana Labs are scaling Cortex for the cloud | AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/how-aws-and-grafana-labs-are-scaling-cortex-for-the-cloud/#:~:text=offer%20their%20own%20Grafana%20Cloud,healthy%20community%20with%20numerous%20contributors)) and official docs.  


[^1]: https://github.com/thanos-io/thanos "Thanos on GitHub"
[^2]: https://github.com/cortexproject/cortex "Cortex on GitHub"
[^3]: https://github.com/VictoriaMetrics/VictoriaMetrics "VictoriaMetrics on GitHub"
[^4]: https://trino.io/docs/current/connector/prometheus.html "Trino prometheus connector"
[^5]: https://github.com/thanos-io/thanos/blob/main/website/data/adopters.yml
[^6]: https://www.cncf.io/blog/2018/12/18/cortex-a-multi-tenant-horizontally-scalable-prometheus-as-a-service "Cortex in CNCF Blog"  
[^7]: https://www.infracloud.io/blogs/cortex-for-ha-monitoring-with-prometheus "infracloud blogs about cortex"
[^8]: https://www.enterprisetimes.co.uk/2023/11/06/open-source-vendor-victoriametrics-delivers-stunning-growth/
[^9]: https://victoriametrics.com/products/open-source/
[^10]: https://github.com/moshe/prometheus-tsdb-parquet "prometheus-tsdb-parquet tool"