# Ptsv2paymentsidcapturesPaymentInformationCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account_type** | **str** | Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process.  This field is required in the following cases:   - Debit transactions on Cielo and Comercio Latino.   - Transactions with Brazilian-issued cards on CyberSource through VisaNet.   - Applicable only for CyberSource through VisaNet (CtV).  **Note** Combo cards in Brazil contain credit and debit functionality in a single card. Visa systems use a credit bank identification number (BIN) for this type of card. Using the BIN to determine whether a card is debit or credit can cause transactions with these cards to be processed incorrectly. CyberSource strongly recommends that you include this field for combo card transactions.  Possible values include the following.   - &#x60;CHECKING&#x60;: Checking account  - &#x60;CREDIT&#x60;: Credit card account  - &#x60;SAVING&#x60;: Saving account  - &#x60;LINE_OF_CREDIT&#x60;: Line of credit or credit portion of combo card  - &#x60;PREPAID&#x60;: Prepaid card account or prepaid portion of combo card  - &#x60;UNIVERSAL&#x60;: Universal account  | [optional] 
**source_account_type_details** | **str** | Type of account that is being used when the value for the override_payment_method field is line of credit (LI) or prepaid card (PP). Possible values for line of credit: - &#x60;AGRC&#x60;: Visa Agro Custeio - &#x60;AGRE&#x60;: Visa Agro Electron - &#x60;AGRI&#x60;: Visa Agro Investimento - &#x60;AGRO&#x60;: Visa Agro Possible values for prepaid card: - &#x60;VVA&#x60;: Visa Vale Alimentacao - &#x60;VVF&#x60;: Visa Vale Flex - &#x60;VVR&#x60;: Visa Vale Refeicao This field is supported only for combo card transactions in Brazil on CyberSource through VisaNet.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


