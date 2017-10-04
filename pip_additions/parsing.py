from collections import namedtuple


def parse_requirements(fp):
    with open(fp, 'r') as f:
        unsupported_requirements = []
        requirements = []
        for r in f:
            if r.strip()[:3] == "git":
                unsupported_requirements.append(r.strip())
            else:
                requirements.append(r.strip())
        RequirementResult = namedtuple('RequirementResult', ['ureq', 'req'])
        result = RequirementResult(ureq=unsupported_requirements,
                                   req=requirements)
        return result
