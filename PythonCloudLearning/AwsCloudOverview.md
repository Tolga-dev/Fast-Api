# Aws Associate Training

## Cloud Overview
* Amazon Web Services (AWS)
  * IaaS and PaaS and SaaS mixed
  * Ec2: Elastic Computer Cloud
    * service provides resizable compute capacity in the cloud
    * making it easy to deploy 
    * manage apps
  * S3: Simple Storage Service
    * scalable, durable storage service
    * ideal for storing large amount of data
  * RDS: relational database service
    * managed database service
    * operate, scale, a relational database
  * Lambda
    * serverless computing service
    * run ur code in response to events
    * manages underlying infrastructure
  * Elastic Load Balancing: 
    * Service distributes incoming traffic across multiple instances to ensure app available
  * Cloud Front
    * content delivery network CDN
    * securely delivers data, video, application and apis 
  * Amazon DynamoDB
    * managed nosql
    * fast, predictable performance
    * doc and key val data models
    * scalability
    * automatic data replication 
  * Aws
    * price
    * scalability
    * sec
    * reliability
    * innovation

## Fundamentals
* Core Concepts
  * Well Arch Tool
    * Six Pillar
      * operational Excellence
      * Sec
      * Relia
      * Performance
      * Cost
      * Sustainability
  * Shared Repoonsibility Model
    * aws
      * software
        * compute
        * storage
        * database
        * network
      * hardware
        * region
        * zone
        * edge
    * Customer
      * data
      * platform app iam
      * operating system, network, firewall
  * Command line interface
    * aws CLI
    * enable u to interact with aws services using commands
  * Basic support
    * one on one reponses
    * forum
    * health check
    * doc, tech paper
  * Customers with dev support plan
    * have basic plan
    * guidance
    * building block support
    * supports unlimited number of support cases
  * Business Enterprise
    * user case
    * aws trusted advisor
    * aws support api
    * this part software support
  * basic to high plan mobe
  * Monitoring Status
    * unassigned
    * work in progess wip
    * pending customer action
    * last status close case
## Tagging Aws Resources
* nice for organization
  * configure tags to be displayed with resources
  * search and filter resources by tag
  * Tags for cost allocation Cost allocation tags to track your AWS costs on a detailed level
  * Tag Everything! Apply your cost allocation tags across all resource types
* Tag Categories
  * Tech tag
    * name id 
    * application id
    * app role
    *  cluster
    * env
    * version
  * tag for automation
    * date time
    * opt in/ opt out
    * sec
  * business tag
    * project
    * owner
    * cost center
    * customer
  * sec tag
    * confidentiality
    * compliance

## Aws Service Quotas
* service overview
  * each aws account has default quotas
  * default quotas limit
    * linked with each aws services
    * has region specific
  * no service quotas then use aws support center
  * if a service adjustable, make a request for increasing a quota for service
  * if not, u cannot be increasing a quota for it

## Aws Cost Management:
* cost and usage important
  * cost managet
  * cost explorer
    * visualize ur cost data for further analysis
    * u can use filter
      * zone
      * service
      * region
      * tag
      * ec2 instance type
      * purchase option
  * Aws Budgets
    * aws usage
    * costs
    * cost visualization
    * provided by cost explorer
    * estimate your costs 
    * trans your aws usage
    * inclusding ur aws free tier usage
    * u can use aws budget to create amazon simple notification service
      * amazon sns
    * when u exceed ur budgeted amount
  * amazon cost anomaly detection:
    * aws cost anomaly detection feature uses ml and monitor ur cost usage and detect unusual spends
    * receive alerts, individually reports
    * cost anomaly detection beneficial
  * rightsizing recommendations
    * revies ur historical amazon ec2 usage
    * 
* Services
  * AWS Networking and Content Delivery services
  * AWS Compute services
  * AWS Storage services
  * Database services
  * Analytics
  * Developer Tools
  * Management tools
  * IoT
  * Security
  * Enterprise app
* Aws Networking
  * networking
    * amazon vpc : isolatd network for resources
    * aws transit gateway: connect vpc, on premises networks through a central hub
    * aws privatelink: connection for vpc, services, on premises apps
  * application networking
    * elastic load balancing :automaticallly distribute traffic across pool resources
      * ip addressess lambda functions
    * aws app mesh
      * app level networking for containers and microservices
    * a api gateway
      * create maintain secure api at any scale
  * edge networking
    * amazon cloud frount
      * deliver data videos apps, aps to customers, globally with low latency
    * route 53
      * route users to int apps with managed dns services
    * aws global acc
      * direct traffic aws global network to improve apps performance
  * network sec
    * aws shield
      * safeguard apps running on aws against ddos
    * aws waf
      * protect web apps common web explots
    * aws firewall maanger
      * configure and manage firewall rules
