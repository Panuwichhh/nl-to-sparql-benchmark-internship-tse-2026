"""
Evaluation question set for NL to SPARQL over the IDMP / FDA-NDC knowledge graph.
"""

QUESTIONS = [
    {
        "id": 1,
        "cq": 'UC1-CQ1',
        "type": 'SELECT',
        "question": 'Which substances have the active moiety Acetaminophen?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 2,
        "cq": 'UC1-CQ1',
        "type": 'SELECT',
        "question": 'What substances share the common active moiety SERTRALINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "SERTRALINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 3,
        "cq": 'UC1-CQ1',
        "type": 'SELECT',
        "question": 'List all substances whose active moiety is Gabapentin.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Gabapentin" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 4,
        "cq": 'UC1-CQ1',
        "type": 'SELECT',
        "question": 'What substances share the common active moiety CETIRIZINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CETIRIZINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 5,
        "cq": 'UC1-CQ1',
        "type": 'SELECT',
        "question": 'List all substances whose active moiety is Penicillin G.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Penicillin G" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 6,
        "cq": 'UC1-CQ1',
        "type": 'COUNT',
        "question": 'How many substances have the active moiety Acetaminophen?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 7,
        "cq": 'UC1-CQ1',
        "type": 'COUNT',
        "question": 'How many substances have the active moiety SERTRALINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "SERTRALINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 8,
        "cq": 'UC1-CQ1',
        "type": 'COUNT',
        "question": 'How many substances have the active moiety Gabapentin?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Gabapentin" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 9,
        "cq": 'UC1-CQ1',
        "type": 'COUNT',
        "question": 'Count the substances whose active moiety is CETIRIZINE.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CETIRIZINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 10,
        "cq": 'UC1-CQ1',
        "type": 'COUNT',
        "question": 'Count the substances whose active moiety is Penicillin G.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Penicillin G" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 11,
        "cq": 'UC1-CQ2',
        "type": 'SELECT',
        "question": 'What is the active moiety of NAPROXEN?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "NAPROXEN" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 12,
        "cq": 'UC1-CQ2',
        "type": 'SELECT',
        "question": 'Identify the active moiety of Metformin.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metformin" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 13,
        "cq": 'UC1-CQ2',
        "type": 'SELECT',
        "question": 'Which substance is the active moiety of LEVOTHYROXINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "LEVOTHYROXINE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 14,
        "cq": 'UC1-CQ2',
        "type": 'SELECT',
        "question": 'Identify the active moiety of Acetaminophen.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 15,
        "cq": 'UC1-CQ2',
        "type": 'SELECT',
        "question": 'Which substance is the active moiety of CAFFEINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 16,
        "cq": 'UC1-CQ2',
        "type": 'COUNT',
        "question": 'How many active moieties does NAPROXEN have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "NAPROXEN" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 17,
        "cq": 'UC1-CQ2',
        "type": 'COUNT',
        "question": 'How many active moieties does Metformin have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metformin" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 18,
        "cq": 'UC1-CQ2',
        "type": 'COUNT',
        "question": 'How many active moieties does LEVOTHYROXINE have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "LEVOTHYROXINE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 19,
        "cq": 'UC1-CQ2',
        "type": 'COUNT',
        "question": 'Count the active moieties of Acetaminophen.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 20,
        "cq": 'UC1-CQ2',
        "type": 'COUNT',
        "question": 'Count the active moieties of CAFFEINE.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }

""",
    },
    {
        "id": 21,
        "cq": 'UC1-CQ3',
        "type": 'SELECT',
        "question": 'Which products contain substances with the active moiety TRAMADOL?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "TRAMADOL" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }

""",
    },
    {
        "id": 22,
        "cq": 'UC1-CQ3',
        "type": 'SELECT',
        "question": 'What products include a substance with common active moiety CAFFEINE?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }

""",
    },
    {
        "id": 23,
        "cq": 'UC1-CQ3',
        "type": 'SELECT',
        "question": 'List the medicinal products whose active ingredient shares the active moiety WARFARIN.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "WARFARIN" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }

""",
    },
    {
        "id": 24,
        "cq": 'UC1-CQ3',
        "type": 'SELECT',
        "question": 'What products include a substance with common active moiety Diclofenac?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }

""",
    },
    {
        "id": 25,
        "cq": 'UC1-CQ3',
        "type": 'SELECT',
        "question": 'List the medicinal products whose active ingredient shares the active moiety Acetaminophen.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }

""",
    },
    {
        "id": 26,
        "cq": 'UC1-CQ3',
        "type": 'COUNT',
        "question": 'How many products contain substances with the active moiety TRAMADOL?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "TRAMADOL" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 27,
        "cq": 'UC1-CQ3',
        "type": 'COUNT',
        "question": 'How many products contain substances with the active moiety CAFFEINE?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 28,
        "cq": 'UC1-CQ3',
        "type": 'COUNT',
        "question": 'How many products contain substances with the active moiety WARFARIN?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "WARFARIN" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 29,
        "cq": 'UC1-CQ3',
        "type": 'COUNT',
        "question": 'Count the products whose active ingredient has active moiety Diclofenac.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 30,
        "cq": 'UC1-CQ3',
        "type": 'COUNT',
        "question": 'Count the products whose active ingredient has active moiety Acetaminophen.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 31,
        "cq": 'UC1-CQ3',
        "type": 'LIMIT',
        "question": 'Give 5 products that contain substances with active moiety TRAMADOL.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "TRAMADOL" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5

""",
    },
    {
        "id": 32,
        "cq": 'UC1-CQ3',
        "type": 'LIMIT',
        "question": 'Give 5 products that contain substances with active moiety CAFFEINE.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5

""",
    },
    {
        "id": 33,
        "cq": 'UC1-CQ3',
        "type": 'LIMIT',
        "question": 'Give 5 products that contain substances with active moiety WARFARIN.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "WARFARIN" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5

""",
    },
    {
        "id": 34,
        "cq": 'UC1-CQ3',
        "type": 'LIMIT',
        "question": 'Show any five medicinal products with active moiety Diclofenac.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5

""",
    },
    {
        "id": 35,
        "cq": 'UC1-CQ3',
        "type": 'LIMIT',
        "question": 'Show any five medicinal products with active moiety Acetaminophen.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Acetaminophen" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5

""",
    },
    {
        "id": 36,
        "cq": 'UC1-CQ4',
        "type": 'SELECT',
        "question": 'What is the EV code of CAFFEINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 37,
        "cq": 'UC1-CQ4',
        "type": 'SELECT',
        "question": 'Give the EV code for the substance Morphine.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 38,
        "cq": 'UC1-CQ4',
        "type": 'SELECT',
        "question": 'Which EudraVigilance (SMS) code does Metoprolol have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metoprolol" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 39,
        "cq": 'UC1-CQ4',
        "type": 'SELECT',
        "question": 'Give the EV code for the substance Prednisone.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Prednisone" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 40,
        "cq": 'UC1-CQ4',
        "type": 'SELECT',
        "question": 'Which EudraVigilance (SMS) code does Codeine have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Codeine" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 41,
        "cq": 'UC1-CQ4',
        "type": 'ASK',
        "question": 'Does CAFFEINE have an EV code?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }

""",
    },
    {
        "id": 42,
        "cq": 'UC1-CQ4',
        "type": 'ASK',
        "question": 'Does Morphine have an EV code?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }

""",
    },
    {
        "id": 43,
        "cq": 'UC1-CQ4',
        "type": 'ASK',
        "question": 'Is an EudraVigilance code registered for Prednisone?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Prednisone" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }

""",
    },
    {
        "id": 44,
        "cq": 'UC1-CQ4',
        "type": 'ASK',
        "question": 'Is an EudraVigilance code registered for Codeine?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Codeine" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }

""",
    },
    {
        "id": 45,
        "cq": 'UC1-CQ4-UNII',
        "type": 'SELECT',
        "question": 'What is the FDA UNII code of Guaifenesin?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Guaifenesin" }

""",
    },
    {
        "id": 46,
        "cq": 'UC1-CQ4-UNII',
        "type": 'SELECT',
        "question": 'Give the Unique Ingredient Identifier for Morphine.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" }

""",
    },
    {
        "id": 47,
        "cq": 'UC1-CQ4-UNII',
        "type": 'SELECT',
        "question": 'Give the Unique Ingredient Identifier for Fluoxetine.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Fluoxetine" }

""",
    },
    {
        "id": 48,
        "cq": 'UC1-CQ4-UNII',
        "type": 'SELECT',
        "question": 'Which UNII does Dextromethorphan have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Dextromethorphan" }

""",
    },
    {
        "id": 49,
        "cq": 'UC1-CQ4-UNII',
        "type": 'ASK',
        "question": 'Does Guaifenesin have an FDA UNII code?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Guaifenesin" }

""",
    },
    {
        "id": 50,
        "cq": 'UC1-CQ4-UNII',
        "type": 'ASK',
        "question": 'Does Morphine have an FDA UNII code?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" }

""",
    },
    {
        "id": 51,
        "cq": 'UC1-CQ4-UNII',
        "type": 'ASK',
        "question": 'Is a UNII registered for Fluoxetine?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Fluoxetine" }

""",
    },
    {
        "id": 52,
        "cq": 'UC1-CQ4-UNII',
        "type": 'ASK',
        "question": 'Is a UNII registered for Dextromethorphan?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Dextromethorphan" }

""",
    },
    {
        "id": 53,
        "cq": 'UC1-CQ4-CAS',
        "type": 'SELECT',
        "question": 'What is the CAS Registry Number of Diclofenac?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" }

""",
    },
    {
        "id": 54,
        "cq": 'UC1-CQ4-CAS',
        "type": 'SELECT',
        "question": 'Give the CAS registry number for Ibuprofen.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Ibuprofen" }

""",
    },
    {
        "id": 55,
        "cq": 'UC1-CQ4-CAS',
        "type": 'SELECT',
        "question": 'Give the CAS registry number for Omeprazole.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Omeprazole" }

""",
    },
    {
        "id": 56,
        "cq": 'UC1-CQ4-CAS',
        "type": 'SELECT',
        "question": 'Which CAS number does Morphine have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" }

""",
    },
    {
        "id": 57,
        "cq": 'UC1-CQ4-CAS',
        "type": 'ASK',
        "question": 'Does Diclofenac have a CAS Registry Number?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" }

""",
    },
    {
        "id": 58,
        "cq": 'UC1-CQ4-CAS',
        "type": 'ASK',
        "question": 'Does Ibuprofen have a CAS Registry Number?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Ibuprofen" }

""",
    },
    {
        "id": 59,
        "cq": 'UC1-CQ4-CAS',
        "type": 'ASK',
        "question": 'Is a CAS number registered for Omeprazole?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Omeprazole" }

""",
    },
    {
        "id": 60,
        "cq": 'UC1-CQ4-CAS',
        "type": 'ASK',
        "question": 'Is a CAS number registered for Morphine?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" }

""",
    },
    {
        "id": 61,
        "cq": 'UC1-CQ4.1',
        "type": 'SELECT',
        "question": 'What are all the identifier codes of Diclofenac?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 62,
        "cq": 'UC1-CQ4.1',
        "type": 'SELECT',
        "question": 'Which codes does the substance Guaifenesin have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Guaifenesin" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 63,
        "cq": 'UC1-CQ4.1',
        "type": 'SELECT',
        "question": 'Which codes does the substance Gabapentin have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Gabapentin" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 64,
        "cq": 'UC1-CQ4.1',
        "type": 'SELECT',
        "question": 'List every code registered for Metformin.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metformin" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }

""",
    },
    {
        "id": 65,
        "cq": 'UC1-CQ4.1',
        "type": 'COUNT',
        "question": 'How many identifier codes does Diclofenac have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" ; cmns-id:isIdentifiedBy ?code }

""",
    },
    {
        "id": 66,
        "cq": 'UC1-CQ4.1',
        "type": 'COUNT',
        "question": 'How many identifier codes does Guaifenesin have?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Guaifenesin" ; cmns-id:isIdentifiedBy ?code }

""",
    },
    {
        "id": 67,
        "cq": 'UC1-CQ4.1',
        "type": 'COUNT',
        "question": 'Count the codes registered for Gabapentin.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Gabapentin" ; cmns-id:isIdentifiedBy ?code }

""",
    },
    {
        "id": 68,
        "cq": 'UC1-CQ4.1',
        "type": 'COUNT',
        "question": 'Count the codes registered for Metformin.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metformin" ; cmns-id:isIdentifiedBy ?code }

""",
    },
    {
        "id": 69,
        "cq": 'UC1-CQ6',
        "type": 'SELECT',
        "question": 'Which products contain ASPIRIN or a substance related to it?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ASPIRIN" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 70,
        "cq": 'UC1-CQ6',
        "type": 'SELECT',
        "question": 'What authorized products contain the substance Diclofenac or its relatives?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 71,
        "cq": 'UC1-CQ6',
        "type": 'SELECT',
        "question": 'What authorized products contain the substance Fluoxetine or its relatives?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Fluoxetine" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 72,
        "cq": 'UC1-CQ6',
        "type": 'SELECT',
        "question": 'List the medicinal products that include CETIRIZINE or any related substance.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CETIRIZINE" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 73,
        "cq": 'UC1-CQ6',
        "type": 'COUNT',
        "question": 'How many products contain ASPIRIN or a substance related to it?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ASPIRIN" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 74,
        "cq": 'UC1-CQ6',
        "type": 'COUNT',
        "question": 'How many products contain Diclofenac or a substance related to it?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 75,
        "cq": 'UC1-CQ6',
        "type": 'COUNT',
        "question": 'Count the products containing Fluoxetine or any related substance.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Fluoxetine" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 76,
        "cq": 'UC1-CQ6',
        "type": 'COUNT',
        "question": 'Count the products containing CETIRIZINE or any related substance.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CETIRIZINE" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 77,
        "cq": 'UC1-CQ9',
        "type": 'SELECT',
        "question": 'What is the molecular structure of AMLODIPINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "AMLODIPINE" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }

""",
    },
    {
        "id": 78,
        "cq": 'UC1-CQ9',
        "type": 'SELECT',
        "question": 'Describe the chemical structure of the substance Morphine.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Morphine" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }

""",
    },
    {
        "id": 79,
        "cq": 'UC1-CQ9',
        "type": 'SELECT',
        "question": 'Describe the chemical structure of the substance Dextromethorphan.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Dextromethorphan" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }

""",
    },
    {
        "id": 80,
        "cq": 'UC1-CQ9',
        "type": 'SELECT',
        "question": 'Give the SMILES, molecular formula and molecular weight of Metoprolol.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metoprolol" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }

""",
    },
    {
        "id": 81,
        "cq": 'UC1-CQ10',
        "type": 'SELECT',
        "question": 'How are Supercortisol and Prednisone related?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Supercortisol" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Prednisone" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }

""",
    },
    {
        "id": 82,
        "cq": 'UC1-CQ10',
        "type": 'SELECT',
        "question": 'Are COX-2 and Diclofenac the same, and if not how do they relate?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "COX-2" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }

""",
    },
    {
        "id": 83,
        "cq": 'UC1-CQ10',
        "type": 'SELECT',
        "question": 'Are PREDNISOLONE ANHYDROUS and Prednisone the same, and if not how do they relate?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "PREDNISOLONE ANHYDROUS" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Prednisone" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }

""",
    },
    {
        "id": 84,
        "cq": 'UC1-CQ10',
        "type": 'SELECT',
        "question": 'What is the relationship between VOLTAGE-GATED CALCIUM CHANNEL SUBUNIT ALPHA CAV1.3 and AMLODIPINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "VOLTAGE-GATED CALCIUM CHANNEL SUBUNIT ALPHA CAV1.3" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "AMLODIPINE" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }

""",
    },
    {
        "id": 85,
        "cq": 'UC1-CQ10',
        "type": 'ASK',
        "question": 'Are Supercortisol and Prednisone related?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Supercortisol" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Prednisone" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }

""",
    },
    {
        "id": 86,
        "cq": 'UC1-CQ10',
        "type": 'ASK',
        "question": 'Are COX-2 and Diclofenac related?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "COX-2" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Diclofenac" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }

""",
    },
    {
        "id": 87,
        "cq": 'UC1-CQ10',
        "type": 'ASK',
        "question": 'Is there a defined relationship between PREDNISOLONE ANHYDROUS and Prednisone?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "PREDNISOLONE ANHYDROUS" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Prednisone" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }

""",
    },
    {
        "id": 88,
        "cq": 'UC1-CQ10',
        "type": 'ASK',
        "question": 'Is there a defined relationship between VOLTAGE-GATED CALCIUM CHANNEL SUBUNIT ALPHA CAV1.3 and AMLODIPINE?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "VOLTAGE-GATED CALCIUM CHANNEL SUBUNIT ALPHA CAV1.3" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "AMLODIPINE" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }

""",
    },
    {
        "id": 89,
        "cq": 'UC2-parent',
        "type": 'SELECT',
        "question": 'What is the parent (non-salt) form of CIPROFLOXACIN?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CIPROFLOXACIN" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 90,
        "cq": 'UC2-parent',
        "type": 'SELECT',
        "question": 'Give the non-salt, non-hydrated form of AMLODIPINE.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "AMLODIPINE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 91,
        "cq": 'UC2-parent',
        "type": 'SELECT',
        "question": 'Give the non-salt, non-hydrated form of CAFFEINE.',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CAFFEINE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 92,
        "cq": 'UC2-parent',
        "type": 'SELECT',
        "question": 'Which substance is the parent of the salt/solvate Guaifenesin?',
        "sparql_label": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Guaifenesin" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }

""",
    },
    {
        "id": 93,
        "cq": 'UC2-CQ1.1',
        "type": 'SELECT',
        "question": 'In which products and packages is LEVOTHYROXINE used as an active ingredient?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "LEVOTHYROXINE" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }

""",
    },
    {
        "id": 94,
        "cq": 'UC2-CQ1.1',
        "type": 'SELECT',
        "question": 'Where is Penicillin G used as an active ingredient (products and packaging)?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Penicillin G" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }

""",
    },
    {
        "id": 95,
        "cq": 'UC2-CQ1.1',
        "type": 'SELECT',
        "question": 'Where is LIDOCAINE used as an active ingredient (products and packaging)?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "LIDOCAINE" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }

""",
    },
    {
        "id": 96,
        "cq": 'UC2-CQ1.1',
        "type": 'SELECT',
        "question": 'List the products and package NDCs that use Hydrocortisone as active.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Hydrocortisone" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }

""",
    },
    {
        "id": 97,
        "cq": 'UC2-CQ1.1',
        "type": 'COUNT',
        "question": 'In how many products is LEVOTHYROXINE used as an active ingredient?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "LEVOTHYROXINE" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 98,
        "cq": 'UC2-CQ1.1',
        "type": 'COUNT',
        "question": 'In how many products is Penicillin G used as an active ingredient?',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Penicillin G" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 99,
        "cq": 'UC2-CQ1.1',
        "type": 'COUNT',
        "question": 'Count the products that use LIDOCAINE as active.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "LIDOCAINE" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },
    {
        "id": 100,
        "cq": 'UC2-CQ1.1',
        "type": 'COUNT',
        "question": 'Count the products that use Hydrocortisone as active.',
        "sparql_label": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Hydrocortisone" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }

""",
    },

]


def get_questions(n: int | None = None) -> list:
    return QUESTIONS if n is None else QUESTIONS[:n]