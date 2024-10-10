<p align="center">
  <a href="http://lovera.maxam.now.sh/">
    <!-- <img src="https://user-images.githubusercontent.com/25841814/79395484-5081ae80-7fac-11ea-9e27-ac91472e31dd.png" alt="screenshot" width="500"> -->
  </a>
  <h3 align="center">✨solved-box</h3>
</p>

<p align="center">
   <img src="https://img.shields.io/badge/language-python-blue?style"/>
   <img src="https://img.shields.io/github/license/BieNew22/Solved-Box"/>
   <img src="https://img.shields.io/github/stars/BieNew22/Solved-Box"/>
   <img src="https://img.shields.io/github/forks/BieNew22/Solved-Box"/>
</p>
<p align="center">
   <br/>
   Show your Solved.ac profile!!
   <br/>
</p>

---

> This project is inspired by maxam2017's productive-box<br/>
> Find more in https://github.com/maxam2017/productive-box/

## Overview

This project display user solved.ac profile

## Setup1 : Prep work

1. Create a new **public GitHub Gist** and **get Gist ID** (https://gist.github.com/)
    * https://gist.github.com/BieNew22/e8cafc40adadb1b28963cf3bf77e9968
    * `e8cafc40adadb1b28963cf3bf77e9968` is gist id
    * **when you make Gist only fill the content.**
2. Create a token with the `gist` (https://github.com/settings/tokens/new)
<p align="center">
   <img src="https://img.shields.io/badge/language-python-blue?style"/>
</p>


## Setup2 : Project setup

1. Fork this repo
2. Open the "Actions" tab of your fork and click the "enable" button
3. Go to the repo **Settings > Secrets and variables** > **Actions**,
   add the following secrets / variables:
   | Name | Description |
   |--------------------|---------------------------------------------------------------|
   | **GH_TOKEN** | The GitHub token generated above. |
   | **GIST_ID** | The ID portion from your gist URL, e.g., `e8cafc40adadb1b28963cf3bf77e9968`. |
   | **USER_NAME** | The user name of your solved.ac id, e.g., `newbie22`|

   Below is the final screenshot
   <p align="center">
    <img src="https://img.shields.io/badge/language-python-blue?style"/>
   </p>
4. Manually run the workflow for the first time or Update the repository. (The workflow will run every day at 21:00 UTC.)
5. Pin the newly created Gist