* Aws computer services
  * instances
    * amazon elastic computer cloud ec2
      * resizable computer cap, secure
    * amazon ec2 spot instances
      * run fault tolerant workload 
    * amazon ec2 autoscaling 
      * automatically add or remove 
    * amazon lightsail
      * easy to use cloud platform that offers you 
  * containers
    * ecs
    * ecr amazon elastic container registry
    * amazon elastic kubernetes service
    * amazon fargate
      * serverless ocmputer for containers
    * aws lambda
      * run code without think aobut servers
* amazon storage services
  * object storage
    * amazon s3
  * file sotrage
    * amazon elastic file system
    * amazon fsx for windows file server
    * amazon fsx for lustre
  * block storage
    * amazon elastic block store
* Database services
  * relational
    * amazon aurora, rds, redshift
  * key values
    * amazon dynamodb
  * in memo
    * amazon elasticache
    * memcache
    * amazon elasticache for redis
* aws sec, indentity, compliance services
  * identity, access management
    * aws identity, access management IAM
    * aws directory service
    * cognito
  * Detection
    * guardduty
    * inpector
      * analyze apps
    * config
      * record and evaluate configs
    * cloud train
      * track users
  * data protection
    * aws key management servier kms
    * cloud hsm
      * hardware based key storage for regulatory
    * certificate manager
      * manage deplot public private ssl tsl certificates
    * secrets maanger
      * rotate maange

## What to do
* what to save omoney on
  * aws cost explorer
  * trusted advisor
* to secure ur account use
  * lock away root user access keys
  * avoid using aws account root user
  * grant least privilege
  * use permissions with aws maanged policies
  * configure a strong password
  * enable mfa
* set budgets
  * set an elar, use set up budgets usign iaac
* Remmeber
  * set up multi factor authentication
  * do not share
  * do not commit ur credentials into git
  * terminate remove all created resources
  * delete nat gateway
  * dont keep instances running
  * track billing

## IAM resource
* service overview
  * it helps u control access to aws and account resources
    * save credentials private
    * create iam users under umbrella of ur account
    * enable temp access 
    * enable access resource aws account
  * without this, u have to create multiple aws accounts
    * billing subs
    * cannot control tasks
  * api request flow
    * https passed, validated on api endpoint, authenticated and authorized on iam, recorded in cloud train
  * price ocnsideration
    * aws and iam and aws sts are feature of your aws account 
  * aws account root user
    * dont use root user for everyday tasks, even administrative ones
      * create rotate disable or delete access ekys 
      * change root password 
  * iam identities
    * a user group is a collection of iam users managed as aunit
    * iam identity represesnt a user
  * iam users
    * entity, create in aws
    * person or service, who uses iam user to interact with aws
    * primary use
      * give people ability to sign in to aws management console 
      * a user in aws 
        * name password into management console
      * u grant permission by making it a member of group
  * user groups
    * a collection of iam users
    * specify persmissions for a collection of users
    * admins for example
    * a user cannot be identified as a principal in a resource based policy
    * a user group is a way to attach policies to multiple users at one time
  * iam roles
    * similar to user
    * can assume a role to temporarly take on different persmission for atask
  * iam role passing
## Type of redentials
* username password
* access keys
  * long term credentials 
  * acess key id 
  * a secret access key
  * do not provide ur access keys to a third party
* mfa
* iam policies
  * it is set of permissions, controls access to aws resources
* role
  * trust relationsship
    * resource based policy
    * who is allowed to assume this role
  * permissions
    * identity based policy
    * what can u do after you assume this role
  * a policy is entity in aws attached to identity or resource fines permission
  * to assume role, use security token service sts
    * gives temp credentials to use the role
* sts response
  * access key
  * secret key
  * sec token
  * expiration
* passwrole
  * iam > users > permissions
  * it is a action block 
  * but not action
  * checking sec
  * iam:passrole pernission
* iam policy simulator
  * policies are json format
  * use instance profile to pass iam role to ec2 instance
  * by default, iam role has max sesion duration 1 hour, u can be changed
  * configure many services, pass iam role to serviec
* cautions
  * roles and policies are global aws resources, their names must be unique across aws account

