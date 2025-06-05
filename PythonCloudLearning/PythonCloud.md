# Cloud Overview

## Cloud Overview
* Welcome
  * AWS
  * GCP
  * MA
* Cloud Core Concepts
  *  What is cloud
    * abstracting, pooling, and sharing computing resources
      * servers, switches, routers, operating systems, and security software
    * cloud computing
      * renting resources over internet
      * cpu, hardware
    * cloud projects
      * adapting cloud tech as much as possible to achieve business goals
    * could specialist
      * to helps to solve business problems
  * Benefits
    * Cost efficiency
    * scalability
      * Vertical
        * involves increasing size of each resource
        * more cpu, memory
      * Horizontal
        * adding more resource to existing cluster
        * most likely same size 
    * elasticity
    * service variety
    * reliability
    * security
  * Cloud Types
    * Deployment models
      * private
        * dedicated hardware, 
        * bridge between pubilc and legacy on premises systems
        * static, how much storage has been paid for 
        * internally or independent contractor
      * public
        * run by specialist provider in data center 
        * accessible via internet or private connections
      * hybrid
        * not good for sensetive
          * use private
      * multi
        * multiple computing
        * storage services
  * Customer Needs
    * consumer
      * personal
        * dropbox
        * icloud
    * vertical
      * healthcare, financial services, government operations
    * external
      * public or private 
    * internal
      * private cloud instance provided and supported
  * Cloud terms glossary
* Cloud Service Models
  * As a service
    * Infrastructure as a service - iaas
      * requires engineers and architects
        * cisco
        * microsoft azure
        * amazon web services
        * google compute engine
        * digital ocean
      * if u need to control everything
      * no finances
      * want to purchase only what you consume or need
      * need to be able to change out specific hardware
      * dont use
        * doesnt have skill
        * vendor does not meet your sec standards
    * Platform as aservice - paas
      * additional layer of abstaction over laas
      * os, pre built tools, testing, runtime, middle ware, and databases
        * azure app
        * salesforce
        * google app engine
        * aws elastic beanstalk
        * openshift
      * devs are ok standardized building blocks
      * no internal want to own service, requires specialized caps
      * services outside, your core business are, auto, deployment, monitoring
      * dont use 
        * ur project needs proprietary
        * low level langs
        * app requires u to customize hardware 
        * 
    * software as a service - saas
      * pay
      * no code 
      * system update
      * security
      * essential tasks
        * dropbox
        * youtube
      * standard solutions
      * does not have skill
      * more cost effective
      * saas ok, data privacy, service, configs options
      * dont use
        * high level of config, custom or specialist integs
        * u can run it urself more effectievly
        * extensive exp of business process
* Containers and Serverless
  * Containers
    * application, image lib
    * container servicer op hardware
    * virtual machine
      * app, image lib, op, hyperviser, op, hardware
  * Docker
    * docker daemon
      * services, on host, executes commands
      * image, container, networks, storage
    * rest api
      * api
      * used by applications to execute docker
    * docker cli
      * interface developers to execute docker commands via daemon
  * Kubernetes
    * most popular orchestration system
    * open source container to automate deployment, scaling, managements of application software
    * u can run by yourself, needs skills
    * abstraction layer
      * performes key functions and allows the dev team 
  * serverless
    * imagine deploying an application without having to think about server management
    * powered by cloud serveces
    * to build scalable, cost efficient app
  * factor app
    * 12
      * code base
        * single code base each app to track
      * dependencies
        * declared and isolated
        * use pack manager
      * config
        * separete config and code
      * backing services
        * 7 portability, 
      * build release run
        * separate them, with each release having a unique id allowing back
      * stateless processes
        * app should be able to execute as single stateless process
      * port binding
        * services should be visible and self contained via port ibnding and shared object libs
      * concurrency
        * not single instance
        * break your app into smaller processes
      * disposability
        * run and stop quickly
      * dev and production 
        * dev, staging, production env should be as similar as possible to limit 
      * logs
        * capture logs as continuous events streams 
      * admin processes
        * admin tasks should be one off and run via app codebase
  * Cloud Native apps
    * for a cloud computing arch
* Cloud Ownership
  * assessment
    * total cost
      * tco - total cost of ownership
      * cost of current data center
      * cost of estimatd cloud infrastructure
      * cost of cloud migration execution
      * additional post migration cost
  * preparation
    * what is cloud migration
      * hosting sites to the cloud
      * similar to physical relocation
      * not packing or transferring real objects
      * just data, app, it
      * implementation is complex
    * migration strategy
      * roadmap, for getting this done and offers various benefits to organizations
    * Considerations in cloud migration
      * ASSESSING CLOUD READINESS 
        • What do the applications run on?
        • Are there any dependencies on hardware or middleware?
        • What will it take to move the applications and data to the cloud?
        • What are the necessary time commitments?
      * cant move to cloud
        * keys 
        * high level of performance
        * licensing limit
        * services not tested
        * programs actual hardware running
        * higher level of sec systems
  * migration
    * minimize impact on end user
    * reducing risk
    * Gather 7r
      * retain
      * rehost
      * replatform 
      * refactor
      * rearch
      * rebuild
      * replace
    * process
      * set objective
      * create a sec strategy
      * copy data 
      * move business intelligence
      * shift production to cloud
  * operation
    * cloud best practice
      * ensure transparency
      * automate security
      * implement redundancy
      * improve continuously
