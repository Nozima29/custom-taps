STREAMS = {
    "EventAttendee": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Contact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Event": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "RSVP": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Issue": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Issue": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Priority": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Project": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Task": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "InvestorVehicle": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "LegalName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Investor": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "MSAZipCode": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "MSAZipCode": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Sector": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Sector": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Industry": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Page": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Events": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PageType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "WatchList": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Geography": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Industry": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Owner": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "GlobalRegion": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "DocumentFolders": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "FieldFrom": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "FieldTo": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Company": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CompanyType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "EBITDAMM": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ParentCompany": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SectorLevel1": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SubSector": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SubType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Geography": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Geography": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "ServiceRequest": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "AssignedTo": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Investor": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestorContact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "RequestType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "CapitalProvider": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "TypeofCapitalProvider": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "MarketingList": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Campaign": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Contact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "ExecutiveEvaluation": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CommunicationSkills": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "EnergyDrive": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Evaluator": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ExecutiveName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "FitasCEOCEO1st": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "IndustryFocus": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "LeadershipCapability": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PLExperience": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PEandMAExperience": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "QualityofThesis": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SuccessinPriorRoles": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "SPSCity": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "City": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "MSA": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "User": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "UserGroups": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Source": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "FundraisingCommitment": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "ActualCommitment": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ConsultantAdvisor": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Entity": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "FundraisingStatus": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestmentType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Investor": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestorContact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Contact": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Company": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Financial": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "EBITDA": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "EnterpriseValue": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "EquityValue": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "NetDebtValue": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PortfolioCompany": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Revenue": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Investor": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "InvestorName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CoveragePerson": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "FundsUnderManagementUSD": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestorType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PrimaryContact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Region": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Tier": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ZipCode": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "News": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "LPDistributionList": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Company": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Contacts": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "LimitedPartner": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Role": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Vehicles": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "ZipCode": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "ZipCode": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "MSA": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Event": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "EventTitle": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ActivityType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Category": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Companies": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Deals": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Industries": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InternalAttendees": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Region": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SubCategory": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Campaign": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CampaignName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CampaignGroup": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Deal": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Industry": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "MarketTransaction": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Category": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Industry": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "MSA": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "MSA": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Geography": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Region": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "USRegion": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Fee": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "ActualFee": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Deal": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ExpFee": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Provider": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "CapitalCommitment": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CapitalProvider": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CommitmentAmount": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "DealName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestmentType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SecurityType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TypeofCapital": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "MailingList": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "MailingList": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Comment": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Subject": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Issue": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Note": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Subject": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Contacts": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "EnteredBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "FollowUp": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "LoanParticipants": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CommitmentAmount": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Lender": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Loan": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Stage": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Loan": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Amount": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "LoanType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Stage": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Underwriter": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "RealAsset": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "AppraisalValue": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "AssetManager": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "AssetType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Broker": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PreviousOwner": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PurchasePrice": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TitleHeldAt": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "FundCommitment": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Amount": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Entity": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestmentType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Investor": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestorContact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Task": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Title": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "AssignedTo": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Deal": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Department": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Phase": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TaskType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Attachment": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Title": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Project": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "BoardMeeting": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Company": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ProjectManager": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ProjectType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Timeline": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "OfficeLocation": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Company": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "MSA": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "State": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Email": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Subject": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ActivityType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Contacts": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InternalRecipients": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "CampaignGroup": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Industry": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Industry": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "SourceCampaigns": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Owner": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "ContactRelationship": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "RelationshipType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "RelationshipWith": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Term": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Category": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Document": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "MailingCampaign": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CampaignName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TypeofCampaign": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Document": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Title": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Companies": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Funds": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Goal": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Person": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Country": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Country": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "GlobalRegion": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Deal": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "DealName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Category": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Company": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "DealStatus": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestmentAmount": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InvestmentType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PrimaryContact": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "PrimaryIndustry": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Security": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Seniority": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Stage": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TotalSize": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TransactionType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "CapitalCall": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Amount": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fund": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Investor": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Vehicle": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "TimeSheetEntry": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "TeamMember": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Type": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "CompanyAffiliaiton": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "ExecutivePlacement": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Deal": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Executive": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Fee": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Role": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "SearchFirm": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Source": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Fund": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "FundName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CapitalDrawn": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Status": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TargetSize": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "TotalCommitment": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "Institution": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CompanyName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ContactFrequency": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CoveragePerson": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "IndustryPreferences": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "InstitutionType": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "USRegion": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "Name": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    },
    "TransactionTarget": {
        "key_properties": [
            "EntryId"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "CompanyName": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "RelationshipOwner": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "Stage": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "CreatedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "ModifiedBy": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    }
}