## Aws Storage Services
* ebs 
  * elastic block store
  * a block level storage service offered by aws provides high available, low latency block level storage volumes for use 
  * for ec2
  * ebs volumes are designed for use single ec2 INSTANCE 
  * can be attached and detached
* efs
  * elastic file system
  * fully managed
  * highly scalable file storage service
    * proviced a simple scalable file system for use with ec2 instances
  * eps is designed to support multiple ec2 instances
* fsx
  * provides u with native compatilibity of third part file systems
  * feature for workloads 
* s3
  * simple storage service
  * scalable durable secure
  * s3 allow to store and retrieve any amount of data from anywhere
  * block
    * amazon ebs
    * amazon ec3 instance store
  * file 
    * amazon efs
  * object
    * amazon s3
    * amazon glacier
* ebs 
  * elastic block storage
  * easy to use
  * high performance
  * block storage service
    * can be used with ec2
* efs
  * amazon efs
  * file sharing service
  * manage file shares
  * mount them on cloud
  * use nfsv3 protocol
  * scalable cloud based 
* amazon fsx
  * thid part file system
  * windows based storage
  * high performance computing hpc
  * ml
  * electronic design automation eda
* simple storage service s3
  * amazon simple storage service 
  * amazon s3
  * highly scalable fast durable solution

## Aws Compute Services
* Elastic Compute Cloud EC2
  * service description
    * scalable computing cap in amazon web services aws 
    * virtual servers
* enable auto scaling
  * amazon ec2, 
  * you have correct numbver of amazon ec2 instances
  * load your app
  * create collections of ec2 instances, auto scaling groups
* load balancing
  * single point of contact for clients
  * load balancer distributes incoming application traffic acreoss multiple targets 

## VPC virtual network dedicated to aws account
* virtual private cloud
  * isolated section of amazon web services aws
  * uve compelte control over ur virtual networking env, including selection of ip range, creation of subnets, 
* elastic network interfaces enis
  * virtual network interface, u can attach to instance amazon vpc 
  * can have one public ip address and multiple private ip addresses 
  * multiple privacte ip -> one of them primary
  * assigning to second network via eni allows it to be dual homed
  * and eni created independently of particular instance persists regardless of life time of any instance to which it is attached
  * create maangement network, use netowrk and securitt
  * create dual homed instances 
* IPV6
  * associate ipv6 cidr block with vpc subnets 
  * public, reaable over internet
* common case
  * creation of management network
    * pubnlic facing app web servers in public submet
      * but lock down ssh access down to private subnet on secondart network interface
  * enis 
    * primary netowrk interface for docker containers
    * ecs using fargate, allow fargate handle complex networking
    * set firewalls in place using sec group 
      * launched into private subnets
* elastic ip addresses
  * pool of public ip addresses in each region makes them available for u associate to resources within amazon vpc
  * static
  * pbulic ip in pool for region, u can allocate to account
  * relase
  * eips allow u maintain set of ip addresses, remain fixed while underlying infrastructure
  * use cases
    * need a fixed public ip
    * mask failure of instance by quickly remapping address to another in same zone
* networking address translation nat and nat gateways
  * private subnet any instance by  default
    * cant communicate with internet through igw
  * use nat gate way not nat instane
  * gateway, provides better availability and higher bandwidth 
* vpc endpoint
  * connect ur vpc to supported aws services and vpc endpoint services powered by privatelink without requiring an internet gateway
  * nat device, vpn connection or aws direct connection connection. 
  * vpc not require public ip to communicate
* vpc peering
  * connection between two amazon vpc
* transit gateway tgw
  * large numbe of vpcs 
  * vpc to vpc communication management
  * use cases
    * delive app 
    * move to global scale
    * repond to spikes in demand
    * host multicast
* vpc flow logs 
  * capture info about ip traffic goin to from networking interface in vpc 
  * flow log to amazon cloudwatch log or amazon s3
* route 53
  * domain name system dns
  * fully with ipv6 ok
  * use cases
    * trafifc flow
    * latendeny based routing
    * geo dns
    * private dns for amazon vpc

## Provisioning Services
* cloud formation
  * helps you model and set up ur amazon web services resources
  * u can spend less time managing those resources and more time focusing on ur apps run in aws
  * u can create a template that describes all the aws resources u want 
* Use cases
  * builds infrastructure using text templates or visually with cloudformation designer
  * infrastructure as code implementation through version control
  * change sets allow to preview proposed changes before applying
  * custom extensions creation using aws lambda
