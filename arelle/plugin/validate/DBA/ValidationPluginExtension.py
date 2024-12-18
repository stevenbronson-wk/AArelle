"""
See COPYRIGHT.md for copyright information.
"""
from __future__ import annotations

from arelle.ModelValue import qname
from arelle.ValidateXbrl import ValidateXbrl
from arelle.typing import TypeGetText
from arelle.utils.validate.ValidationPlugin import ValidationPlugin
from .PluginValidationDataExtension import PluginValidationDataExtension

_: TypeGetText

DANISH_CURRENCY_ID = 'DKK'
NAMESPACE_ARR = 'http://xbrl.dcca.dk/arr'
NAMESPACE_CMN = 'http://xbrl.dcca.dk/cmn'
NAMESPACE_FSA = 'http://xbrl.dcca.dk/fsa'
NAMESPACE_GSD = 'http://xbrl.dcca.dk/gsd'
NAMESPACE_SOB = 'http://xbrl.dcca.dk/sob'
PERSONNEL_EXPENSE_THRESHOLD = 200000
ROUNDING_MARGIN = 1000


class ValidationPluginExtension(ValidationPlugin):
    def newPluginData(self, validateXbrl: ValidateXbrl) -> PluginValidationDataExtension:
        return PluginValidationDataExtension(
            self.name,
            annualReportTypes=frozenset([
                'Årsrapport',
                'årsrapport',
                'Annual report'
            ]),

            assetsQn=qname(f'{{{NAMESPACE_FSA}}}Assets'),
            auditedAssuranceReportsDanish='Andre erklæringer med sikkerhed',
            auditedAssuranceReportsEnglish='The independent auditor\'s reports (Other assurance Reports)',
            auditedExtendedReviewDanish='Erklæring om udvidet gennemgang',
            auditedExtendedReviewEnglish='Auditor\'s report on extended review',
            auditedFinancialStatementsDanish='Revisionspåtegning',
            auditedFinancialStatementsEnglish='Auditor\'s report on audited financial statements',
            auditedNonAssuranceReportsDanish='Andre erklæringer uden sikkerhed',
            auditedNonAssuranceReportsEnglish='Auditor\'s reports (Other non-assurance reports)',
            averageNumberOfEmployeesQn=qname(f'{{{NAMESPACE_FSA}}}AverageNumberOfEmployees'),
            balanceSheetQnLessThanOrEqualToAssets=frozenset([
                qname(f'{{{NAMESPACE_FSA}}}NoncurrentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}IntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}CompletedDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}ConcessionsOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}PatentsOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}TrademarksOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}OtherSimilarRightsOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredConcessions'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredPatents'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredLicences'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredTrademarks'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredOtherSimilarRights'),
                qname(f'{{{NAMESPACE_FSA}}}Goodwill'),
                qname(f'{{{NAMESPACE_FSA}}}DevelopmentProjectsInProgressAndPrepaymentsForIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DevelopmentProjectsInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}PrepaymentsForIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}LandAndBuildings'),
                qname(f'{{{NAMESPACE_FSA}}}Land'),
                qname(f'{{{NAMESPACE_FSA}}}Buildings'),
                qname(f'{{{NAMESPACE_FSA}}}InvestmentProperty'),
                qname(f'{{{NAMESPACE_FSA}}}OtherInvestmentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}PlantAndMachinery'),
                qname(f'{{{NAMESPACE_FSA}}}FixturesFittingsToolsAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}BiologicalAssets'),
                qname(f'{{{NAMESPACE_FSA}}}LeaseholdImprovements'),
                qname(f'{{{NAMESPACE_FSA}}}Ships'),
                qname(f'{{{NAMESPACE_FSA}}}Planes'),
                qname(f'{{{NAMESPACE_FSA}}}RightofuseAssets'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyPlantAndEquipmentInProgressAndPrepaymentsForPropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyPlantAndEquipmentInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}PrepaymentsForPropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsAndReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsInGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsInAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsInJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}OtherLongtermInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}OtherLongtermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromOwnersAndManagement'),
                qname(f'{{{NAMESPACE_FSA}}}NoncurrentDeferredTaxAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DepositsLongtermInvestmentsAndReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}CostExceedsIncomeForTheFinancialYearLongtermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ContributedCapitalInArrearsLongTerm'),
                qname(f'{{{NAMESPACE_FSA}}}NoncurrentContractAssets'),
                qname(f'{{{NAMESPACE_FSA}}}CurrentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}Inventories'),
                qname(f'{{{NAMESPACE_FSA}}}RawMaterialsAndConsumables'),
                qname(f'{{{NAMESPACE_FSA}}}WorkInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}ManufacturedGoodsAndGoodsForResale'),
                qname(f'{{{NAMESPACE_FSA}}}PrepaymentsForGoods'),
                qname(f'{{{NAMESPACE_FSA}}}Livestock'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyHeldForSaleInTheOrdinaryCourseOfBusiness'),
                qname(f'{{{NAMESPACE_FSA}}}AssetsHeldForSaleInventories'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermTradeReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ContractWorkInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}CurrentDeferredTaxAssets'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermTaxReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermTaxReceivablesFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}VatAndDutiesReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}OtherShorttermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ContributedCapitalInArrears'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromOwnersAndManagement'),
                qname(f'{{{NAMESPACE_FSA}}}DeferredIncomeAssets'),
                qname(f'{{{NAMESPACE_FSA}}}CostExceedsIncomeForTheFinancialYearShorttermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}TimingDifferencesShorttermReceivablesEspeciallyUtilities'),
                qname(f'{{{NAMESPACE_FSA}}}CurrentContractAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DerivativeFinancialInstrumentsShorttermAssets'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermInvestmentsInGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}OtherShorttermInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}CashAndCashEquivalents'),
                qname(f'{{{NAMESPACE_FSA}}}AssetsMeantForSale'),
            ]),
            classOfReportingEntityQn=qname(f'{{{NAMESPACE_FSA}}}ClassOfReportingEntity'),
            consolidatedMemberQn=qname(f'{{{NAMESPACE_CMN}}}ConsolidatedMember'),
            consolidatedSoloDimensionQn=qname(f'{{{NAMESPACE_CMN}}}ConsolidatedSoloDimension'),
            dateOfApprovalOfAnnualReportQn=qname(f'{{{NAMESPACE_SOB}}}DateOfApprovalOfAnnualReport'),
            dateOfExtraordinaryDividendDistributedAfterEndOfReportingPeriod=qname(f'{{{NAMESPACE_FSA}}}DateOfExtraordinaryDividendDistributedAfterEndOfReportingPeriod'),
            dateOfGeneralMeetingQn=qname(f'{{{NAMESPACE_GSD}}}DateOfGeneralMeeting'),
            descriptionOfQualificationsOfAssuranceEngagementPerformedQn=qname(f'{{{NAMESPACE_ARR}}}DescriptionOfQualificationsOfAssuranceEngagementPerformed'),
            distributionOfResultsQns=frozenset([
                qname(f'{{{NAMESPACE_FSA}}}DistributionsResultDistribution'),
                qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryDistributions'),
                qname(f'{{{NAMESPACE_FSA}}}ProposedDividendRecognisedInEquity'),
                qname(f'{{{NAMESPACE_FSA}}}ProposedExtraordinaryDividendRecognisedInEquity'),
                qname(f'{{{NAMESPACE_FSA}}}ProposedExtraordinaryDividendRecognisedInLiabilities'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredFromToHedgeFund'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredFromToReserveFund'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredFromToReservesAvailable'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromEquityAttributableToParent'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromMinorityInterests'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromOtherStatutoryReserves'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromReserveAccordingToArticlesOfAssociation'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromReserveForNetRevaluationAccordingToEquityMethod'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromReserveForNetRevaluationOfInvestmentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromRestOfOtherReserves'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromRetainedEarnings'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForCurrentValueAdjustmentsOfCurrencyGains'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForCurrentValueOfHedging'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForDevelopmentExpenditure'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForEntrepreneurialCompany'),
            ]),
            employeeBenefitsExpenseQn=qname(f'{{{NAMESPACE_FSA}}}EmployeeBenefitsExpense'),
            equityQn=qname(f'{{{NAMESPACE_FSA}}}Equity'),
            extraordinaryCostsQn=qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryCosts'),
            extraordinaryIncomeQn=qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryIncome'),
            extraordinaryResultBeforeTaxQn=qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryResultBeforeTax'),
            fr37RestrictedText='has not given rise to reservations',
            identificationNumberCvrOfAuditFirmQn=qname(f'{{{NAMESPACE_CMN}}}IdentificationNumberCvrOfAuditFirm'),
            independentAuditorsReportDanish='Den uafhængige revisors erklæringer (review)',
            independentAuditorsReportEnglish='The independent auditor\'s reports (Review)',
            informationOnTypeOfSubmittedReportQn=qname(f'{{{NAMESPACE_GSD}}}InformationOnTypeOfSubmittedReport'),
            liabilitiesQn=qname(f'{{{NAMESPACE_FSA}}}LiabilitiesAndEquity'),
            liabilitiesAndEquityQn=qname(f'{{{NAMESPACE_FSA}}}LiabilitiesAndEquity'),
            liabilitiesOtherThanProvisionsQn=qname(f'{{{NAMESPACE_FSA}}}LiabilitiesOtherThanProvisions'),
            longtermLiabilitiesOtherThanProvisionsQn=qname(f'{{{NAMESPACE_FSA}}}LongtermLiabilitiesOtherThanProvisions'),
            noncurrentAssetsQn=qname(f'{{{NAMESPACE_FSA}}}NoncurrentAssets'),
            nameAndSurnameOfChairmanOfGeneralMeetingQn=qname(f'{{{NAMESPACE_GSD}}}NameAndSurnameOfChairmanOfGeneralMeeting'),
            nameOfAuditFirmQn=qname(f'{{{NAMESPACE_CMN}}}NameOfAuditFirm'),
            positiveProfitThreshold=1000,
            precedingReportingPeriodEndDateQn=qname(f'{{{NAMESPACE_GSD}}}PredingReportingPeriodEndDate'),  # Typo in taxonomy
            precedingReportingPeriodStartDateQn=qname(f'{{{NAMESPACE_GSD}}}PrecedingReportingPeriodStartDate'),
            profitLossQn=qname(f'{{{NAMESPACE_FSA}}}ProfitLoss'),
            proposedDividendRecognisedInEquityQn=qname(f'{{{NAMESPACE_FSA}}}ProposedDividendRecognisedInEquity'),
            provisionsQn=qname(f'{{{NAMESPACE_FSA}}}Provisions'),
            reportingPeriodEndDateQn=qname(f'{{{NAMESPACE_GSD}}}ReportingPeriodEndDate'),
            reportingPeriodStartDateQn=qname(f'{{{NAMESPACE_GSD}}}ReportingPeriodStartDate'),
            shorttermLiabilitiesOtherThanProvisionsQn=qname(f'{{{NAMESPACE_FSA}}}ShorttermLiabilitiesOtherThanProvisions'),
            signatureOfAuditorsDateQn=qname(f'{{{NAMESPACE_ARR}}}SignatureOfAuditorsDate'),
            taxExpenseOnOrdinaryActivitiesQn=qname(f'{{{NAMESPACE_FSA}}}TaxExpenseOnOrdinaryActivities'),
            taxExpenseQn=qname(f'{{{NAMESPACE_FSA}}}TaxExpense'),
            typeOfAuditorAssistanceQn=qname(f'{{{NAMESPACE_CMN}}}TypeOfAuditorAssistance'),
            typeOfReportingPeriodDimensionQn=qname(f'{{{NAMESPACE_GSD}}}TypeOfReportingPeriodDimension'),
            wagesAndSalariesQn=qname(f'{{{NAMESPACE_FSA}}}WagesAndSalaries'),
        )
