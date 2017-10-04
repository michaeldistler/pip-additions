import pip


def install_unsupported(unsupported_req):
    if install_unsupported:
        installation_results = []
        for req in unsupported_req:
            try:
                pip.main(['install', req])
                result = {req: True}
            except Exception as e:
                result = {req: False}
            installation_results.append(result)
        return installation_results