* Pricing Consideerations
  * no additional charge for the service
* authoring with json yaml
* safety controls
* preview changes to the user environment
* dependency maangement
* cross account and cross region management
* extensibility
* cloud formation
  * template and stack
    * template contains all resources u want to be created using json or taml
    * stack logical unit of related resources
    * u can create update and delete a collection of resources
      * by creating updating and deleting stacks
    * before making changes to ur resources, generate a change set
      * summary of proposed changes
    * change sets allow u to see how ur changes might impact ur running resources 
* template basics
  * a template is declaration of aws resources that make up a stack
  * template is stored as a textfile whose format complies with json or ymal standard
  * they re just text files, u can create and edit them in any text editor
    * manage them in ur source control system
  * template include several major sections
  * the resource section is the only required section 

## Modules Registry
* modules are building block cna be reused acress multiple cloud formation templates
  * native cloud formation resource
* Deploying apps
  * u can use aws cloudformation to automatically install configure and start apps on amazon ec2 instances
  * duplicate deplotments and update existing installlations without connecting directly to instance 
  * can save u a lot of time and effort
* cloud formation includes a set of helper
  * cfn init
  * cnf signal
  * cfn get meta data
  * cfn hup
  * u can call them to install configure and update apps
* Aws systems manager
  * to view and control ur infrastructure on aws
  * configures for u
  * helps u configure and maintain ur instance
  * support ec2
  * on premises server
  * vms 
    * including vms in other cloud environments

## Aws Database Service
* RDS 
  * relational
  * only encrypt amazon rds db instnace when u create it, not after
  * cant turn off encryted snapshot of and uncrypted using same kms keys as the db instance
  * cannot have encrypted real replica of an unencrypted db instance or unencrypted read replica of an encrypted db instance
  * encrypted real replicas must be encrypted with same kmw key as source db instance when btoh are in same aws region
  * cannot restore unencrypted backup or snapshot to encrypted db instance
  * to copy snapshot from one region to another, u must specify the kms key in destination aws region
  * cant unencrypt an encrypted db instance, u can export data from an encrypted db instan and import data into unencrypted db instance
* Dynamodb 
  * key value
* Document
  * Document db
* in memory
  * elastic cache
    * resids
* graph
  * neptune
* time series 
  * timestean
* ledger
  * qldb
* search
  * amazon elastic searchservice
* amazon relational database service RDS
  * set up, operate, scale a relational databases sql in aws cloud
  * cost effecient, resizable cap for industry standard relational database and manages common database adiministration tasks
  * use cases
    * e commerca apps
    * mobile onle games
    * web mobile apps
* monitoring
  * event recorded and rotation period of record
* Amazon dynamodb
  * fully managed no sql
  * fast predictable performance
  * table item attributes are core
    * a table collection of items
    * each item is collection of attributes
  * consistent, stronglyraeds
  * read / write ap modes
  * use cases
    * when sql database, rds is not ok then use this
    * really if fast readm dynamod accelerator dax 
      * cache query data
    * easy to udnerstand 
  * governance
    * on demand backup cap
      * fully backups ur table for long term retention and archival for regulatory
      * on demand backups and enable point in time recovery for amazon dynamodb table
      * point in time recovery helps protect tables from accidental write or delete operations
        * with point in time recovery, restore a table any point in time during last 35 days
      * it allows u delete expired items from tables automatically to help u reduce storage usage and cost of storing data 
      * integrated with cloudwatch, allowing u enable logging and monitoring
  * cautions
    * a number of quotas u need to pay attention to 
    * limits write and read 
* AMAZON ELASTICACHE
  * SET UP MANAGE SCALE DSITRIBUTES IN MEMO CACHE ENV IN CLOUD
  * high performance, resizable and cost effective in memory cache while removing complexity associated with deploying and managing a distributed cache env
  * redis and memcache engine work with
  * use cases and considerations
    * building low latenct data 
    * eases backend databsse load
    * accelerated performance of app
    * cache
    * in memo data
  * governance
    * elasaticahe fully integrated with aws cloud watch for metrics 
    * cloud trail for logging
    * sns: to sending all impotant event to a specific topic
  * security 
    * several types of encryption and role based access control
  * cautions
    * doesnt have replication like redis does
