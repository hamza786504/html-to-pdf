import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

filePath= "loan-estimate-fixed-rate-loan-sample"
filePath= "additional-information"
# filePath= "closing-cost-details"

with open(f"htmlFiles/{filePath}.html", 'r') as f:
    document_content = f.read()

try:
    response = doc_api.create_doc({
        'test': True,  # test documents are free but watermarked
        'document_type': 'pdf',
        # "name": "docraptor.pdf",                                 # help you find a document later
        'document_content': document_content,
        # 'document_url': 'https://docraptor.com/examples/invoice.html',
        # 'javascript': True,
        'prince_options': {
           'media': 'print', # @media 'screen' or 'print' CSS
        #    'baseurl': 'https://yoursite.com', # the base URL for any relative URLs
        },
    })

    # create_doc() returns a binary string
    with open(f"pdfFiles/{filePath}.pdf", 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print(f'Successfully created {filePath}!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)