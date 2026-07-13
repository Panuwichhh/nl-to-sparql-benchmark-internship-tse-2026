Domain = """
=== PREFIX DECLARATIONS ===
PREFIX :           <http://example.com/idmp-demo/>
PREFIX idmp-mprd:  <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11615-MedicinalProducts/>
PREFIX idmp-sub:   <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO11238-Substances/>
PREFIX idmp-dtp:   <https://spec.pistoiaalliance.org/idmp/ontology/ISO/ISO21090-HarmonizedDatatypes/>
PREFIX idmp-nara:  <https://spec.pistoiaalliance.org/idmp/ontology/ISO/NorthAmericanJurisdiction/NorthAmericanRegistrationAuthorities/>
PREFIX idmp-eura:  <https://spec.pistoiaalliance.org/idmp/ontology/ISO/EuropeanJurisdiction/EuropeanRegistrationAuthorities/>
PREFIX cmns-id:    <https://www.omg.org/spec/Commons/Identifiers/>
PREFIX cmns-dsg:   <https://www.omg.org/spec/Commons/Designators/>
PREFIX cmns-rlcmp: <https://www.omg.org/spec/Commons/RolesAndCompositions/>
PREFIX cmns-col:   <https://www.omg.org/spec/Commons/Collections/>
PREFIX cmns-cls:   <https://www.omg.org/spec/Commons/Classifiers/>
PREFIX cmns-txt:   <https://www.omg.org/spec/Commons/TextDatatype/>
PREFIX cmns-qtu:   <https://www.omg.org/spec/Commons/QuantitiesAndUnits/>
PREFIX lcc-639-1:  <https://www.omg.org/spec/LCC/Languages/ISO639-1-LanguageCodes/>
PREFIX rdf:        <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:       <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd:        <http://www.w3.org/2001/XMLSchema#>

=== AVAILABLE CLASSES ===
# Substances (ISO 11238) — GSRS side
idmp-sub:Substance                    - A substance (from GSRS, status='approved', or from FDA openFDA data)
idmp-sub:ChemicalSubstance / ProteinSubstance / NucleicAcidSubstance / PolymerSubstance /
  Mixture / StructurallyDiverseSubstance / SpecifiedSubstance
                                       - Substance subtype, by GSRS substance_class (a GSRS substance also keeps the plain idmp-sub:Substance type)
idmp-sub:SubstanceName                - Name node for a substance (GSRS or FDA openFDA)
idmp-sub:SubstanceNameDomain          - Domain/category a substance name belongs to (GSRS only)
idmp-sub:ActiveIngredient             - Active ingredient role (played by a Substance), FDA side
# Substance identifiers/codes (ISO 11238 + jurisdiction-specific ISO modules)
idmp-sub:SubstanceCode                - Generic GSRS code node, used ONLY when the code system is
                                         none of {FDA UNII, CAS, CHEBI, MESH, EudraVigilance-SUBxxxx}
idmp-nara:UniqueIngredientNumber       - FDA UNII code node (GSRS code_system='FDA UNII', AND the
                                         separate FDA-side verified-UNII node under :fda/unii/... — see URI PATTERNS)
idmp-nara:CASRegistryNumber           - CAS Registry Number code node (GSRS code_system='CAS')
idmp-nara:MedicalSubjectHeadingsUniqueIdentifier - MeSH identifier code node (code_system='MESH')
idmp-eura:ChemicalEntitiesOfBiologicalInterestIdentifier - CHEBI identifier code node (code_system='CHEBI')
idmp-eura:EudraVigilanceCode          - EudraVigilance/SMS code node (code_system='EVMPD', value matches ^SUB[A-Z0-9]+$)
idmp-dtp:CodeSystem                   - A coding scheme a SubstanceCode is a member of (e.g. "CAS", "FDA UNII", ...)
idmp-dtp:CodeSystemName               - Name node of a CodeSystem (holds the scheme's literal name)
# Chemistry (GSRS)
idmp-sub:MolecularStructure           - Structure node of a substance
idmp-sub:MolecularStructureIdentifier - External identifier of a MolecularStructure (e.g. an ID string)
idmp-sub:MolecularFormula             - Molecular formula node of a substance
idmp-sub:SMILES                       - SMILES structure node of a substance
idmp-sub:Molfile                      - Molfile (structural representation) node of a substance
idmp-sub:MolecularWeight              - Molecular weight node of a substance
# Substance relationships (GSRS only — both sides are always GSRS substances)
idmp-sub:SubstanceRelationship        - A relationship between two GSRS substances
idmp-sub:SubstanceRelationshipCode    - The type-code node of a relationship (its text value is the type, e.g. "ACTIVE MOIETY")
idmp-sub:SubstanceRelationshipType    - A secondary "interaction type" classification node of a relationship (rarer; separate from the type code)
# Medicinal products & packaging (ISO 11615, FDA side)
idmp-mprd:MedicinalProduct            - A medicinal product (FDA product level)
idmp-mprd:MedicinalProductName        - Name node for a product
idmp-mprd:MedicinalProductIdentifier  - Identifier node for a product (product NDC)
idmp-mprd:PharmaceuticalProduct       - The pharmaceutical-product facet of a medicinal product
idmp-mprd:ProductComposition          - Composition node; both the product and its pharmaceutical-product are
                                         "defined in" this node, and it is what carries the active ingredients
idmp-mprd:QuantitativeComposition / QualitativeComposition - ProductComposition subtype, by composition_type
idmp-mprd:PharmaceuticalDoseForm      - Dose form node
idmp-mprd:RouteOfAdministration       - Route-of-administration node
idmp-mprd:RouteOfAdministrationCode   - Label/code node for a route (linked to RouteOfAdministration via isSignifiedBy)
idmp-mprd:PackagedMedicinalProduct    - A packaged medicinal product (FDA package level)
idmp-mprd:PackageIdentifier           - Identifier node for a package (package NDC)
cmns-cls:Classifier                   - Generic classifier node; used for a product identifier's TYPE (no
                                         more specific idmp-mprd class exists for identifier-type)

=== NAMED INDIVIDUALS (object values, not classes) ===
# Value of idmp-sub:hasSubstanceNameType for a GSRS substance name (from name_type: cn/sys/cd/of/bn).
# NOTE: there is no "PreferredName" / "DisplayName" classifier in this graph — only these five:
idmp-sub:SubstanceNameClassifier-CommonName
idmp-sub:SubstanceNameClassifier-SystematicName
idmp-sub:SubstanceNameClassifier-CompanyCode
idmp-sub:SubstanceNameClassifier-OfficialName
idmp-sub:SubstanceNameClassifier-BrandName
# Value of idmp-sub:hasStereochemistry / hasOpticalActivity: a data-driven individual under idmp-sub:,
# e.g. idmp-sub:{stereochemistry_classifier}. Not enumerable here — only present when the source column
# is non-null; if the question needs a specific value, query the graph rather than guessing the IRI.

=== AVAILABLE PROPERTIES ===
# Identifiers & codes (generic pattern, reused across substances/products/packages/structures)
cmns-id:isIdentifiedBy             - Substance/Product/Package/MolecularStructure -> its Identifier or Code node
cmns-id:identifies                 - Identifier/Code node -> the thing it identifies (inverse of isIdentifiedBy)
cmns-txt:hasTextValue              - Identifier/Code/MolecularFormula/RelationshipCode/CodeSystemName/DoseForm/
                                      RouteCode/IdentifierType node -> xsd:string (the literal code/NDC/formula/label value)
cmns-col:isMemberOf                - SubstanceCode (any code, including UNII/CAS/CHEBI/MESH/EV) -> CodeSystem
cmns-cls:isClassifiedBy            - MedicinalProductIdentifier -> its type Classifier node;
                                      also SubstanceRelationship -> SubstanceRelationshipType (secondary classification)
cmns-cls:classifies                - inverse of isClassifiedBy
# Names & designators
cmns-dsg:hasName                   - MedicinalProduct -> MedicinalProductName;  CodeSystem -> CodeSystemName
cmns-dsg:isDefinedIn               - MedicinalProduct -> ProductComposition;  PharmaceuticalProduct -> ProductComposition;
                                      PackagedMedicinalProduct -> MedicinalProduct
cmns-dsg:defines                   - inverse of isDefinedIn
cmns-dsg:hasDescription            - PackagedMedicinalProduct -> xsd:string
cmns-dsg:isSignifiedBy             - SubstanceRelationship -> SubstanceRelationshipCode;  RouteOfAdministration -> RouteOfAdministrationCode
cmns-dsg:denotes                   - inverse of isSignifiedBy
rdfs:label                         - ALSO holds the same literal as cmns-txt:hasTextValue on:
                                      SubstanceNameDomain, PharmaceuticalDoseForm, RouteOfAdministrationCode,
                                      the identifier-type Classifier node (both predicates work; NOT on CodeSystem
                                      itself — a CodeSystem's name is reached via cmns-dsg:hasName -> CodeSystemName)
idmp-mprd:hasFullMedicinalProductName - MedicinalProductName -> xsd:string
idmp-mprd:hasActiveIngredient      - ProductComposition -> ActiveIngredient
idmp-mprd:hasDoseForm              - PharmaceuticalProduct -> PharmaceuticalDoseForm
idmp-mprd:hasRouteOfAdministration - PharmaceuticalProduct -> RouteOfAdministration
# Substances, names, ingredients
idmp-sub:hasSubstanceName          - Substance -> SubstanceName
idmp-sub:hasSubstanceNameValue     - SubstanceName -> xsd:string
idmp-sub:hasSubstanceNameType      - SubstanceName -> SubstanceNameClassifier individual (Common/Systematic/CompanyCode/Official/Brand)
idmp-sub:hasSubstanceNameDomain    - SubstanceName -> SubstanceNameDomain  (GSRS names only)
idmp-dtp:hasLanguageCode           - SubstanceName -> lcc-639-1 language individual  (GSRS names only)
cmns-rlcmp:isPlayedBy              - ActiveIngredient -> Substance (a :gsrs/substance/... when FDA-GSRS matched,
                                      otherwise a :fda/substance/... openFDA substance when unmatched)
cmns-col:comprises                 - MedicinalProduct -> PharmaceuticalProduct;  PharmaceuticalProduct -> Substance
                                      (:gsrs/substance/... or :fda/substance/...)
# Substance relationships (GSRS)
idmp-sub:hasSubjectSubstance       - SubstanceRelationship -> subject Substance (always a :gsrs/substance/...)
idmp-sub:hasRelatedSubstance       - SubstanceRelationship -> related Substance (always a :gsrs/substance/...)
idmp-sub:hasComment                - SubstanceRelationship / SubstanceCode -> xsd:string  (optional)
# Chemistry (GSRS)
idmp-sub:hasDefiningStructure       - Substance -> MolecularStructure
idmp-sub:hasDefiningMolecularFormula - Substance -> MolecularFormula
idmp-sub:hasDefiningMolecularWeight - Substance -> MolecularWeight
idmp-sub:hasSMILES                 - Substance -> SMILES  (also: MolecularStructure -> SMILES)
idmp-sub:hasSMILESValue            - SMILES -> xsd:string
idmp-sub:hasMolfile                - MolecularStructure -> Molfile
idmp-sub:hasStructuralRepresentationText - Molfile -> xsd:string
idmp-sub:hasStereochemistry         - Substance -> data-driven idmp-sub: individual  (optional)
idmp-sub:hasOpticalActivity         - Substance -> data-driven idmp-sub: individual  (optional)
cmns-qtu:hasNumericValue           - MolecularWeight -> xsd:decimal  (NOTE: decimal, not string)
idmp-dtp:hasDisplayName            - SubstanceCode -> xsd:string  (optional display label of a code)
idmp-dtp:hasReferenceURL           - SubstanceCode -> xsd:anyURI  (optional; only set when code_url looks like a URL)

=== URI PATTERNS ===
# GSRS source (:gsrs/...) — substances, chemistry, relationships, names, codes
:gsrs/substance/{gsrs_uuid}                              a idmp-sub:Substance (+ subtype)
:gsrs/substance-name/{name_uuid}                         a idmp-sub:SubstanceName
:gsrs/substance-name-domain/{domain_key}                 a idmp-sub:SubstanceNameDomain
:gsrs/substance-code/{code_uuid}                         a idmp-sub:SubstanceCode OR idmp-nara:UniqueIngredientNumber
                                                          OR idmp-nara:CASRegistryNumber OR idmp-nara:MedicalSubjectHeadingsUniqueIdentifier
                                                          OR idmp-eura:ChemicalEntitiesOfBiologicalInterestIdentifier OR idmp-eura:EudraVigilanceCode
                                                          (depending on code_system; see AVAILABLE CLASSES)
:gsrs/code-system/{code_system_key}                      a idmp-dtp:CodeSystem
:gsrs/code-system-name/{code_system_key}                 a idmp-dtp:CodeSystemName
:gsrs/molecular-structure/{structure_key}                a idmp-sub:MolecularStructure
:gsrs/molecular-structure-id/{structure_id}              a idmp-sub:MolecularStructureIdentifier
:gsrs/molecular-formula/{structure_key}                  a idmp-sub:MolecularFormula
:gsrs/molecular-weight/{structure_key}                   a idmp-sub:MolecularWeight
:gsrs/smiles/{structure_key}                             a idmp-sub:SMILES
:gsrs/molfile/{structure_key}                            a idmp-sub:Molfile
:gsrs/substance-relationship/{relationship_uuid}         a idmp-sub:SubstanceRelationship
:gsrs/substance-relationship-code/{relationship_type_key} a idmp-sub:SubstanceRelationshipCode
:gsrs/substance-relationship-type/{interaction_type_key}  a idmp-sub:SubstanceRelationshipType
# FDA source (:fda/...) — products, packages, active ingredients, openFDA substances
:fda/product/{product_id}                                a idmp-mprd:MedicinalProduct
:fda/product-name/{product_name_key}                     a idmp-mprd:MedicinalProductName
:fda/medicinal-product-identifier/{identifier_key}       a idmp-mprd:MedicinalProductIdentifier  (product NDC)
:fda/medicinal-product-identifier-type/{identifier_type_key} a cmns-cls:Classifier
:fda/pharmaceutical-product/{pharmaceutical_product_key} a idmp-mprd:PharmaceuticalProduct
:fda/product-composition/{product_composition_key}       a idmp-mprd:ProductComposition (+ Quantitative/Qualitative)
:fda/dose-form/{dose_form_key}                           a idmp-mprd:PharmaceuticalDoseForm
:fda/route/{route_key}                                   a idmp-mprd:RouteOfAdministration
:fda/route-code/{route_key}                              a idmp-mprd:RouteOfAdministrationCode
:fda/package/{package_key}                               a idmp-mprd:PackagedMedicinalProduct
:fda/package-identifier/{package_identifier_key}         a idmp-mprd:PackageIdentifier  (package NDC)
:fda/active-ingredient/{active_ingredient_key}           a idmp-sub:ActiveIngredient
:fda/substance/{substance_key}                           a idmp-sub:Substance  (openFDA substance, used only when NOT matched to a GSRS substance)
:fda/substance-name/{substance_name_key}                 a idmp-sub:SubstanceName  (name of the openFDA substance above)
:fda/unii/{active_ingredient_key}                        a idmp-nara:UniqueIngredientNumber  (FDA-verified UNII node,
                                                          ONLY exists for active ingredients matched to a GSRS substance;
                                                          cmns-id:identifies the MATCHED :gsrs/substance/{gsrs_uuid} — NOT an
                                                          :fda/substance/... node. There is no canonical/unified substance
                                                          IRI in this graph: a matched ingredient's substance data lives on
                                                          the :gsrs/substance/... node; only this extra UNII node is FDA-side.)
# There is NO cross-source "canonical" IRI (no :substance/{unii}, no obda:isCanonicalIRIOf) in this graph.
# To restrict a query to one source, FILTER on the IRI string, e.g.
#   FILTER(STRSTARTS(STR(?s), "http://example.com/idmp-demo/gsrs/substance/"))

=== CONTROLLED VOCABULARY (exact literal values for filters) ===
# These are DATA values, not schema. The property list tells you the PATH to a coded
# value; this section tells you the exact string to match. Values are ^^xsd:string.

# Code systems — value reached via SubstanceCode -> cmns-col:isMemberOf -> CodeSystem -> cmns-dsg:hasName
#   -> CodeSystemName -> cmns-txt:hasTextValue (two hops; NOT rdfs:label on CodeSystem directly).
#   For UNII/CAS/CHEBI/MESH/EudraVigilance it is simpler and preferred to filter by the code node's
#   CLASS instead (idmp-nara:UniqueIngredientNumber / CASRegistryNumber / MedicalSubjectHeadingsUniqueIdentifier,
#   idmp-eura:ChemicalEntitiesOfBiologicalInterestIdentifier / EudraVigilanceCode) rather than walking to CodeSystemName.
#   Other schemes (anything not in that list) only exist as a generic idmp-sub:SubstanceCode + CodeSystem name, e.g.
#   RXCUI, PUBCHEM, and others that may appear in the data — for those, the CodeSystemName path is the only way in.
#   NOTE: there is no ATC / WHO-ATC mapping in this graph.

# Substance-relationship types — value of (SubstanceRelationshipCode cmns-txt:hasTextValue ...).
#   Path: SubstanceRelationship -> cmns-dsg:isSignifiedBy -> SubstanceRelationshipCode -> cmns-txt:hasTextValue
#   Convention: "<SUBJECT ROLE>->[<RELATED ROLE>]"; most types have an inverse (A->B and B->A).
#   GSRS defines ~280 types; the common ones (match the literal EXACTLY, arrows/slashes included):
ACTIVE MOIETY            - active moiety of a substance (single literal, no inverse arrow)
SALT/SOLVATE->PARENT     - salt/solvate form -> its parent   (inverse: PARENT->SALT/SOLVATE)
IMPURITY->PARENT         - impurity -> its parent            (inverse: PARENT->IMPURITY)
METABOLITE->PARENT       - metabolite -> its parent          (inverse: PARENT->METABOLITE)
ACTIVE ISOMER->PARENT    - active isomer -> its parent       (inverse: PARENT->ACTIVE ISOMER)
ANALOGUE->PARENT         - structural analogue -> its parent (inverse: PARENT->ANALOGUE)
#   ...and ~270 more of the same "ROLE->ROLE" form. Pick the literal that names the
#   relationship the question asks about; if unsure, this is the value to FILTER on.

=== RULES ===
(Single-hop paths are not listed here — read domain/range straight from AVAILABLE PROPERTIES.
 These rules only cover what is not obvious from the property list alone.)
1. All literals are typed xsd:string EXCEPT molecular weight (cmns-qtu:hasNumericValue is xsd:decimal)
   and a code's reference URL (idmp-dtp:hasReferenceURL is xsd:anyURI). When matching a literal in a
   FILTER or triple, use "value"^^xsd:string (or the matching type above).
2. Active ingredient -> substance name (multi-hop), FDA side:
   MedicinalProduct -> cmns-col:comprises -> PharmaceuticalProduct; separately
   MedicinalProduct -> cmns-dsg:isDefinedIn -> ProductComposition -> idmp-mprd:hasActiveIngredient -> ActiveIngredient
   -> cmns-rlcmp:isPlayedBy -> Substance -> idmp-sub:hasSubstanceName -> idmp-sub:hasSubstanceNameValue -> string
3. Substance identifiers/codes (GSRS): Substance -> cmns-id:isIdentifiedBy -> a code node typed either as the
   generic idmp-sub:SubstanceCode or as one of the specific classes (UniqueIngredientNumber / CASRegistryNumber /
   MedicalSubjectHeadingsUniqueIdentifier / ChemicalEntitiesOfBiologicalInterestIdentifier / EudraVigilanceCode)
   -> cmns-txt:hasTextValue -> string. Every code node ALSO has cmns-col:isMemberOf -> CodeSystem regardless of type.
4. UNII specifically has TWO possible paths to the same information:
   - GSRS-native: Substance -> isIdentifiedBy -> (a code node) a idmp-nara:UniqueIngredientNumber -> hasTextValue
   - FDA-verified: the :fda/unii/{...} node (see URI PATTERNS) also a idmp-nara:UniqueIngredientNumber, reached
     via cmns-id:identifies pointing AT the substance (query from the code node, or via the substance's isIdentifiedBy)
   A robust UNII query should not assume only one of the two exists for a given substance.
5. Chemistry (GSRS substance):
   - formula: Substance -> idmp-sub:hasDefiningMolecularFormula -> MolecularFormula -> cmns-txt:hasTextValue -> string
   - SMILES:  Substance -> idmp-sub:hasDefiningStructure -> MolecularStructure -> idmp-sub:hasSMILES -> SMILES
              -> idmp-sub:hasSMILESValue -> string  (Substance also has a DIRECT idmp-sub:hasSMILES shortcut to the
              same SMILES node, skipping the MolecularStructure hop)
   - weight:  Substance -> idmp-sub:hasDefiningMolecularWeight -> MolecularWeight -> cmns-qtu:hasNumericValue -> decimal
6. Substance relationship: SubstanceRelationship -> idmp-sub:hasSubjectSubstance / idmp-sub:hasRelatedSubstance
   -> a :gsrs/substance/{uuid} node directly (both sides are always GSRS substances; there is no FDA-side
   relationship data). Type via cmns-dsg:isSignifiedBy -> SubstanceRelationshipCode -> cmns-txt:hasTextValue -> string.
7. Data sources by IRI prefix — there is NO canonical/cross-source substance IRI in this graph:
   - :gsrs/...     GSRS data (chemistry, codes, name domains, relationships; the substance node used by matched
                   FDA active ingredients and by ALL substance relationships)
   - :fda/...      FDA NDC data (products, packages, active ingredients, product/package identifiers); an
                   active ingredient's substance is :gsrs/substance/... when matched to GSRS, or a separate
                   :fda/substance/... openFDA-only node when unmatched (no UNII link in that case)
   To restrict to one source, FILTER on the IRI string, e.g.
   FILTER(STRSTARTS(STR(?s), "http://example.com/idmp-demo/gsrs/substance/")).
"""
