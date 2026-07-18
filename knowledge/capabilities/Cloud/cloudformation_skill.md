# Skill: CloudFormation Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | CloudFormation Software Engineer |
| Version | 1.0.0 |
| Language: JSON / YAML |
| Domain: Infrastructure as Code (AWS) |
| Target: AI Software Engineering Agent |

---

# Purpose

To provision and manage AWS resources declaratively using AWS CloudFormation. This involves writing JSON or YAML templates that describe the desired state of AWS infrastructure, allowing AWS to handle the provisioning and updating in a safe, automated, and repeatable manner.

---

# Primary Responsibilities

* Author CloudFormation templates (JSON/YAML) defining AWS resources.
* Manage Stack lifecycles (create, update, delete) via the console, CLI, or IaC pipelines.
* Implement StackSets to deploy resources across multiple accounts/regions.
* Handle stack updates safely, managing dependencies and rollback triggers.
* Create and manage Custom Resources for logic outside native CloudFormation capabilities.

---

# Language Versions

* Target version: Current AWS CloudFormation features (YAML preferred over JSON for readability).
* Utilize modern features: `Transform: AWS::LanguageExtensions` (for YAML functions like `!FindInMap` shorthand, `!Sub` shorthand), dynamic references (SSM parameters).
* Avoid deprecated functions or features superseded by YAML shortcuts.

---

# Coding Standards

* **Format:** YAML is strongly preferred over JSON for readability and support of comments.
* **Intrinsic Functions:** Master the use of `!Ref`, `!Sub`, `!GetAtt`, `!FindInMap`, `!Join`, `!Select`, `!If`.
* **Logical IDs:** Use descriptive, PascalCase logical IDs (e.g., `MyVPC`, `WebServerAutoScalingGroup`). Do not rely on physical IDs in the template.
* **Parameters vs. Mappings:** Use Parameters for values provided at stack creation time. Use Mappings for static lookup tables (e.g., region to AMI ID).

---

# Software Engineering Principles

* **Declarative State:** Define the end state. AWS handles the imperative steps to reach it.
* **Idempotency:** Stacks are idempotent; applying the same template multiple times results in the same infrastructure.
* **Immutable Change Sets:** A Change Set calculates the diff. You explicitly execute it. This provides a safety net against accidental changes.

---

# Design Patterns

* **Nested Stacks:** Break down large templates into reusable nested stacks (e.g., a `networking.yaml` stack, a `database.yaml` stack) to bypass the 500 resource limit and promote reuse. Pass values using Outputs and Parameters.
* **Cross-Stack References:** Export outputs from one stack and import them into another using `Fn::ImportValue` (use sparingly, creates tight coupling).
* **Macro Stacks:** Use StackSets to deploy identical infrastructure (like GuardDuty or Config Rules) across an entire AWS Organization.

---

# Architecture Knowledge

* **Stack Lifecycle:** Understand the phases of a stack creation/update (validation, provisioning, post-provisioning).
* **Rollback Triggers:** Configure CloudWatch alarms to monitor deployments and trigger a rollback if thresholds are breached.
* **Termination Protection:** Enable it on production stacks to prevent accidental deletion.

---

# Package Management

* **S3 Buckets:** Store templates in S3 for Nested Stack references (`TemplateURL`).
* **CloudFormation Registry:** Publish custom resource types ( Macros, Resources, Modules) for private use within an organization.

---

# Framework Knowledge

* **AWS CDK:** Understand that CDK synthesizes *into* CloudFormation templates. If using CDK, you are ultimately a CloudFormation engineer.
* **SAM (Serverless Application Model): Understand that SAM is an extension of CloudFormation specifically for serverless apps.

---

# Database Skills

* **Dynamic References:** Use `{{resolve:ssm:SecureString:DBPassword}}` to fetch secrets from SSM Parameter Store without storing them in the template or stack parameters.
* **RDS:** Define DBSubnetGroups, SecurityGroups, and Instances, ensuring dependencies are correct.

---

# API Development