* Self Check
  * What's the difference between Relational, NoSQL and In-Memory databases?
  * If you need to store simple data(string/integer) in cache, will you use Redis or Memcached?
  * When you want to make sure you get the latest data from DynamoDB, which type of read will you use?
  * Can you make your DynamoDB highly available? If yes, how?
  * How can you backup Database services?
  * What is RDS? What engines does it support?
  * What is RDS pricing?
  * Can you make your RDS instance highly available? If yes, how?
  * What is read replica in RDS and how it works?
  * What RDS operational (maintenance, monitoring) practices do you know?
  * What RDS capacity planning best practices do you know?
  * What RDS testing and profiling best practices do you know?
  * What are the advantages of RDS over manually managed databases?
  * What is the difference between multi-AZ deployment and read replicas in RDS?
  * What security features does RDS provide?
  * What is AWS Aurora?
  * You need to make a snapshot in RDS at a specific time, is that possible? If yes, how?
## AWS Application Integration
* Simple queue service
  * fully managed message queuing service, that enables u to decouple and scale microservices
  * distributes system 
  * serverless application.
  * sqs eliminates complexity and overhead associated with managing and operating message
  * send store receive messages 
* offers, secure, durable, hosted queue, let u integrate decouple distributes software systems
* proviced generic web services api, u can access using any lang
  * default queue type, standard queue support unlimited api almost per second per api action.
  * at least once message delivery
* fifo
  * limited number of transtion tps, .fifo suffix, 80 char,
  * order
  * complements
  * exatcly once processing
  * not duplicated
  * dead letter queues
    * queeu of standard queue must also be standard queue
    * benefits
      * configure alarm for any messages delivered to dead letter
      * examine logs for exceptions
      * analyze content of message delivered to dead letter
      * determine whether u have given ur consumer sufficient time to process messages
* standard queue
  * decouple live user request from intensive bg work 
  * allocate taks to multiple worker nodes
  * batch messages for future processing
  * at least once delivery
    * at least onece delivery
      * amazon sqs stores copies of ur messages on multiple servers 
      * 
* max is 256 kb
* Simple notifiation service
  * sns, messaging servie for both app to app a2a app to person a2p 
  * client can subscrive to kdf sqs lambda http email mobile sms
  * no upfront costs 
  
* Self-check 
  * What is a message queue? 
  * When will you use SQS and when will you use SNS? 
  * Is it possible  to scale an Auto Scaling Group using metrics such as SQS queue depth, or numbers of SNS messages?
  * What is SQS pricing? 
  * You want to collect notifications from all your AWS regions using SNS and forward them to external system. How can you design such solution?
  * What is FIFO queue?

# Amazon Serverless
* amazon api gateway
  * glossary
  * amazon api gateway
    * create, publish, maintain, monitor, secure appis at any scale
    * front door of aps
    * create restful api and websocket
      * enable real time two way commmunicatoin apps
      * serverless workloads as well as web apps
    * handles al ltaks involved in acepting and processing up 
  * http based 
  * support ssl
  * enable stateless client server communication
  * implement standard http methods 
  * use cases
    * api and app dev
    * api dev
      * create and deploys an api to enable required functionality in api gateway
      * api dev must be an iam user in aws account that owns the api
    * app dev
      * builds functioning app to call aws services by invoking websocket or rest api 
      * customer of api dev
      * not need to have aws 
      * provided api either 
* Aws Lambda
  * serverless computer service 
  * response to events and automatically manages the underlying computer resources for u
  * run ur code on high availablity compter infrasture and performs all administation of compute resources, including server 
  * and operation system maintenance
  * code is lambda function
  * start to wait for trigger requests
  * each function includes ur coe as well as some associated configuration infromation
  * including function name an resource requirements
  * stateless
  * no affinity
  * use cases
    * web aps
      * static webs
      * coplex web
      * pacages
    * backend
      * app 
      * mobile 
      * iot
    * data processing
      * real time
      * map 
      * batch
    * chat bot
      * powering chat 
    * amazon alexa
      * voice enabled app
      * alexa skills kit
    * it 
      * policy engine
      * extending aws service
      * infrastructure management
  * limits
    * max 15 min
    * parallel
    * default safety throttle for number of concurrent executions per account per region
  * Serverless Application model
    * building serverless apps
    * shorthand syntax to express functions api databases evenr source mapping 
  * why sam
    * simgle deploymenet configuration
    * local debugging and testing
    * deep integration with development tool
    * built in best practices
    * extension of aws cloudformation