* Public cloud playforms overview
  * aws
    * good
      * dominant
      * extensive
      * large org
      * global
      * flexibility
      * recommended for all cases
    * bad
      * advanced tech
      * overwhelming
    * first oned
    * iaas and paas services
    * elastic beanstalk
    * elastic block store
    * glacier storage
    * relational database service
    * dynamodb nosql
    * amazon simple storage service and amazon elastic compute cloud, s3, ec2
    * s3
      * developer version of dropbox
      * automatically scale
    * ec2
      * teams can rent machine 
    * aws lambda
      * event driven, serverless
      * cost less ec2
      * not more suitable longer than few mins
      * 
  * gcp
    * good
      * cloud native businese
      * commitment to open source
      * flexible
      * devops
      * container based
      * most cost efficient
    * bad
      * limited
      * contract 
    * simple to use
    * iaas and paas
    * compute engine, app engine, container engine, cloud storage, bigquery
    * 
  * ms
    * good
      * second largest
      * integration 
      * broad feature
      * hybrid cloud
      * support  for open source
      * ideal for startups
    * bad
      * historical issues
      * advanced tech
    * iass and paas
    * several saas 
      * office 365
    * azure cosmos db
      * nosql
  * Popular cloud services
    * sql databases
      * amazon aurora
      * azure sql database
      * google cloud sql
    * storage
      * amazon s3
      * azure blob storage
      * google cloud storage
    * migration
      * amazon ec2
      * azure virtual machine
      * google compute engine
* Key Takeaways
  * iaas
    * vendor maanges hardware and virtualization, leaving rest up to u
  * paas
    * config, function, scale, but vendor operates
  * saas
    * subscription, only manage configuration
  * Decide whether the cloud is a financially suitable option by calculating the total cost of ownership.
  * Assess their organization's cloud readiness.
  * Build a cloud migration strategy.  
  * Go through with migration.  
  * Set up resources so that the cloud is operated.

## EPAM Cloud Caps and Services
Epam cloud cap and services
  * cloud services
    * modernization
      * multi cloud  (cloud center of excellence (CCoE), strategy, design, migration) 
    * engineering
      * serverless applications
      * data, ml, in cloud
      * saas cloud platforms
    * dev.test
      * devops transformations
      * software lifecycle sdlc
      * cybersec
      * test auto
      * desvelopment, testing, security, operations
    * operations
      * cloud app and infrastructure management
      * aiops AIOps (AI for IT operations)
      * itsm ITSM (IT service management) automation
      * building effective and automated hybrid cloud; 
      * cloud cost control and optimization;  ensuring self-service capabilities; 
      * technical debt reduction; and
      * automated, efficient, and reliable cloud operations.
      * results
        * cost optimization autmating, build a strong cloud community
    * Cloud-Native Transformation
      * help create business value with cloud services
      * entire cloud lifecycle
      * unrivaled partner ecosystem
      * future of it is in the cloud
      * complexity of modern clouds
    * Cloud Advisory Services
      * strategy & analysis, design & plan, and implementation
Cloud Tools
  * prism
    * customizable assessments of appm arch, data, it
  * migvisor
    * gcp based cloud database migration advisor and automated db
    * gcp, azure, aws
  * maestro
    * production proves platform for cloud orchestration
    * self provisioning
    * infrastructure as code
    * auto configuration
    * security inspection
  * EPAM deliv platform
    * software engineering, arch, and dev
    * production proven, open source,
    * deployment ready,
    * best practive ci cd
    * advanced sec model sso 
    * one click env
    * devops to devs ratio
  * epam datalab
    * self service env for collaborative data science work
    * a provisioning interface that ensures secure access to a personal exploratory environment
    * a data scientist interface that gives single-click access to analytical tools and computational resources
    * a collaboration interface that provides a shared codebase, storage, wiki; multiple Git repositories support
    * a billing interface that helps manage detailed billing reports and the cloud data services limit
Epam Partnerships
  * aws
  * google
  * azure 
  * become a certified professional yourself or assure your clients that EPAM helps
    * its customers assess, design, develop, migrate, and
    * manage their AWS/GCP/Azure deployments to reduce complexity and maximize value.
