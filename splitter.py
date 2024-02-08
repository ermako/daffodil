
rawstrings = [
    "5d576b-8884ff-d7bce8-e8cee4-fde2ff",
    "454545-6d5959-9dcbba-abebd2-04f06a",
    "ed6a5a-f4f1bb-9bc1bc-5ca4a9-e6ebe0",
    "87f1ff-c0f5fa-bd8b9c-af125a-582b11",
    "564787-dbcbd8-f2fdff-9ad4d6-101935",
    "1f2041-4b3f72-ffc857-119da4-19647e",
    "420039-932f6d-e07be0-dcccff-f6f2ff",
    "fb8b24-d90368-820263-291720-04a777",
    "558b6e-88a09e-704c5e-b88c9e-f1c8db",
    "edeec9-dde7c7-bfd8bd-98c9a3-77bfa3",
    "52d1dc-475b5a-8d8e8e-a3a9aa-bbbbbf",
    "000000-3d2645-832161-da4167-f0eff4",
    "d7dae5-b9cdda-a6d8d4-8eaf9d-6b7d7d",
    "212922-294936-3e6259-5b8266-aef6c7",
    "a80874-b7fdfe-5ef38c-2b9720-343a1a",
    "795c5f-a69658-d9b26f-fadf7f-f2e29f",
    "0d3b66-faf0ca-f4d35e-ee964b-f95738",
    "f1e8b8-f9e784-e58f65-d05353-191919",
    "d4f2db-cef7a0-ba9790-914d76-69353f",
    "555b6e-89b0ae-bee3db-faf9f9-ffd6ba",
    "ff1053-6c6ea0-66c7f4-c1cad6-ffffff",
    "ffa69e-ff7e6b-8c5e58-a9f0d1-fff7f8",
    "436436-d6f599-d2ff28-c84c09-420217",
    "4281a4-48a9a6-e4dfda-d4b483-c1666b",
    "334139-1e2d24-c52184-e574bc-f9b4ed",
    "fa8334-fffd77-ffe882-388697-271033",
    "a9ddd6-7a8b99-91adc2-9ba0bc-c1b8c8",
    "b80c09-0b4f6c-01baef-fbfbff-040f16",
    "12100e-30321c-4a4b2f-6b654b-d4df9e",
    "e2cfea-a06cd5-6247aa-102b3f-062726",
    "fe5d26-f2c078-faedca-c1dbb3-7ebc89",
    "f9f8f8-cdd3ce-bbb5bd-aa6da3-b118c8",
    "330c2f-7b287d-7067cf-b7c0ee-cbf3d2",
    "713e5a-63a375-edc79b-d57a66-ca6680",
    "272838-f3de8a-eb9486-7e7f9a-f9f8f8",
    "6dd3ce-c8e9a0-f7a278-a13d63-351e29",
    "4b4237-d5a021-ede7d9-a49694-736b60",
]

for string in rawstrings:
    splitlist = string.split("-")
    for i in range(len(splitlist)):
        splitlist[i] = "#" + splitlist[i]
    print(str(splitlist) + ",")
