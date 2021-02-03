# Project setup

This part of the workshop is to provide basic setup for your project on Cloud Pak for Data as a Service.

1. [Sign up for IBM Cloud Pak for Data as a service](#1-sign-up-for-ibm-cloud-pak-for-data-as-a-service)
1. [Setup a project](#2-project-setup)

## 1. Sign up for IBM Cloud Pak for Data as a service

* Launch a web browser and navigate to [IBM Cloud Pak for Data](https://dataplatform.cloud.ibm.com/registration/stepone?context=cpdaas&apps=all&preselect_region=true)

* You can leave the pre-selected region or select the region nearest to you.

* You can then log in using your IBMid if you have one or create a new IBMid.

  * If you do not have an IBMid, enter your email address and accept the terms checkbox in the `Create a new IBM Cloud Account` section. Then click the `Next` button to complete the process of creating a new account.
  * If you are a returning user, click on the `Log in with your IBMid` link.
    > **Note:** If you are a returning user and you have watson services in a different region than the pre-selected one, you will see an error message telling you to select that region instead. See the [FAQ](../faq/README.md) section for help.

![CPDaaS login](../assets/images/setup/new-signup-page.png)

* The services required for IBM Cloud Pak for Data will be automatically provisioned for you. Once you see a message that says that the apps are ready to use, click on `Go to IBM Cloud Pak for Data`.

![CPDaaS ready](../assets/images/setup/cpdaas-ready.png)

## 2. Project setup

In Cloud Pak for Data, we use the concept of a project to collect / organize the resources used to achieve a particular goal (resources to build a solution to a problem). Your project resources can include data, collaborators, and analytic assets like notebooks and models, etc.

* Once you are on [Cloud Pak for Data as a Service](https://dataplatform.cloud.ibm.com). Click on the (☰) navigation menu on the top left, expand *Projects* and click on the *View all projects* link.

![(☰) Menu -> Projects](../assets/images/setup/menu-projects.png)

* Click on the `New project` button on the top. *Note: If you already have existing projects, your screen will look different from the screenshot below. In that case, click on the `New project +` button on the top right.*

![Start a new project](../assets/images/setup/cpd-new-project.png)

* Click on `Create an empty project`:

![Create empty project](../assets/images/setup/cpd-create-empty-project.png)

* Give the project a name and optional description. You also need to provide an object storage instance for this project. If you have not previously created a Cloud Object Storage instance in your IBM Cloud account, you can create one now by clicking `Add`. *Note: If you do have an existing storage service, select it from the drop down list and click the `Create` button.*

![Project name](../assets/images/setup/cpd-project-name.png)

* A new tab opens up, where you can create the Cloud Object Service. By default, a `Lite` (Free) plan will be selected. Scroll down and update the name of your Cloud Object Storage service if you wish, and click `Create`.

![Create COS instance](../assets/images/setup/create-cos-instance.png)

* The browser tab will automatically close when the Cloud Object Storage instance has been created. Back on IBM Cloud Pak for Data as a Service, click `Refresh`.

![Refresh COS](../assets/images/setup/refresh-cos.png)

* The newly created Cloud Object Storage instance will now be displayed under "Storage". Click `Create` to finish creating the project.

![Create project](../assets/images/setup/create-project.png)

* Once the project is succesfully created you will be brought to the project overview page (*Note:You may be presented with a project tour pop up window, go ahead and close it*)

![Import project success](../assets/images/setup/project-create-success.png)

## Conclusion

At this point we are done with this section. We have completed creating an IBM Cloud account, a Cloud Pak for Data as a Service instance, and the project that we will use in the rest of this workshop.
