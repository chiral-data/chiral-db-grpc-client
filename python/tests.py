from chiral_db_grpc_client import client

def test_cases(chiral_db_client: client.Client = client.Client('localhost', '10000')):
    print("-------------- Testing GetDescrition ... --------------")
    desc = chiral_db_client.get_description()
    print(desc)
    print("-------------- Testing GetDescrition Complete... --------------")

    print("-------------- Testing Query Similarity ... --------------", end='\r')
    results = chiral_db_client.query_similarity('ChEMBL', 'Cc1cc(NC(=O)c2cc(Cl)cc(Cl)c2O)ccc1Sc1nc2ccccc2s1', 1.0)
    assert 'CHEMBL263810' in results.keys()
    print("-------------- Testing Query Similarity Pass -------------")


    print("-------------- Testing Query Substructure ... --------------", end='\r')
    results = chiral_db_client.query_substructure('ChEMBL', 'Sc1nc2ccccc2s1')
    assert 'CHEMBL263810' in results.keys()
    assert 'CHEMBL6685' in results.keys()
    print("-------------- Testing Query Substructure Pass -------------")

if __name__ == '__main__':
    print('Tesing local server ...')
    test_cases()

    # print('Tesing remote server ...')
    # test_cases(chiral_db_client=client.Client('demo.chiral.one', '10000'))