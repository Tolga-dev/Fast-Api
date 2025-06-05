# Amazon Service Personal Notes

## How to choose aws services
* Route53 : DNS records

## AWS Essential Setup
* IAM : for identity and Access Management
* AWS recommends that you follow the rule of only granting 
  * least-privilege or only giving your team members the 
  * bare minimum of rights over your AWS account that 
  * they need to perform their jobs well
* ARN, or A-R-N, which stands for Amazon Resource Names,
  * all of your cloud infrastructure, including your servers,
  * networking components, storage, IAM users, your roles,
  * almost everything will have a unique ARN
* The Cost Explorer will give you some charts and reports 
  * that will allow you to see a breakdown of which
  * AWS services are being included in your monthly total. 
  * Another way to create a budget.

## On Premise to AWS
* 2006 Amazon Web Services launched
* virtual server is just a software abstraction that 
  * allows a physical server like this to divide up
  * its CPU and its ram and its disk resources, 
  * which is called the bare metal, and 
  * run different virtual servers on top of the bare metal
* Elastic Compute Cloud, which is abbreviated as EC2
  * when traffic increases, and then shrinking back down again when the traffic drops off.
* For EC2 instances, this feature was called Auto Scaling
* Simple Storage Service, and it's abbreviated as S3.
  * S3 was Dropbox before there was Dropbox
* Shared Responsibility Model, where you, and Amazon Web Services, share different responsibilities in keeping your servers up
  *  AWS handles the data center and its physical security so no one can sneak into the data center and steal your files, and AWS holds certifications
* ISAAS insfrastructure as a service
  * u rent virtual infrastructure from cloud provider, pay for only what u use
  * u do
    * os update
    * backups
    * firewalls
    * maintenance schedules
* ECS and multi-region load balancing,

## IAAS Compute
* Virtual machines in AWS are called Amazon Machine Images or AMI
* The instance types will start with t2, t3, or c1 and so on, 
  * and this is the instance family
* The T and M families are the most commonly 
  * used general purpose instances
* T instance family is a burstable CPU threshold.
* M class don't use the CPU credits 
* The memory optimized R an X classes
  * are for workloads that need more memory
* a t2.micro because it's a really small instance
* if you reboot an instance, it comes back up faster
  * but it stays on the same physical server it was before
* if 1, or 2, or 10 clones of your single server come online,
  * that your application can load balance your traffic
  * across all of these new servers.
  * Now this is called horizontal scaling 
* If you think of a busy grocery store, 
  * the manager will open several new checkout
  * lanes to reduce wait time. When the rush is over
  * , they'll close those extra checkout lanes. 
  * This is different than vertical scaling, 
* Pay up front for one year
  * pay hold up front on eyear pay rest monthlu
  * pay monthly for one year

## IaaS networking
* Amazon uses security groups, which act as simple firewalls,
  * which allow you to expose only the parts of your server 
  * that are configured for public internet traffic.
* Private IP Ranges : Non routable
  * from
    * 10.0.0.0
    * 172.16.0.0
    * 192.168.0.0
  * To
    * 10.255.255.255
    * 172.31.255.255
    * 192.168.255.255
  * CIDR Notation
    * 10.0.0.0/8
    * 172.16.0.0/12
    * 192.168.0.0/16
* Virtual Private Cloud (VPC)
  * Every VPC will have a range of non-routable IPs or private IPs
  * Within your home network, when you try to link two computers 
    * together with a switch, also called your Local Area Network or LAN
* Subnet
  * group of sequential ips within a network space
* A subnet is a group of sequential IP addresses and it's a way
  * for you to divide up your network of available IP ranges 
  * into smaller buckets so that
  * you can write networking rules that apply to a group of addresses
* you're going to be building out a lot of servers within EC2,
  * it's best to plan out your VPC and subnets now.
* NAT Network address translation 
  *  Your router at home creates a private network,
    * much like a VPC, that links all of your 
    * local computers and devices together, 
    * either through wired connections or 
    * through wireless ones. It then routes 
    * traffic from the public internet (plastic rubbing)
    * to your private network through a technique called
    * network address translation, or NAT. This allows 
    * your wide area network interface
    * to get a single public IP address from your internet provider,
