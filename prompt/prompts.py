FEW_SHOT_EXAMPLES = [
    # 1.UC1-CQ9/SELECT
    {
        "question": 'Describe the chemical structure of the substance ADENINE [USP MONOGRAPH].',
        "sparql": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu: <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>

SELECT ?smiles ?formula ?mw 
WHERE { 
  ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ADENINE [USP MONOGRAPH]" . 
  OPTIONAL { ?sub idmp-sub:hasDefiningStructure/idmp-sub:hasSMILES/idmp-sub:hasSMILESValue ?smiles } 
  OPTIONAL { ?sub idmp-sub:hasDefiningMolecularFormula/cmns-txt:hasTextValue ?formula } 
  OPTIONAL { ?sub idmp-sub:hasDefiningMolecularWeight/cmns-qtu:hasNumericValue ?mw } 
}""",
    },
    # 2.UC1-CQ3/LIMIT
    {
        "question": 'Give 5 products that contain substances with active moiety Apixaban [USAN].',
        "sparql": """\
PREFIX idmp-mprd: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>

SELECT DISTINCT ?product ?pname 
WHERE { 
  ?moiety idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "Apixaban [USAN]" . 
  ?rel idmp-sub:hasRelatedSubstance ?moiety ; 
       idmp-sub:hasSubjectSubstance ?sub ; 
       cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" . 
  ?ai cmns-rlcmp:isPlayedBy ?sub . 
  ?comp idmp-mprd:hasActiveIngredient ?ai . 
  ?product cmns-dsg:isDefinedIn ?comp ; 
           cmns-dsg:hasName/idmp-mprd:hasFullMedicinalProductName ?pname 
} 
LIMIT 5""",
    },
    # 3.UC1-CQ4-UNII/ASK
    {
        "question": 'Is a UNII registered for ROCCUS CHRYSOPS FLESH, COOKED?',
        "sparql": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-nara: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>

ASK 
WHERE { 
  ?code a idmp-nara:UniqueIngredientNumber ; 
        cmns-id:identifies ?sub . 
  ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "ROCCUS CHRYSOPS FLESH, COOKED" 
}""",
    },
    # 4.UC1-CQ2/COUNT
    {
        "question": 'How many active moieties does TESTOSTERONE UNDECANOATE have?',
        "sparql": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX cmns-dsg: <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>

SELECT (COUNT(DISTINCT ?moiety) AS ?count) 
WHERE { 
  ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "TESTOSTERONE UNDECANOATE" . 
  ?rel idmp-sub:hasSubjectSubstance ?sub ; 
       idmp-sub:hasRelatedSubstance ?moiety ; 
       cmns-dsg:isSignifiedBy/cmns-txt:hasTextValue "ACTIVE MOIETY" 
}""",
    },
    # 5.UC1-CQ4/SELECT
    {
        "question": 'Which EudraVigilance (SMS) code does EUDISTEMON HUMIFUSUM WHOLE have?',
        "sparql": """\
PREFIX idmp-sub: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-eura: <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id: <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-txt: <https://www.omg.org/spec/Commons/TextDatatype/>

SELECT ?val 
WHERE { 
  ?sub idmp-sub:hasSubstanceName/idmp-sub:hasSubstanceNameValue "EUDISTEMON HUMIFUSUM WHOLE" ; 
       cmns-id:isIdentifiedBy ?code . 
  ?code a idmp-eura:EudraVigilanceCode ; 
        cmns-txt:hasTextValue ?val 
}""",
    },
]

# PROMPT TEMPLATE FRAGMENTS
_OUTPUT_FORMAT = """\
=== OUTPUT FORMAT ===
Output ONLY the raw SPARQL query text.
- DO NOT wrap in markdown code fences (no ``` or ```sparql)
- DO NOT add explanation, comments, or preamble
- Start your response directly with PREFIX or SELECT"""

_CONTEXT_HEADER = (
    "You are a SPARQL query generator for a pharmaceutical knowledge graph\n"
    "based on the IDMP (Identification of Medicinal Products) standard."
)

_COT_STEPS = """\
=== INSTRUCTIONS ===
Think step by step. Write out your reasoning for EACH step below before the query:

Step 1 - What form does the answer take?
         yes/no question -> ASK
         build a graph -> CONSTRUCT
         anything else -> SELECT

Step 2 - What do I need to return?
         List the variables or values the question is asking for.

Step 3 - Which class do I start from?
         Pick the anchor class from the schema that matches the subject of the question.

Step 4 - How do I reach each value?
         Trace the property path from the anchor class to each return value.
         Every literal sits behind at least one intermediate node, do not skip it.

Step 5 - Are there any conditions?
         Exact match: "value"^^xsd:string
         Partial match: STRSTARTS / CONTAINS / UCASE
         Missing values: OPTIONAL
         Exclude: FILTER NOT EXISTS
         Aggregate: COUNT / GROUP BY / HAVING / ORDER BY / LIMIT"""


_COT_OUTPUT_FORMAT = """\
=== OUTPUT FORMAT ===
First write your step-by-step reasoning (Step 1 to Step 5).
Then, on its own line, write exactly:
SPARQL:
and after it output ONLY the raw SPARQL query (no markdown fences, starting with PREFIX or SELECT/ASK)."""
