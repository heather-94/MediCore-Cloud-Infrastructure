# MediCore Health Systems Incident Response Plan (IRP)
Prepared by: Heather Ramshaw
Date: 17/08/2026

## Purpose
This Incident Response Plan (IRP) defines the procedures MediCore Health Systems will follow when responding to cyber security incidents affecting cloud-hosted systems, patient data, and NHS-related services.
The plan follows the National Cyber Security Centre (NCSC) six-phase incident response lifecycle and applies to all AWS resources deployed within the MediCore cloud environment, including:
•	MediCore-Bastion-VM-01
•	MediCore-Web-VM-01
•	medicore-db (Amazon RDS PostgreSQL)
•	Amazon S3 Storage
•	Amazon CloudWatch Monitoring
The purpose of this plan is to minimise business disruption, preserve forensic evidence, protect Special Category health data, and ensure compliance with UK GDPR and NHS Data Security and Protection Toolkit (DSPT) requirements.

## Roles and Escalation Chain
Role	Person	Communication Method	Response SLA
Incident Lead	Heather Ramshaw	Microsoft Teams / Phone	Immediate
CTO	MediCore Chief Technology Officer	Microsoft Teams / Phone	Within 2 hours
Data Protection Officer (DPO)	MediCore DPO	Microsoft Teams / Phone	Within 2 hours
Database Administrator	MediCore DBA	Microsoft Teams / Phone	Within 30 minutes
AWS System Administrator	Cloud Operations Team	Microsoft Teams / Phone	Within 30 minutes
ICO Contact	Information Commissioner’s Office	ICO Reporting Portal	Within 72 hours
Email must not be used for urgent incident escalations. Teams messages and telephone communication are the primary communication methods.

##Monitoring Alerts
The following CloudWatch alerts provide the primary detection mechanism for security and operational incidents.
Alert Name	Purpose
High-CPU-WebVM	Detect abnormal web server CPU activity
High-NetworkIn-WebVM	Detect unusually high inbound traffic
High-NetworkOut-WebVM	Detect abnormal outbound traffic or possible data exfiltration
High-CPU-RDS	Detect abnormal database activity
Low-FreeStorage-RDS	Detect storage exhaustion affecting database availability


## NCSC Six-Phase Incident Response Lifecycle
## Phase 1 – Preparation
MediCore maintains the following preventative and detective security controls:
•	Security Groups configured using least privilege principles.
•	Bastion Host (MediCore-Bastion-VM-01) as the sole administrative entry point.
•	AES-256 encryption for Amazon S3 storage.
•	AWS KMS encryption for Amazon RDS.
•	HTTPS/TLS encryption for data in transit.
•	CloudWatch monitoring and alerting.
•	IAM least-privilege access roles.
•	Automated database backups and Point-in-Time Restore.
### Monitoring Alert SLA
Alert	Response SLA
High-CPU-WebVM	15 minutes
High-NetworkIn-WebVM	15 minutes
High-NetworkOut-WebVM	15 minutes
High-CPU-RDS	15 minutes
Low-FreeStorage-RDS	30 minutes


## Phase 2 – Identification
The identification phase begins when a CloudWatch alert enters an ALARM state.
### Alert Triggers
Alert	Potential Incident
High-CPU-WebVM	Denial of Service attack, malware, resource exhaustion
High-NetworkIn-WebVM	Port scanning, brute force attempt, external attack
High-NetworkOut-WebVM	Data exfiltration, malware communication
High-CPU-RDS	Unauthorised queries, database misuse
Low-FreeStorage-RDS	Database outage or service degradation risk

### GDPR Breach Reporting Clock
The UK GDPR 72-hour notification period begins when MediCore becomes aware that a personal data breach involving patient information has occurred. 
The Incident Lead must immediately notify:
•	CTO
•	DPO
for breach assessment and escalation.

## Phase 3 – Containment
### Critical Requirement
Before any containment activity begins:
ALL logs must be preserved.
The following evidence must be collected:
•	CloudWatch Logs
•	CloudWatch Metrics
•	EC2 System Logs
•	Operating System Logs
•	RDS Logs
•	Security Group Audit Information
•	IAM Access Logs
No servers may be rebuilt, restarted, patched, or modified until evidence has been captured.

### Containment Actions
Potential containment activities include:
•	Isolating compromised EC2 instances.
•	Restricting Security Group access.
•	Blocking malicious IP addresses.
•	Disabling compromised IAM accounts.
•	Restricting database access.
•	Removing affected systems from service behind the load balancer.

## Phase 4 – Eradication
### Web Server Compromise
If MediCore-Web-VM-01 is compromised:
1.	Terminate the affected instance.
2.	Deploy a new clean instance using the approved AMI.
3.	Apply the MediCore-Web-SG Security Group.
4.	Re-enable CloudWatch monitoring.
5.	Verify HTTPS functionality.
### Database Compromise
If medicore-db is compromised:
1.	Remove malicious access.
2.	Rotate credentials.
3.	Apply security patches.
4.	Validate encryption settings.
5.	Perform forensic review.

## Phase 5 – Recovery
### Web Tier Recovery
Recovery actions include:
•	Launching clean web server instances from the approved AMI.
•	Verifying CloudWatch monitoring status.
•	Restoring normal network connectivity,
•	Monitoring the environment for 24 hours.
### Database Recovery
Recovery of medicore-db includes:
1.	Restore from Amazon RDS Point-in-Time Restore.
2.	Validate database integrity.
3.	Verify patient record availability.
4.	Confirm application functionality.

### Verification
Recovery is complete when:
•	All services are operational.
•	CloudWatch alerts return to OK state.
•	User acceptance testing is successful.
•	No indicators of compromise remain.

## Phase 6 – Lessons Learned
Following incident resolution:
1.	Conduct an incident review meeting
2.	Identify root cause
3.	Assess impact to confidentiality, integrity and availability
4.	Update security controls where required
5.	Update staff awareness training
6.	Update the B3 Risk Register
7.	Record improvement actions and owners

## B3 Risk Register Updates
Potential updates may include:
•	New monitoring rules
•	Additional IAM restrictions
•	Enhanced Security Group controls
•	Additional backup or recovery testing
•	New staff awareness activities


## Alert-to-Response Mapping
Alert	IRP Phase Triggered	Notification	SLA
High-CPU-WebVM	Identification	Incident Lead	15 minutes
High-NetworkIn-WebVM	Identification	Incident Lead	15 minutes
High-NetworkOut-WebVM	Identification	Incident Lead	15 minutes
High-CPU-RDS	Identification	DBA and Incident Lead	15 minutes
Low-FreeStorage-RDS	Identification	DBA and Incident Lead	30 minutes


## Document Approval
Role	Status
Incident Lead	Approved
CTO	Pending
Data Protection Officer	Pending