Epam Target
  * cloud maturity
  * cloud native 
    * business via tech
    * customer brought these skills in house
  * cloud optimized
    * enjoying cloud caps 
    * customer is running in scale and maybe looking to go cloud native
  * cloud growth
    * deliver agile aps in cloud
    * runs in cloud at scale and has room
  * cloud initiate
    * mature, enterprise ready
    * gaining on moving to cloud
  * cloud curious/ advisory
    * organizational alignment for transformation
    * customer gains alighment potential fir, great 
  * Executive Team	Strategic alignment, cost optimization, risk mitigation, business agility, accelerating innovation, efficiency, quality of service
  * Infrastructure Team	Cloud governance, clarity on roles and responsibilities, upskilling, minimizing the impact of changes in organizational structure, best practice cloud tooling, software automation
  * Operations	Operational readiness, operational strategy, operational efficiency, best practice cloud tooling, software automation, improving resilience and recovery
  * Finance Team	Financial governance and automation, optimizing billing process and reporting, changes in budget planning
  * Product / Data / App Dev / Software Team	Time to market, clarity on roles and responsibilities, upskilling, minimizing the impact of changes in organizational structure, agile development process, DevOps framework
  * Compliance and Legal Team	Risk mitigation, security and cloud governance framework
  * Security Team	Risk mitigation, security and cloud governance framework, best-practice cloud tooling, software automation
  * Enterprise Architecture Team	Cloud governance, cloud reference architecture, business architecture 
  * Marketing and Communications	Organizational changes, communications approach / channels, changes to value proposition, USP creation

* Epam Cloud Elevator Pitch
  * pain points
    * multiple integration platforms within the enterprise, with increased TCO (total cost of ownership)
    * portfolio-specific implementation of integrations
    * lack of real-time/event-based integrations
    * lack of agility in delivering services to market
    * point-to-point integrations
    * manual and grey IT workarounds
    * data ownership and quality issues
    * tactical focus limiting platform scalability to future needs
    * performance issues and missing transactions
    * management and maintenance overheads
  * gaps
    * saas
    * mobile 
    * real time integrations
  * opportunities
    * Simplify and consolidate the integration landscape.
    * Reduce TCO as a result of consolidation.
    * Standardize the implementation of integrations across the enterprise. 
    * Develop real-time/event-based integrations.
    * Adopt a configuration-based approach to implementing integrations.
    * Loosely couple the integrations to minimize impact from future changes.
    * Automate data migration and integration.
    * Build an enterprise grade integration platform that scales to future needs.
    * Reduce maintenance and support overhead through consolidation.
  * plan
    * portfolio 
    * migvisor 
    * prism
  * building
    * epam
    * cloud data
    * data lab , odahu
  * managing
    * maestro
    * syndicate
    * cloud native pipeline landing zone

* Key Takeaways
  * cloud modernization; 
  * cloud engineering; 
  * cloud operations; 
  * DevTestSecOps
 
## Cloud-x Associate AWS Developer(Self Paced)
* Check List 
  * AWS Essential Setup
  * On Premise to AWS
  * IaaS Compute
  * IaaS Storage
  * IaaS Networking
  * Databases As a Service (DBaaS)
  * Platform As a Service (PaaS)
  * Software As a Service (SaaS)
  * DevOps with AWS
  * Security on AWS
  * On Promise
    * you have most, responsiblity, to keep server up
  * Servers
    * elastic compute cloud
      * ec2
      * auto scaling
    * simple storage service
      * s3
      * for backup
      * dropbox in before
    * amazon manages physical
    * u virtual
      * this is shared responsilibity model
    * os update
    * backups
    * firewalls
    * maintenance schedules
  * secs
    * windows server sec
    * linux sec
    * owasp
  * two place zone at least
  * north
    * us easat 1
    * us easat 2
    * us easat 3
  * finance models, ml
  * high usage, conoute optimized
  * ECS
    * elastic container service
    * simple 
    * less popular
    * basic
  * elastic kubernetes service
    * kubetnetes runs anywhere
    * very popular
    * advanced networking
  * from small to high
  * list 
    * ecs and fargate
    * ecs with ec2 instances
    * eks with ec2 instances
    * on premisses with eks anywhere
  * functions as a service
    * a small chunk of code that runs on your cloud playform every time an event occurs
    * use lambda
    * serverles arch
      * app responds to incoming events without need for always on server that you manage
  * Saas
  * Continuous Integration CI
    * smaller changes to code are automatically tested whenever a change is made
  * Continuous Deployment CD
    * tested changes are automatically deployed to a staging environment and can then be automatically sent into production
  * terminate ec2 instances
  * release elastic ip
  * delete application load balancer
  * delete ebs volumes
  * delete s3 buckets and cloud front distributions
  * pillars of the well arch framework
    * op excellence
      * infrastructure as code
      * many small changes
      * design for failure
      * learn from failure
      * quickly make changes to operational procedures
    * security
      * use id management
      * use traceability
      * apply sec everywhere
      * automate sec
      * sec data as rest 
      * limit exposure of sensitive
      * practive for sec 
    * reliability
      * auto recover from failure
      * rest rec
      * stop guessing cap
      * scale horizontally
      * implement elasticity
      * automate change
    * performance efficiency
      * have mech 
      * use managed services
      * use serverless arch
      * decouple components instead of monoliths
      * think parallel
      * run experiments
      * go global in min
    * cost optimization 
      * save on it cap and use economies of scale
      * have a budget
      * pas as you go
      * mesaure usage for right sizing
      * tag expenditures across teams
    * sustainability
      * max efficiency
      * use managed services
      * know your environmental impact 
      * set goals to reduce waste
  * 

