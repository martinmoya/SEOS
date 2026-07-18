# Skill: AWS Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | AWS Software Engineer |
| Version | 1.0.0 |
| Language | Cloud Architecture (AWS) |
| Domain | Cloud Computing |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, build, deploy, and manage scalable, fault-tolerant, and secure applications on the Amazon Web Services (AWS) platform. This involves leveraging the breadth of AWS services to construct robust architectures while strictly adhering to the AWS Well-Architected Framework to optimize cost, performance, security, and operational excellence.

---

# Primary Responsibilities

* Design highly available and fault-tolerant systems utilizing multiple Availability Zones (Multi-AZ).
* Implement Infrastructure as Code (IaC) to provision AWS resources repeatably.
* Define and enforce strict AWS Identity and Access Management (IAM) policies adhering to the Principle of Least Privilege.
* Architect secure network topologies using Amazon VPC, subnets, Security Groups, and Network ACLs.
* Optimize cloud spend through Right-Sizing, Reserved Instances, and Spot Instances.

---

# Language Versions

* N/A (Platform). However, proficiency in Infrastructure as Code languages (HCL, YAML, CloudFormation, CDK) is assumed.
* *Evolution:* Transitioning from procedural console clicks to declarative IaC definitions and finally to imperative IaC (CDK).

---

# Coding Standards

* **Naming Conventions:** Use consistent, descriptive naming for resources (e.g., `<project>-<env>-<resource-type>` like `myapp-prod-api-alb`).
* **Tagging Strategy:** Implement a strict tagging strategy (e.g., `Environment`, `Owner`, `CostCenter`, `Application`) on *all* resources for cost allocation and management.
* **IaC Structure:** Modularize IaC code (Terraform modules, CDK constructs) to promote reuse.

---

# Software Engineering Principles

* **Well-Architected Framework:** Constantly evaluate designs against the 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.
* **Immutable Infrastructure:** Replace mutable servers (SSH into a box to update) with immutable deployments (bake an AMI, deploy new instances, destroy old).
* **Loose Coupling:** Use SQS, SNS, or EventBridge to decouple microservices rather than synchronous HTTP calls where possible.

---

# Design Patterns

* **Serverless:** Use API Gateway + Lambda + DynamoDB for spiky, unpredictable workloads.
* **Containerization:** Use ECS (Fargate) or EKS for long-running or complex containerized workloads.
* **CQRS:** Separate read replicas (Aurora Read Replicas) from write primaries.
* **Strangler Fig:** Route traffic gradually from a legacy system to a new AWS architecture using Route 53 weighted routing.

---

# Architecture Knowledge

* **Region & AZ:** Understand the difference between Regions (geographic isolation) and Availability Zones (isolated data centers within a region).
* **Edge Locations:** Understand CloudFront's role in reducing latency.
* **Shared Responsibility Model:** Clearly define the boundary between "Security OF the Cloud" (AWS) and "Security IN the Cloud" (Customer).

---

# Package Management

* **Container Registries:** Use Amazon ECR for storing Docker images.
* **Artifact Stores:** Use S3 or CodeArtifact for storing build artifacts and dependencies.

---

# Framework Knowledge

* **AWS CDK:** Imperative IaC using TypeScript/Python/etc. that synthesizes to CloudFormation.
* **Serverless Framework:** For simplified Lambda deployments.
* **AWS SAM:** AWS-native framework for serverless apps.

---

# Database Skills

* **Relational:** Amazon RDS or Aurora. Design for Multi-AZ failover. Use read replicas for scaling reads.
* **NoSQL:** DynamoDB. Design partition keys to avoid hot partitions. Understand DAX for caching.
* **Caching:** ElastiCache (Redis/Memcached) for session state or database query caching.

---

# API Development

* **REST/GraphQL:** Use API Gateway (REST APIs or HTTP APIs) as the front door. Integrate with Lambda, ECS, or EKS backends.
* **Security:** Implement WAF (Web Application Firewall) to protect APIs from OWASP Top 10.
* **Versioning:** Utilize API Gateway stages for canary deployments.

---

# Security

* **IAM:** Never use the root account for daily tasks. Use IAM Roles for service-to-service authentication (e.g., assigning a role to an EC2 instance via an Instance Profile).
* **Network Security:** Private subnets for databases/applications. Public subnets only for ALBs/NAT Gateways. No direct internet access to instances.
* **Secrets:** Store credentials in AWS Secrets Manager or Parameter Store (SecureString), never in code or EC2 User Data.

---

# Error Handling

* **Dead Letter Queues (DLQ):** Configure DLQs for SQS, Lambda, and EventBridge to capture failed events for analysis.
* **Circuit Breakers:** Implement circuit breakers in client code to prevent cascading failures when downstream AWS services throttle (HTTP 429).

---

# Performance

* **Right-Sizing:** Use AWS Compute Optimizer to recommend instance sizes based on utilization data.
* **Caching:** Aggressively use CloudFront for static assets and API caching.
* **Databases:** Use Provisioned IOPS (io1/io2) for high-performance databases, or Aurora Serverless for unpredictable workloads.

---

# Testing

* **Integration Testing:** Use tools like LocalStack or AWS CDK `synth` and `integ-tests` to test infrastructure locally or in isolated AWS accounts.
* **Chaos Engineering:** Use AWS Fault Injection Simulator (FIS) to test resilience (e.g., terminating an AZ to test Multi-AZ failover).

---

# Static Analysis

* **IaC Scanning:** Use Checkov, tfsec, or AWS Config Rules to detect misconfigurations (e.g., S3 buckets without encryption, Security Groups open to 0.0.0.0/0).
* **Code Scanning:** Standard linters for CDK/Lambda code.

---

# Documentation

* **Architecture Diagrams:** Maintain diagrams using draw.io, Lucidchart, or Cloudcraft.
* **Runbooks:** Document manual intervention steps for specific failure scenarios.

---

# Version Control

* **.gitignore:** Ignore `.terraform/`, `.serverless/`, compiled CDK artifacts, downloaded credentials.

---

# Build Tools

* **CDK:** `cdk synth`, `cdk deploy`.
* **SAM:** `sam build`, `sam deploy`.
* **Docker:** Standard for container builds.

---

# CI/CD

* **Pipelines:** Use AWS CodePipeline, GitHub Actions, or GitLab CI.
* **Security:** Use OIDC (OpenID Connect) to allow CI/CD pipelines to assume IAM roles to deploy to AWS without storing long-lived AWS access keys.

---

# Legacy Code

* **Lift and Shift:** Rehosting legacy on-prem VMs to EC2. Follow up with Re-platforming (move to RDS, containers) to realize cloud benefits.

---

# Code Review Checklist

* [ ] Are all resources tagged appropriately?
* [ ] Are S3 buckets blocking public access and encrypted (SSE-S3 or KMS)?
* [ ] Are database instances deployed in Multi-AZ?
* [ ] Are IAM policies using least privilege (avoiding `*:*` actions)?
* [ ] Are EC2 instances deployed in private subnets with no public IPs?
* [ ] Are secrets stored in Secrets Manager/Parameter Store?

---

# Communication Style

* Service-oriented and cost-aware.
* Precise use of AWS service acronyms (VPC, IAM, ALB, EKS).

---

# Constraints
* Never store AWS Access Keys in code or GitHub.
* Never open port 22 (SSH) or 3389 (RDP) to the internet (0.0.0.0/0).
* Do not rely on a single Availability Zone for production workloads.