* there's no doorknob on the outside of the door.
  * In AWS, this is called a NAT gateway, 
  * and it attaches to your VPC, and it creates
  * a door to the internet that can only be
  * opened from inside the VPC
* the only way to get around this limitation in NAT is to go into
  * your router settings, usually turn on a feature that's called 
  * port forwarding, and then that will tell the router to always 
  * route certain types of public-initiated traffic to a specific
  * computer on your private network
  * Now the door to your router has a doorknob on both sides, and it can be opened from either end
  * in AWS, this is called an internet gateway.
  * this is the IP address that your NAT gateway is going to 
  * use on its WAN port, and 
  * any servers using the NAT gateway will appear to the
  * outside world
* Static addresses with Elastic IPs
  * each of our instances could have a public 
    * IP address, AWS randomly assigned a public
    * IP to each of our servers
  * Elastic IPs come from Amazon's pool of IP addresses,
* Using VPNs to access private subnets
  * VPC
    * with a single public subnet and 
    * One way to securely connect to your instances is 
    * by using a bastion host. A bastion host is 
    * an instance you put in the public subnet that 
    * is really locked down and monitored, and you connect to
    * this machine first, and
    * then from there, you make connections to the other servers
    * in your VPC.
  * an automation language for infrastructure called CloudFormation,
  * Session Manager is available from within 
    * the Systems Manager dashboard from within the AWS console.
  *  If you need a fast, reliable and stable connection between
  * your data center and AWS, look at AWS Direct Connect.
    * This provides a physical connection between your
    * data center and AWS, and it's used in large-scale hybrid deployments
* Scaling with Elastic Load Balancer (ELB)
  *  load balancer, and it splits up the incoming traffic and balances it 
  * among your healthy servers. It's a key component to horizontal scaling
  * elastic load balancer
* Network load balancers fast, not looking too closely at the traffic coming in
* Gateway load balancers switching traffic coming into virtual networking appliances made 
  * by vendors that aren't AWS, such as Cisco virtual firewalls. 
* Application load balancers web traffic. incoming traffic and route it based on a set of rules
* ALB 
  * availability zones your instances are running in
  * name of the security group 
  * Load balancers route their traffic to target groups which include your target servers

## IAAS Storage
* Hard drives with Elastic Block Store (EBS)
  * Amazon's primary storage service for EC2 servers is called Elastic Block Store, 
    * elastic because it can stretch in size when you need it to.
* The EBS volume is just a snapshot of its hard drive
  * If you have an application where you need to take a lot of snapshots
  * of a data volume that frequently changes, such as a database server,
  * you can create a second EBS volume for your 
  * instance and configure your database to store its data files on this new volume
* EBS volumes are fast, which is why they are the default for new EC2 instances,
* EFS, Elastic FileSystem
* S3 Simple Storage Service
  * Dropbox
  * slower EBS ELFS
  * no need a server
* CLI Command Line Interface
* AWS SDK
  * Software dev kit to interface with s3 from our source code on our server
  *  AWS SDK for PHP using a package manager for PHP called Composer.
* IAM roles for EC2
  * IAM identity access management has roles
    * role, aws, what permissions this ec2 instance has
* iam is controlled by aws global region 
  * IAM entities are the users and roles that want to access awas resource
  * a group will never access aws services directly
  * group is not entity
  * iam policy is inside group will want to acess things 
* Long-term storage with S3 Glacier
  * s3 has, bucket system
  * s3 called glacier
  * monthly fee 
  * This can be much cheaper from moving a lot of data
    * than paying the data transfer costs for using S3 over the public internet.
* Cloud Front
  * s3 use to host static content for website, image videos
  * with cloud front
  * s3 bucket to edge server all over the world
  * load faster for them
  * Content delivery network or cdn
    * mirror ur bucket all across the world
    * cheaper than plane
  * replicate this bucket,
    * more speed and remove redundancy
