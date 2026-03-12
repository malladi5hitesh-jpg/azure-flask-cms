# Azure Flask CMS Deployment – WRITEUP

## Overview
For this project, the Flask-based Article CMS application was deployed to Microsoft Azure. Azure provides multiple deployment options such as Virtual Machines (VMs) and Azure App Service. After comparing these two options, Azure App Service was chosen for deploying the application.

---

## Option 1: Virtual Machine (VM)

A Virtual Machine provides full control over the operating system and environment. With a VM, the developer is responsible for configuring and maintaining everything required to run the application.

### Advantages
- Full control over the operating system and server configuration
- Ability to install any software or dependencies required
- Greater flexibility for complex or customized environments

### Disadvantages
- Requires manual setup of the server, runtime environment, and security
- Higher maintenance responsibility (updates, patches, monitoring)
- Slower deployment compared to managed services
- Requires managing scaling and load balancing manually

---

## Option 2: Azure App Service

Azure App Service is a Platform as a Service (PaaS) offering that allows developers to deploy web applications without managing the underlying infrastructure.

### Advantages
- Fully managed platform by Azure
- Quick and simple deployment
- Built-in scaling, monitoring, and logging
- Easy integration with GitHub for continuous deployment
- Automatic environment configuration for supported languages like Python

### Disadvantages
- Less control over the underlying operating system
- Limited customization compared to a full VM

---

## Reason for Choosing Azure App Service

Azure App Service was chosen for this project because it simplifies the deployment process and reduces the need to manage infrastructure. Since the goal of this project is to deploy a Flask web application and integrate it with Azure services such as Azure SQL Database and Azure Blob Storage, App Service provides a faster and more efficient way to host the application.

Additionally, App Service supports continuous deployment from GitHub, making it easy to update the application whenever code changes are pushed to the repository.

---

## Conclusion

While Virtual Machines provide more flexibility and control, they require significant setup and maintenance effort. Azure App Service offers a managed environment that simplifies deployment and management. For this project, Azure App Service was the better choice because it allows the application to be deployed quickly while still supporting the required Azure integrations.