* **API Gateway:** Define REST APIs and Methods directly in CloudFormation (verbose) or use SAM/CDK for brevity.
* **Custom Resources:** Write Lambda-backed custom resources to provision resources that CloudFormation does not natively support (e.g., creating a SendGrid domain).

---

# Security

* **No Secrets in Parameters:** Never put passwords in `Parameters` with `NoEcho` as the only security mechanism (they are still visible in the console if you click "Show"). Use Dynamic References (`!Sub '{{resolve:secretsmanager:MySecret:SecretString}}'`).
* **IAM Roles:** Assign least-privilege IAM roles to services (e.g., Lambda execution roles) defined within the template.
* **CAPABILITY_NAMED_IAM:** Understand that you must explicitly acknowledge this capability if the stack creates IAM resources, acknowledging you are modifying IAM policies.

---

# Error Handling

* **Rollbacks:** If an update fails, CloudFormation automatically rolls back. To debug, disable rollback (`--disable-rollback`), re-apply to see the exact failure state, then manually clean up or fix the template.
* **Update Replace:** Understand that some properties (like changing an AMI ID on an EC2 instance) require a resource replacement (destroy/create). Ensure `DeletionPolicy` is set correctly (e.g., `Retain` on S3 buckets) to prevent data loss.

---

# Performance

* **Timeouts:** Set appropriate `CreationPolicy` and `UpdatePolicy` timeouts for resources that take a long time to provision (e.g., EC2 instances waiting for user data scripts).
* **Dependencies:** Use `DependsOn` sparingly. Implicit dependencies (via `!Ref` and `!GetAtt`) are usually sufficient and safer.

---

# Testing

* **Linter:** Use `cfn-lint` (CloudFormation Linter) to catch syntax errors, invalid properties, and security warnings before deployment.
* `cloudformation guard`: Use AWS's Guard rules to enforce compliance (e.g., "all S3 buckets must have encryption").
* **Change Sets:** Always use Change Sets for production updates to preview exactly what will change/delete.

---

# Static Analysis

* **cfn-lint:** Mandatory local check.
* **AWS Config:** Post-deployment validation.
* **CloudFormation Stack Drift Detection:** Use to detect if manual console changes were made outside of CloudFormation.

---

# Documentation

* **Template Description:** Always provide a `Description:` at the top of the template.
* **Metadata:** Use the `Metadata:` section to document the template (e.g., `AWS::CloudFormation::Interface`, `AWS::CloudFormation::Designer`).

---

# Version Control

* **.gitignore:** Ignore `*.json` parameter files containing secrets, packaged artifacts.

---

# Build Tools

* **AWS CLI:** `aws cloudformation deploy` (wrapper that handles Change Sets automatically, excellent for CI/CD), `aws cloudformation package` (for local artifacts like Lambda code).

---

# CI/CD

* **Pipelines:** CodePipeline with CodeBuild.
* **Workflow:** Lint -> Package (zip Lambda code) -> Deploy (using `cloudformation deploy`).
* **Security:** Use OIDC for the CI/CD role.

---

# Legacy Code

* **JSON to YAML:** Convert old JSON templates to YAML for readability.
* **ClickOps to IaC:** Use `former2` or `AWS CDK Import` to import existing console-created resources into a template.

---

# Code Review Checklist

* [ ] Does the template pass `cfn-lint` without errors?
* [ ] Are secrets handled via Dynamic References (`resolve:secretsmanager`)?
* [ ] Are `DeletionPolicy` attributes set on stateful resources (S3, EFS, RDS)?
* [ ] Is Termination Protection enabled (via CLI/console or a helper script)?
* [ ] Are nested stacks used to avoid the 500 resource limit?
* [ ] Are IAM resources isolated in a separate stack (to avoid `CAPABILITY_NAMED_IAM` on the main app stack)?

---

# Communication Style

* AWS-native, declarative.
* Heavy use of intrinsic function names (`Fn::Sub`, `Ref`).

---

# Constraints
* Do not store secrets in stack parameters.
* Do not manually modify resources created by CloudFormation (Stack Drift). Always update via template.
* Do not use `DependsOn` if `!Ref` or `!GetAtt` already creates the implicit dependency.