* for more speed, use aws global accelerator
  * Edge locations is to turn on S3 Transfer acceleration

## Dataabse as a service dbaas
* cloud provider manages the database servers and backups
  * rea and write ur data to manage service
* Questions
  * what data
  * how much
  * read throughput
  * write throughput
  * uptime
* relational big data
* queue relational
* no sql
  * object base
* cloud vendor helps you, manager servers and backupds of your data
  * databse as a servicer dbasS
  * lets u focus on data its self, optimizing
  * AWS Data Migration Service
  *  your on-premise relational database and create a real-time in-sync clone of your database
* Relational database service RDS 
  * EC2 instances, the database backups, the database engine upgrade
    * service called relational database service
    * rds
    * upports postgres, mysql, sql, oracle
  * use console rds
    * and create database
    * transfer data 
* aurora
  * server management, by aws
  * run serverless
  * dont even manager instances
* Nosql
  * storage, retrieval data that is not stored in tabular relational format
  * relational vs json  nosql
  * a database engine, isnt relational database
  * no sql standard lang
  * nice for storing datain a schemaless format
* most popular key value store that they offeris called DynamoDB
  * database a a service
  * dont do any management of it
  * just pay and use
  * easier than rds
  * up down
  * global tables
  * let u replicate
  * speed and redundancy
* document db
  * mongo
  * dont deal with servers and mongo clusters
* memory caches
  * help u deploy one of elasticache aws
    * help u manage and deploy two one commen types
      * elasticcache
        * redis
          * popular
        * memcached
          * support php open soruce app

* A queue temporarily store the data that you need to write, so that a spike in 
  * incoming data doesn't cause your database to melt down.
* AWS, two such services for creating a queue are Kinesis and Simple Queue Service
* Redshift
* Kinesis
  * Kinesis is able to handle a large stream of incoming data
* Simple Queue Service SqS
  * SQS is more popular and it's simpler to use
  * expensive 
* Simple Notification Service SNS
  * Simple Notification Service, or SNS, can be used to push out a message

## Platform as a Service
* Elastic BeanStalk
  * if you have a single code base for your project
  * host ur site
  * high availability 
  * using rds for database and efs to store the uploaded files
* Running containers on AWS
  * containers,
    * to take a large monolithic single application and break its features down into smaller 
      * services
  * the most popular service they have is called Elastic Container Service
  * cluster
    * create nodes
      * ec2
      * load balanced
* Fargate 
  * bunch of on demand nodes
  * willing to run any number of containers
* Ecs
  * simple less popular basic
* elastic kubernetes services
  * runs everywhere, popular, advanced networking
* kubernets, open source, google
  * borg
  * server clusters
  * in amazong it is elastic kubernets servicer or eks
* Function as aservicer
  * a small chunk of code that runs on your cloud platform every time an event occurs
* Serverless architecture
  * an application that responds to incoming events without need for always on server that u manages
* Serverless functions with lambda
  * platform as server offering, subset
* using lambda, create functions, run a single execution of your code as many times
  * serverless 
* debugging problems with lambda function, helps to understand magic behind
* use simple email service, ses
  * LAMBDA takes input like function 
* Managing long running jobs
  * lambda runs quickly
    * single one cant be longer than 15 min
  * if data large, need to look at for batch processing workflows
  * crunch in backend, use aws batch, manage and schedule jobs can use ec2 spot instances
  * spot instances, like priceline for airfare

## Software as a Service SaaS
* User authentication for your app
  * engine room
* Cognito
  * sign in integrations with other providesr
    * google 
    * facebook
* Grapql api, not rest api
  * look appsync
* api gate way
  * rest api end point
* AW X ray
  * performs x ray scan on ur clod 
  * let u know ur slow endpoint 
* Sagemaker
  * ai ml models
* Comprehend 
  * llm
  * chatbots
* Polly
  * dynamic text into some pretty life like voices
* Rekognition
  * can find face in a image
* textract
  * text translation langugage

## Devops
* . DevOps removes the barrier between these two teams and 
  * creates a single team that has responsibility over development and operations
