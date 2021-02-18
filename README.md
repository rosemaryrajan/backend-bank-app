# nrny-backend

### API Documentation Link
https://immense-sands-37038.herokuapp.com/swagger/
### 1.GET API to fetch a bank details, given branch IFSC code
```shell script
curl -X GET "https://immense-sands-37038.herokuapp.com/api/v1/banks/branch-details/APGB0001109/" -H  "accept: application/json"
```

### 2. GET API to fetch all details of branches, given bank name and a city. This API should also support limit and offset parameters
```shell script
curl -X GET "https://immense-sands-37038.herokuapp.com/api/v1/banks/branch-details/?bank__name=ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED&city=MUMBAI&limit=10&offset=11" -H  "accept: application/json"
```

