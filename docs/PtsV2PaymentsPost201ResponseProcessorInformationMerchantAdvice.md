# PtsV2PaymentsPost201ResponseProcessorInformationMerchantAdvice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Reason the recurring payment transaction was declined. For some processors, this field is used only for Mastercard. For other processors, this field is used for Visa and Mastercard. And for other processors, this field is not implemented.  Possible values:   - &#x60;00&#x60;: Response not provided.  - &#x60;01&#x60;: New account information is available. Obtain the new information.  - &#x60;02&#x60;: Try again later.  - &#x60;03&#x60;: Do not try again. Obtain another type of payment from the customer.  - &#x60;04&#x60;: Problem with a token or a partial shipment indicator.  - &#x60;21&#x60;: Recurring payment cancellation service.  - &#x60;99&#x60;: An unknown value was returned from the processor.  For processor-specific information, see the &#x60;auth_merchant_advice_code&#x60; field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 
**code_raw** | **str** | Raw merchant advice code sent directly from the processor. This field is used only for Mastercard.  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file1: - Record: CP01 TCR7 - Position: 96-99 - Field: Response Data-Merchant Advice Code   For processor-specific information, see the &#x60;auth_merchant_advice_code_raw&#x60; field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 
**name_match** | **str** | #### Visa Platform Connect The field contains will contain the Account Name Request Result for zero amount Authorization request. Valid values are:  00 &#x3D; Name Match Performed 01 &#x3D; Name Match not Performed 02 &#x3D; Name Match not supported  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


