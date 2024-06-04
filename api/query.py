
def resolve_contracts(obj, info):
    try:
        contracts = [contract.to_dict() for contract in Contract.query.all()]
        payload = {
            "success": True,
            "todos": contracts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def resolve_users(obj, info):
    try:
        users = [user.to_dict() for user in User.query.all()]
        payload = {
            "success": True,
            "todos": users
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