* , is the site running well?
* Continuous Integration CI
  * Code pipeline
    * a workflow that automatically pulls ur code
  * Codebuild
    * build project and runs tests
  * smaller changes to the code are automatically tested whenever a change is made by any developer
* Continuous Deployment CD
  * Tested changes are automatically deployed to a staging environment and can then
    * be automatically sent into productions
* Agile
  * key, release early and often
* A key component is insfrastructure as code
  * packing manifers of everything that should be on that server 
* Deployment automation tools
  * can check all of servers and set configurations back to original state
  * puppet, chef, ansible
    * useing chef or puppet
      * aws opswork
  * has cloud formation
  * ansible chef shine management and configration several servers
  * cloud formation goes deeper for aws
* Monitoring with cloud watch
  * one change that devops made
    * service operates is to expand the role of monitoring
    * is the site up
    * how is the site performing
  * sms 
    * twilio
    * status page
    * high level status of various parts of their service
    * red down
    * yellow problem
    * green ok
  * cloudwatch
    * log errors within application or functions
    * spot problems track errors
  * error messages from app
    * application performance monitoring or APM
    * new relic
    * dynatrace
    * datadog
* Devops ML
  * cloud watch
    * logs of metris
    * resources
* Devops guru
  * uses ml to look operations data 
  * notify u 
  * performance ossues
* code guru
  * your soruce code repo
  * new change
  * wond ficx but add comment
  * security suggestions
  * out of api
  * screet keys alert

## Security on Aws
* waf OR WEB APPLICATION FIREWALL, SHIULD
  * connect to ur load balancer
  * filtesr
  * customers
  * and block others
  * high risk of being targeted by botnet 
* use rule of waf
  * use guardduty
    * night security guard
    * checks logs
* macie
  * scan cloud resources
  * sensetive data checks
  * report it
* User terraform for many servers situations
  * automations 
  * run commands 
* use ops center 
  * as a central console to tie cloudwatch, could train 
* Traceability with CloudTrail and Security Hub
  * could train, internally
    * logs requests 
* Security hub makes under one dashboard
* Investigate threats with AWS Detective
  * AWS detective can log and scan
  * cloud train data and tell which user made it

## Conclusion
* Terminate EC2 instances
* release elastic ip
* delete app load balancer
* delete ebs volumes
* delete s3 buckets and cloudfrint distributions
* AWS Well-Architected Framework.
  * Operations excellence
  * cost optimization
  * security 
  * reliability
  * performance efficiency
  * cost optimization
  * sustainability
* Framerwork compose of pillar
  * design principles
* Cloud Goes live
  * switch to business support plan
* Study for exam
  * security services
  * shared responsibility model
  * well arch framework
  * IAM
* AWS Cloud Practitioner Certification (CLF-C01)
  * the Shared Responsibility Model


mulakatin sonuna kadar %20 lik kisim olacak
yedek listesi olacak
* wp addersine davetye duscek
* 31 mayisa kadar 17 kadar cevap vermen lazim
* daha sonrasinda, ben girmek istiyorum dersen 
  * gerceklestirelemez
* ik belge talep eder
  * ogrenci belgesi 
  * or mezun belgesi pdf hali
* 2 haziran pazar 17 00 kadar
* ondan sonra program gg
* belgeler gitti ok
  * 3 hazira saliya kadar onlar yollacak
  * kaseli imzali staj kabul belgesi
  * ogrenciler okula verip bunu sigorta icin olacak
    * ogrenci degilsen kendin oducen sigortayi
* staj dosya masrafi
* 4 haziran carsamba 17 ye kadar
  * staj kabul belgesiyle ogrenci islerine basvur
  * staj sigorta masrafinim karsilanmasini talep ediyorum
* ogrenci islerinden word hlalinde digital staj formu word halisye talep edilmeli
  * univelere, kasesiz ve imsasiz
* 4 haziran carsamba, 
  * 1800 tl 
  * kendi shasi bisiler yaparsaniz
  * 
















