# CreateSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save** | **bool** | Indicates whether or not you want to save this search request for future use. The options are:  * &#x60;true&#x60; * &#x60;false&#x60; (default value)  If set to &#x60;true&#x60;, this field returns &#x60;searchID&#x60; in the response. You can use this value to retrieve the details of the saved search.  | [optional] 
**name** | **str** | Name of this search. When &#x60;save&#x60; is set to &#x60;true&#x60;, this search is saved with this name.  | [optional] 
**timezone** | **str** | Merchant’s time zone in ISO standard, using the TZ database format. For example: &#x60;America/Chicago&#x60;  | [optional] 
**query** | **str** | String that contains the filters and variables for which you want to search. For information about supported field-filters and operators, see the [Query Filters]( https://developer.cybersource.com/api/developer-guides/dita-txn-search-details-rest-api-dev-guide-102718/txn-search-intro/txn-filtering.html) section of the Transaction Search Developer Guide.  | [optional] 
**offset** | **int** | Controls the starting point within the collection of results, which defaults to 0. The first item in the collection is retrieved by setting a zero offset.  For example, if you have a collection of 15 items to be retrieved from a resource and you specify limit&#x3D;5, you can retrieve the entire set of results in 3 successive requests by varying the offset value like this:  &#x60;offset&#x3D;0&#x60; &#x60;offset&#x3D;5&#x60; &#x60;offset&#x3D;10&#x60;  **Note:** If an offset larger than the number of results is provided, this will result in no embedded object being returned.  | [optional] 
**limit** | **int** | Controls the maximum number of items that may be returned for a single request. The default is 20, the maximum is 2000.  | [optional] 
**sort** | **str** | A comma separated list of the following form:  &#x60;submitTimeUtc:desc&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


