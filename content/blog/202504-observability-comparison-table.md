---
title: 'Beyond Observability (Part II)'
date: 2025-04-04T14:50:00+02:00
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

## Introduction

This is a second part on the subject, continuing the original blog post [ Beyond Observability: Exploring the Future of Long-Term Metric Storage](202504-observability-comparison-table/).

After the overview in the original blog post, now we'll list the comparison and selection criterias for the leading long-term storage solutions for observability metrics: `Thanos`[^1], `Cortex`[^2], and `VictoriaMetrics`[^3]. 


## Observability Platform Comparison Table

| Feature | **Thanos** | **Cortex** | **VictoriaMetrics** |
|---------|------------|------------|---------------------|
| **Architecture** | Layer on top of Prometheus | Horizontally scalable microservices | Independent TSDB (single binary) |
| **Storage Approach** | Prometheus TSDB blocks in object storage (S3, GCS, Azure, etc.) | Originally chunk store; now also Prometheus TSDB blocks in object storage | Custom LSM-tree + columnar format on local/network disks |
| **Prometheus Compatibility** | 100% compatible (augments Prometheus) | 100% compatible (exposes same APIs) | Compatible with Prometheus remote write |
| **Long-term Storage** | Offloads blocks to object storage for unlimited retention | Stores data in object stores for long-term retention | Stores on disk; snapshots can be copied to object storage |
| **Query Capabilities** | Single PromQL endpoint for recent and archived data | PromQL query APIs | PromQL support; optimized export API |
| **Downsampling** | Automatic downsampling for older data | No automatic downsampling in open-source version | Enterprise version supports downsampling |
| **Data Lake Integration** | Requires external ETL; community tools like Obslytics for Parquet export | Similar to Thanos; requires ETL for data lake formats | Built-in export API makes extraction easier |
| **Multi-tenancy** | Basic | Strong multi-tenant design | Available in cluster version |
| **Operational Complexity** | Moderate | High (many components) | Low (simple deployment) |
| **Resource Efficiency** | Moderate | Moderate | High |

##  When to Choose Each Platform

### Choose **Thanos** when:
- You already use Prometheus and want a plug-in solution
- You need cloud-friendly archiving with minimal operational changes
- Automatic downsampling for historical data is important
- You want to leverage cheap object storage for unlimited retention

### Choose **Cortex** when:
- Multi-tenancy is a primary requirement
- You need horizontally scalable, "Prometheus-as-a-Service"
- Your organization has multiple teams/tenants with isolated data needs
- You're handling massive workloads requiring scale-out architecture
- You need robust logical separation of metrics by team

### Choose **VictoriaMetrics** when:
- Operational simplicity and easy deployment are priorities
- Resource efficiency and raw performance are critical
- You need straightforward data export capabilities for analytics
- You don't immediately need object storage integration
- Single-binary operation with minimal overhead is appealing


[^1]: https://github.com/thanos-io/thanos "Thanos on GitHub"
[^2]: https://github.com/cortexproject/cortex "Cortex on GitHub"
[^3]: https://github.com/VictoriaMetrics/VictoriaMetrics "VictoriaMetrics on GitHub"
[^4]: https://trino.io/docs/current/connector/prometheus.html "Trino prometheus connector"
[^5]: https://github.com/moshe/prometheus-tsdb-parquet "prometheus-tsdb-parquet tool"