* Self Check
  * What is the biggest benefit of AWS Lambda?  
  * What ways of triggering a Lambda do you know?  
  * What is the contract of Lambda function?  
  * What is Lambda pricing?  
  * Which code libraries/frameworks are reasonable to use in Lambda?  
  * How Lambda instances are reused? How to prepare the Lambda code for that?  
  * What programming languages does Lambda support?  
  * What is the difference between synchronous and asynchronous Lambda invocations?  
  * What is Lambda concurrency?  
  * What kinds of Lambda concurrency allocations are there?  
  * What AWS resources can Lambda access? How?  
  * What are the advantages of API Gateway endpoints over traditional web applications?  
  * What are the typical API Gateway use cases? What is the use case for combining API GW with Lambda?  
  * What is the use case for combining API GW with Lambda?  
  * What is API Gateway pricing?

## CI CD with Aws
* ci cd stands for continuoius integration and continuous deployment and delivery
  * continuous integration 
    * in code changes, merge and build and test automatically
    * build or integration stage of software release process and entails both an automation component
    * a cultural component
    * ci often includes so called request build or checks fir each pull or merge request new code is checked
  * Continuous delivery
    * software dev practice where code changes are automatically prepared for release to production
    * multiple, parallel test stages before a production deployment
  * ultimate goal shorten time to market
    * allows to detect issues as early as possible 
  * tools
    * jenkins
    * gitlab
    * travisci
    * actions
    * teamcity
    * azure devops
  * system overview
    * codecommit
      * host private git repos
      * integration with other aws servies
      * pull request approval templates
      * access control
    * code build 
      * fully managed
      * on demand
      * out of box
      * 
    * codedeploy
      * code
      * serverless
      * web configs files
      * executables
      * packages
      * scripts
      * multimedia files
      * primary components
        * app
        * compute platform
        * deployment config
        * deployment type
        * iam isntance profile
        * revision
        * target revision
        * service role
        * appspec file
    * code pileline
      * cd service
      * use to model visualize automate stesp
      * work flow and consist of stages
        * each stage, logical unit use to isolate an env and limit number of concurrent changes
        * each stage made up of series of serial or parallel actions
    * app runner
      * containerized web app in aws
      * builds, dploys apps, distributes traffic with encrytions
      * fargate
      * build service 
      * ecs cluster 
      * load balancer
      * pros
        * load balancing under hood
        * simpler than aws ecs and fargate
        * custom domain name
        * can be fully private
      * drawbacks
        * cannot pull image outside ecr
        * cannot use secret manager
        * only python and node js supported in build mode
        * no scale t o0 
        * only github can be used as source code
      * 
    * compute platforms
      * ec2 
    * AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software
    
* Self Check
  * How to set up different deployment strategies (blue-green, canary) via the AWS CodeDeploy?  
  * What is application, revision, deployment, deployment configuration, and deployment group in terms of AWS CodeDeploy?  
  * What is stage, action and transition in CodePipeline?  
  * What is pricing for the AWS CodeCommit/AWS CodeDeploy/AWS CodePipeline services?  
  * What is CI?  
  * What is CD (delivery)?  
  * What is CD (deployment)?  
  * What CodePipeline best practices do you know?  
  * How easy is it to migrate from more traditional services like GitHub/GitLab onto CodeCommit?  
  * How would you compare CodeCommit to Git?  
  * What are the key elements of an app spec in CodeDeploy?  
  * What are the key elements of a build spec in CodeBuild?  
  * What AWS services may aid CodeBuild execution?  
  * What 3rd party tools and other AWS services may participate CodePipeline execution?  

## What is lambda
* u can implement aws labda runtime in any language
* How can a developer provide Lambda code? 
  * By uploading a .zip file
  * By editing inline
  * From an S3 bucket
* build specification (buildspec) files
  * collection of build command and related settings, in yaml format, that codebuilds uses to run a build
 
* In a default VPC, all EC2 instances are assigned with 2 IP addresses at launch. What are they?
  * Public IP address
  * Private IP address
  


How do you author a Lambda in a programming language that AWS does not support?
-Create a Lambda function with a custom runtime and reference the function in your Lambda
Create a Lambda layer with a custom runtime and reference the layer in your lambda
You cannot use Lambda in this situation
-Create a Lambda function with a custom runtime


Which tasks are available ONLY for the root user? (Select TWO answers)
Change your account settings (account name, email address, root user password, and root user access keys); not only
Change your IAM user settings (name, passowrd, access keys, MFA etc.); not with first
Activate IAM access to the Billing and Cost Management console;
Set up budget and free tier usage alerts.