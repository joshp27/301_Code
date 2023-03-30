# # Script: Ops 301 Class 13 Code Challenge
# # Joshua Phipps
# # 3/29/2023
# # Purpose:  Powershell AD Automation

Import-Module ActiveDirectory

New-ADUser -Name "Fran Ferdinand" -Title "TSP Reporting Lead" -EmailAddress "ferdi@GlobeXpower.com" -Department "TSP" -City "Springfield" -State "OR"
