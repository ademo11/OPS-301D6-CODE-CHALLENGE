#!/usr/bin/env python3
# Script: OPS 301 Class 03 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 29 Mar 2023
# Purpose: 

Import-Module ActiveDirectory


$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "Franz Ferdinand"
$office = "Springfield"
$state = "OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$description = "TPS Reporting Lead at GlobeX USA"
$username = $firstName.ToString().ToLower() + $lastName.ToString().ToLower()

New-ADUser -Name $displayName -GivenName $firstName -Surname $lastName -EmailAddress $email -Path "OU=TPS Department,OU=Springfield,OU=GlobeX USA,DC=corp,DC=globexpower,DC=com" -AccountPassword (ConvertTo-SecureString -AsPlainText "P@ssw0rd" -Force) -Enabled $true
$username = $firstName.ToLower() + $lastName.ToLower()