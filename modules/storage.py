"""
DFSL exemplar bank (retrieval pool).
"""

storage = [
    {
        "id": 'P001',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ1',
        "form": 'SELECT',
        "label": 'Which substances have the active moiety HI-TI?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "HI-TI" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P002',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ1',
        "form": 'SELECT',
        "label": 'List all substances whose active moiety is STREPTOCOCCUS THERMOPHILUS KB-19.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "STREPTOCOCCUS THERMOPHILUS KB-19" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P003',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ1',
        "form": 'SELECT',
        "label": 'What substances share the common active moiety SECOBARBITAL [USP IMPURITY]?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?sub ?name WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "SECOBARBITAL [USP IMPURITY]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P004',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ1',
        "form": 'COUNT',
        "label": 'How many substances have the active moiety HI-TI?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "HI-TI" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }"""
    },
    {
        "id": 'P005',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ1',
        "form": 'COUNT',
        "label": 'Count the substances whose active moiety is STREPTOCOCCUS THERMOPHILUS KB-19.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "STREPTOCOCCUS THERMOPHILUS KB-19" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }"""
    },
    {
        "id": 'P006',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ1',
        "form": 'COUNT',
        "label": 'How many substances have the active moiety SECOBARBITAL [USP IMPURITY]?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?sub) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "SECOBARBITAL [USP IMPURITY]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }"""
    },
    {
        "id": 'P007',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ2',
        "form": 'SELECT',
        "label": 'What is the active moiety of TESTOSTERONE UNDECANOATE?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "TESTOSTERONE UNDECANOATE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P008',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ2',
        "form": 'SELECT',
        "label": 'Which substance is the active moiety of 3-CHLORO-4-(6-HYDROXY-2-QUINOLINYL)BENZOIC ACID?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "3-CHLORO-4-(6-HYDROXY-2-QUINOLINYL)BENZOIC ACID" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P009',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ2',
        "form": 'SELECT',
        "label": 'Identify the active moiety of Deleobuvir [WHO-DD].',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?moiety ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Deleobuvir [WHO-DD]" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P010',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ2',
        "form": 'COUNT',
        "label": 'How many active moieties does TESTOSTERONE UNDECANOATE have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "TESTOSTERONE UNDECANOATE" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }"""
    },
    {
        "id": 'P011',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ2',
        "form": 'COUNT',
        "label": 'Count the active moieties of 3-CHLORO-4-(6-HYDROXY-2-QUINOLINYL)BENZOIC ACID.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "3-CHLORO-4-(6-HYDROXY-2-QUINOLINYL)BENZOIC ACID" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }"""
    },
    {
        "id": 'P012',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ2',
        "form": 'COUNT',
        "label": 'How many active moieties does Deleobuvir [WHO-DD] have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?moiety) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Deleobuvir [WHO-DD]" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?moiety ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" }"""
    },
    {
        "id": 'P013',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'SELECT',
        "label": 'Which products contain substances with the active moiety Apixaban [USAN]?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Apixaban [USAN]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }"""
    },
    {
        "id": 'P014',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'SELECT',
        "label": 'List the medicinal products whose active ingredient shares the active moiety GLAUBERITUM.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "GLAUBERITUM" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }"""
    },
    {
        "id": 'P015',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'SELECT',
        "label": 'What products include a substance with common active moiety Pasireotide [WHO-DD]?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Pasireotide [WHO-DD]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname }"""
    },
    {
        "id": 'P016',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'COUNT',
        "label": 'How many products contain substances with the active moiety Apixaban [USAN]?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Apixaban [USAN]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P017',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'COUNT',
        "label": 'Count the products whose active ingredient has active moiety GLAUBERITUM.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "GLAUBERITUM" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P018',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'COUNT',
        "label": 'How many products contain substances with the active moiety Pasireotide [WHO-DD]?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Pasireotide [WHO-DD]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P019',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'LIMIT',
        "label": 'Give 5 products that contain substances with active moiety Apixaban [USAN].',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Apixaban [USAN]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5"""
    },
    {
        "id": 'P020',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'LIMIT',
        "label": 'Show any five medicinal products with active moiety GLAUBERITUM.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "GLAUBERITUM" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5"""
    },
    {
        "id": 'P021',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ3',
        "form": 'LIMIT',
        "label": 'Give 5 products that contain substances with active moiety Pasireotide [WHO-DD].',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?pname WHERE { ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Pasireotide [WHO-DD]" . ?rel idmp-sub:hasRelatedSubstance ?moiety ; idmp-sub:hasSubjectSubstance ?sub ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp ; cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname } LIMIT 5"""
    },
    {
        "id": 'P022',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4',
        "form": 'SELECT',
        "label": 'What is the EV code of EICOSAPENTAENOIC ACID ETHYL ESTER [MI]?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "EICOSAPENTAENOIC ACID ETHYL ESTER [MI]" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }"""
    },
    {
        "id": 'P023',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4',
        "form": 'SELECT',
        "label": 'Which EudraVigilance (SMS) code does EUDISTEMON HUMIFUSUM WHOLE have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "EUDISTEMON HUMIFUSUM WHOLE" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }"""
    },
    {
        "id": 'P024',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4',
        "form": 'SELECT',
        "label": 'Give the EV code for the substance 99MTC-PIPIDA.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "99MTC-PIPIDA" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode ; cmns-txt:hasTextValue ?val }"""
    },
    {
        "id": 'P025',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4',
        "form": 'ASK',
        "label": 'Does EICOSAPENTAENOIC ACID ETHYL ESTER [MI] have an EV code?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "EICOSAPENTAENOIC ACID ETHYL ESTER [MI]" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }"""
    },
    {
        "id": 'P026',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4',
        "form": 'ASK',
        "label": 'Is an EudraVigilance code registered for EUDISTEMON HUMIFUSUM WHOLE?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "EUDISTEMON HUMIFUSUM WHOLE" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }"""
    },
    {
        "id": 'P027',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4',
        "form": 'ASK',
        "label": 'Does 99MTC-PIPIDA have an EV code?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "99MTC-PIPIDA" ; cmns-id:isIdentifiedBy ?code . ?code a idmp-eura:EudraVigilanceCode }"""
    },
    {
        "id": 'P028',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-UNII',
        "form": 'SELECT',
        "label": 'What is the FDA UNII code of Plectranthus tomentosus whole?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Plectranthus tomentosus whole" }"""
    },
    {
        "id": 'P029',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-UNII',
        "form": 'SELECT',
        "label": 'Which UNII does ROCCUS CHRYSOPS FLESH, COOKED have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ROCCUS CHRYSOPS FLESH, COOKED" }"""
    },
    {
        "id": 'P030',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-UNII',
        "form": 'SELECT',
        "label": 'Give the Unique Ingredient Identifier for 1,3-DIOXANE-5,5-DIMETHANOL, 2-PHENYL-.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "1,3-DIOXANE-5,5-DIMETHANOL, 2-PHENYL-" }"""
    },
    {
        "id": 'P031',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-UNII',
        "form": 'ASK',
        "label": 'Does Plectranthus tomentosus whole have an FDA UNII code?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Plectranthus tomentosus whole" }"""
    },
    {
        "id": 'P032',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-UNII',
        "form": 'ASK',
        "label": 'Is a UNII registered for ROCCUS CHRYSOPS FLESH, COOKED?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ROCCUS CHRYSOPS FLESH, COOKED" }"""
    },
    {
        "id": 'P033',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-UNII',
        "form": 'ASK',
        "label": 'Does 1,3-DIOXANE-5,5-DIMETHANOL, 2-PHENYL- have an FDA UNII code?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?code a idmp-nara:UniqueIngredientNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "1,3-DIOXANE-5,5-DIMETHANOL, 2-PHENYL-" }"""
    },
    {
        "id": 'P034',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-CAS',
        "form": 'SELECT',
        "label": 'What is the CAS Registry Number of Apomorphine compd. with 5-oxo-L-proline?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Apomorphine compd. with 5-oxo-L-proline" }"""
    },
    {
        "id": 'P035',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-CAS',
        "form": 'SELECT',
        "label": 'Which CAS number does THIAZOLIUM, 4-(4-BIPHENYLYL)-3-ETHYL-2-(P-1-PYRROLIDINYLSTYRYL)-, IODIDE have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "THIAZOLIUM, 4-(4-BIPHENYLYL)-3-ETHYL-2-(P-1-PYRROLIDINYLSTYRYL)-, IODIDE" }"""
    },
    {
        "id": 'P036',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-CAS',
        "form": 'SELECT',
        "label": 'Give the CAS registry number for NSC-279266.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-txt:hasTextValue ?val ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "NSC-279266" }"""
    },
    {
        "id": 'P037',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-CAS',
        "form": 'ASK',
        "label": 'Does Apomorphine compd. with 5-oxo-L-proline have a CAS Registry Number?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Apomorphine compd. with 5-oxo-L-proline" }"""
    },
    {
        "id": 'P038',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-CAS',
        "form": 'ASK',
        "label": 'Is a CAS number registered for THIAZOLIUM, 4-(4-BIPHENYLYL)-3-ETHYL-2-(P-1-PYRROLIDINYLSTYRYL)-, IODIDE?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "THIAZOLIUM, 4-(4-BIPHENYLYL)-3-ETHYL-2-(P-1-PYRROLIDINYLSTYRYL)-, IODIDE" }"""
    },
    {
        "id": 'P039',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4-CAS',
        "form": 'ASK',
        "label": 'Does NSC-279266 have a CAS Registry Number?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
ASK WHERE { ?code a idmp-nara:CASRegistryNumber ; cmns-id:identifies ?sub . ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "NSC-279266" }"""
    },
    {
        "id": 'P040',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4.1',
        "form": 'SELECT',
        "label": 'What are all the identifier codes of oseltamivir [INN]?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "oseltamivir [INN]" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }"""
    },
    {
        "id": 'P041',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4.1',
        "form": 'SELECT',
        "label": 'List every code registered for SULFAMIC ACID, ((1S,2S,4R)-4-(4-(((1S)-2,3-DIHYDRO-1H-INDEN-1-YL)AMINO)-7H-PYRROLO(2,3-D)PYRIMIDIN-7-YL)-2-HYDROXYCYCLOPENTYL)METHYL ESTER.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "SULFAMIC ACID, ((1S,2S,4R)-4-(4-(((1S)-2,3-DIHYDRO-1H-INDEN-1-YL)AMINO)-7H-PYRROLO(2,3-D)PYRIMIDIN-7-YL)-2-HYDROXYCYCLOPENTYL)METHYL ESTER" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }"""
    },
    {
        "id": 'P042',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4.1',
        "form": 'SELECT',
        "label": 'Which codes does the substance CODONOPSIS RADIX (CODONOPSIS PILOSULA) [CHP] have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?val WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CODONOPSIS RADIX (CODONOPSIS PILOSULA) [CHP]" ; cmns-id:isIdentifiedBy ?code . ?code cmns-txt:hasTextValue ?val }"""
    },
    {
        "id": 'P043',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4.1',
        "form": 'COUNT',
        "label": 'How many identifier codes does oseltamivir [INN] have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "oseltamivir [INN]" ; cmns-id:isIdentifiedBy ?code }"""
    },
    {
        "id": 'P044',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4.1',
        "form": 'COUNT',
        "label": 'Count the codes registered for SULFAMIC ACID, ((1S,2S,4R)-4-(4-(((1S)-2,3-DIHYDRO-1H-INDEN-1-YL)AMINO)-7H-PYRROLO(2,3-D)PYRIMIDIN-7-YL)-2-HYDROXYCYCLOPENTYL)METHYL ESTER.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "SULFAMIC ACID, ((1S,2S,4R)-4-(4-(((1S)-2,3-DIHYDRO-1H-INDEN-1-YL)AMINO)-7H-PYRROLO(2,3-D)PYRIMIDIN-7-YL)-2-HYDROXYCYCLOPENTYL)METHYL ESTER" ; cmns-id:isIdentifiedBy ?code }"""
    },
    {
        "id": 'P045',
        "family": 'substance-code',
        "cq_id": 'UC1-CQ4.1',
        "form": 'COUNT',
        "label": 'How many identifier codes does CODONOPSIS RADIX (CODONOPSIS PILOSULA) [CHP] have?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
SELECT (COUNT(DISTINCT ?code) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "CODONOPSIS RADIX (CODONOPSIS PILOSULA) [CHP]" ; cmns-id:isIdentifiedBy ?code }"""
    },
    {
        "id": 'P046',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ6',
        "form": 'SELECT',
        "label": 'Which products contain IMMUNOGLOBULIN G, ANTI-(HUMAN CALCITONIN GENE-RELATED PEPTIDE RECEPTOR) (HUMAN MONOCLONAL HEAVY CHAIN), DISULFIDE WITH HUMAN MONOCLONAL LIGHT CHAIN, DIMER or a substance related to it?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "IMMUNOGLOBULIN G, ANTI-(HUMAN CALCITONIN GENE-RELATED PEPTIDE RECEPTOR) (HUMAN MONOCLONAL HEAVY CHAIN), DISULFIDE WITH HUMAN MONOCLONAL LIGHT CHAIN, DIMER" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P047',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ6',
        "form": 'SELECT',
        "label": 'List the medicinal products that include GINGER WHOLE or any related substance.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "GINGER WHOLE" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P048',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ6',
        "form": 'SELECT',
        "label": 'What authorized products contain the substance QULIPTA or its relatives?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT DISTINCT ?product WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "QULIPTA" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P049',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ6',
        "form": 'COUNT',
        "label": 'How many products contain IMMUNOGLOBULIN G, ANTI-(HUMAN CALCITONIN GENE-RELATED PEPTIDE RECEPTOR) (HUMAN MONOCLONAL HEAVY CHAIN), DISULFIDE WITH HUMAN MONOCLONAL LIGHT CHAIN, DIMER or a substance related to it?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "IMMUNOGLOBULIN G, ANTI-(HUMAN CALCITONIN GENE-RELATED PEPTIDE RECEPTOR) (HUMAN MONOCLONAL HEAVY CHAIN), DISULFIDE WITH HUMAN MONOCLONAL LIGHT CHAIN, DIMER" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P050',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ6',
        "form": 'COUNT',
        "label": 'Count the products containing GINGER WHOLE or any related substance.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "GINGER WHOLE" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P051',
        "family": 'substance-product',
        "cq_id": 'UC1-CQ6',
        "form": 'COUNT',
        "label": 'How many products contain QULIPTA or a substance related to it?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "QULIPTA" . { ?ai cmns-rlcmp:isPlayedBy ?sub } UNION { ?rel idmp-sub:hasRelatedSubstance ?sub ; idmp-sub:hasSubjectSubstance ?rs . ?ai cmns-rlcmp:isPlayedBy ?rs } ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P052',
        "family": 'substance-structure',
        "cq_id": 'UC1-CQ9',
        "form": 'SELECT',
        "label": 'What is the molecular structure of p-Nitrophenyl isocyanate?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>
SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "p-Nitrophenyl isocyanate" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }"""
    },
    {
        "id": 'P053',
        "family": 'substance-structure',
        "cq_id": 'UC1-CQ9',
        "form": 'SELECT',
        "label": 'Give the SMILES, molecular formula and molecular weight of FLURIDONE [ISO].',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>
SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "FLURIDONE [ISO]" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }"""
    },
    {
        "id": 'P054',
        "family": 'substance-structure',
        "cq_id": 'UC1-CQ9',
        "form": 'SELECT',
        "label": 'Describe the chemical structure of the substance ADENINE [USP MONOGRAPH].',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>
SELECT ?smiles ?formula ?mw WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ADENINE [USP MONOGRAPH]" . OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } }"""
    },
    {
        "id": 'P055',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ10',
        "form": 'SELECT',
        "label": 'How are Metamfepramone hydrochloride [WHO-DD] and METAMFEPYRAMONE related?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metamfepramone hydrochloride [WHO-DD]" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "METAMFEPYRAMONE" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }"""
    },
    {
        "id": 'P056',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ10',
        "form": 'SELECT',
        "label": 'What is the relationship between Metamfepramone hydrochloride [WHO-DD] and METAMFEPRAMONE [MI]?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metamfepramone hydrochloride [WHO-DD]" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "METAMFEPRAMONE [MI]" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }"""
    },
    {
        "id": 'P057',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ10',
        "form": 'SELECT',
        "label": 'Are .BETA.-D-GLUCOPYRANURONIC ACID, 1-((4S,7S,10AS)-OCTAHYDRO-4-(((2S)-2-(METHYLTHIO)-1-OXO-3-PHENYLPROPYL)AMINO)-5-OXO-7H-PYRIDO(2,1-B)(1,3)THIAZEPINE-7-CARBOXYLATE) and OMAPATRILATE the same, and if not how do they relate?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?relType ?comment WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ".BETA.-D-GLUCOPYRANURONIC ACID, 1-((4S,7S,10AS)-OCTAHYDRO-4-(((2S)-2-(METHYLTHIO)-1-OXO-3-PHENYLPROPYL)AMINO)-5-OXO-7H-PYRIDO(2,1-B)(1,3)THIAZEPINE-7-CARBOXYLATE)" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "OMAPATRILATE" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue ?relType . OPTIONAL { ?rel idmp-sub:hasComment ?comment } }"""
    },
    {
        "id": 'P058',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ10',
        "form": 'ASK',
        "label": 'Are Metamfepramone hydrochloride [WHO-DD] and METAMFEPYRAMONE related?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metamfepramone hydrochloride [WHO-DD]" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "METAMFEPYRAMONE" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }"""
    },
    {
        "id": 'P059',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ10',
        "form": 'ASK',
        "label": 'Is there a defined relationship between Metamfepramone hydrochloride [WHO-DD] and METAMFEPRAMONE [MI]?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Metamfepramone hydrochloride [WHO-DD]" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "METAMFEPRAMONE [MI]" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }"""
    },
    {
        "id": 'P060',
        "family": 'substance-relationship',
        "cq_id": 'UC1-CQ10',
        "form": 'ASK',
        "label": 'Are .BETA.-D-GLUCOPYRANURONIC ACID, 1-((4S,7S,10AS)-OCTAHYDRO-4-(((2S)-2-(METHYLTHIO)-1-OXO-3-PHENYLPROPYL)AMINO)-5-OXO-7H-PYRIDO(2,1-B)(1,3)THIAZEPINE-7-CARBOXYLATE) and OMAPATRILATE related?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
ASK WHERE { ?a idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ".BETA.-D-GLUCOPYRANURONIC ACID, 1-((4S,7S,10AS)-OCTAHYDRO-4-(((2S)-2-(METHYLTHIO)-1-OXO-3-PHENYLPROPYL)AMINO)-5-OXO-7H-PYRIDO(2,1-B)(1,3)THIAZEPINE-7-CARBOXYLATE)" . ?b idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "OMAPATRILATE" . ?rel idmp-sub:hasSubjectSubstance ?a ; idmp-sub:hasRelatedSubstance ?b }"""
    },
    {
        "id": 'P061',
        "family": 'substance-relationship',
        "cq_id": 'UC2-parent',
        "form": 'SELECT',
        "label": 'What is the parent (non-salt) form of 3-PYRROLIDINEACETAMIDE, 1-(2-(2,3-DIHYDRO-5-BENZOFURANYL)ETHYL)-.ALPHA.,.ALPHA.-DIPHENYL-, (3S)-?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "3-PYRROLIDINEACETAMIDE, 1-(2-(2,3-DIHYDRO-5-BENZOFURANYL)ETHYL)-.ALPHA.,.ALPHA.-DIPHENYL-, (3S)-" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P062',
        "family": 'substance-relationship',
        "cq_id": 'UC2-parent',
        "form": 'SELECT',
        "label": 'Which substance is the parent of the salt/solvate NSC-404385?',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "NSC-404385" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P063',
        "family": 'substance-relationship',
        "cq_id": 'UC2-parent',
        "form": 'SELECT',
        "label": 'Give the non-salt, non-hydrated form of NSC-759169.',
        "sparql": """PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT ?parent ?name WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "NSC-759169" . ?rel idmp-sub:hasSubjectSubstance ?sub ; idmp-sub:hasRelatedSubstance ?parent ; cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "SALT/SOLVATE->PARENT" . ?parent idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue ?name }"""
    },
    {
        "id": 'P064',
        "family": 'substance-product',
        "cq_id": 'UC2-CQ1.1',
        "form": 'SELECT',
        "label": 'In which products and packages is STREPTOCOCCUS PNEUMONIAE TYPE 18C CAPSULAR POLYSACCHARIDE ANTIGEN used as an active ingredient?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "STREPTOCOCCUS PNEUMONIAE TYPE 18C CAPSULAR POLYSACCHARIDE ANTIGEN" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }"""
    },
    {
        "id": 'P065',
        "family": 'substance-product',
        "cq_id": 'UC2-CQ1.1',
        "form": 'SELECT',
        "label": 'List the products and package NDCs that use AMPHETAMINE ASPARTATE MONOHYDRATE as active.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "AMPHETAMINE ASPARTATE MONOHYDRATE" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }"""
    },
    {
        "id": 'P066',
        "family": 'substance-product',
        "cq_id": 'UC2-CQ1.1',
        "form": 'SELECT',
        "label": 'Where is FIBRINOGEN HUMAN used as an active ingredient (products and packaging)?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
SELECT DISTINCT ?product ?packageNDC WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "FIBRINOGEN HUMAN" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp . OPTIONAL { ?pkg cmns-dsg:isDefinedIn ?product ; cmns-id:isIdentifiedBy/cmns-txt:hasTextValue ?packageNDC } }"""
    },
    {
        "id": 'P067',
        "family": 'substance-product',
        "cq_id": 'UC2-CQ1.1',
        "form": 'COUNT',
        "label": 'In how many products is STREPTOCOCCUS PNEUMONIAE TYPE 18C CAPSULAR POLYSACCHARIDE ANTIGEN used as an active ingredient?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "STREPTOCOCCUS PNEUMONIAE TYPE 18C CAPSULAR POLYSACCHARIDE ANTIGEN" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P068',
        "family": 'substance-product',
        "cq_id": 'UC2-CQ1.1',
        "form": 'COUNT',
        "label": 'Count the products that use AMPHETAMINE ASPARTATE MONOHYDRATE as active.',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "AMPHETAMINE ASPARTATE MONOHYDRATE" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
    {
        "id": 'P069',
        "family": 'substance-product',
        "cq_id": 'UC2-CQ1.1',
        "form": 'COUNT',
        "label": 'In how many products is FIBRINOGEN HUMAN used as an active ingredient?',
        "sparql": """PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
SELECT (COUNT(DISTINCT ?product) AS ?count) WHERE { ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "FIBRINOGEN HUMAN" . ?ai cmns-rlcmp:isPlayedBy ?sub . ?comp idmp-mprd:hasActiveIngredient ?ai . ?product cmns-dsg:isDefinedIn ?comp }"""
    },
]
