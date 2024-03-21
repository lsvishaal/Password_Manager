# T1 - Developer Environment Setup

## T1.1 Git Setup

We will be using SourceTree as the primary git client. We have to generate a PAT (Personal Access Token) on GitHub, and register it in SourceTree - to allow SourceTree application to make changes directly to GitHub.

If you already know how to do it, skip this section.

Note: This is not required if you use GitHub desktop app.

1. Install [SourceTree](https://www.sourcetreeapp.com/)

2. Goto `GitHub` > `Settings` > `Developer Settings` > `Personal access tokens` and select `Generate new token`. (classic token does the job for now)

3. Set the token's `Note` as **SourceTree-Win** so you can identify it in the future. Set expiration to `90 days` Check all options (give all permissions).

4. Finally click `Generate token` button, and DO NOT CLOSE THE PAGE. COPY THE TOKEN - because you need to set it up in SourceTree.

5. Launch SourceTree. Goto `Tools` > `Options` > `Authentication` > `Add`

6. Configuration:<br>Hosting Service: GitHub<br>Preferred Protocol: HTTPS<br>Authentication: Basic<br>Username: `<Your Github Username>`<br><br>and click `Refresh App Password`. You will be asked to enter username, and the PAT (Personal Access Token) that you generated and (hopefully) copied as the password.

7. Click `Okay` and you should be done.

## T1.2 Project Setup

1. Open SourceTree, and click `Clone`.

2. From the GitHub repository, copy the `HTTPS` Clone url. (Green Button, and HTTPS tab)

3. Paste-this under `Source Path / URL` in SourceTree. Complete on screen requirements to complete cloning.

4. Open the repository in VS Code. (Browse to local folder, `Shift + RMB` > `Open with Code`)

5. Your github repository needs to have the following structure.

    ```
    root
    |
    +-- src/
        +-- __init__.py
    +-- tests/
        +-- __init__.py
    +-- LICENSE.md
    +-- README.md
    ```

    All source code stays inside the `src` folder. We will create sub-folders / modules as and when necessary for the project.

6. Create your first (or second) commit with this structure on the `main` branch.
