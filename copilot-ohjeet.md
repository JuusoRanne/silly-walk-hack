# GitHub Copilotin työpajaohje

## 1. Johdanto (Noin 5 minuuttia)

Tämä opas kuvaa, kuinka GitHub Copilotia käytetään tehokkaasti "The Silly Walk Grant Application Orchestrator" -projektissa (taustajärjestelmiin keskittyvä palvelu). Tavoitteena on käyttää Copilotia suunnitteluun, dokumentaatiovetoiseen kehitykseen, turvalliseen toteutukseen ja API-dokumentaatioon aikarajoitetussa työpajassa (esim. 2 tuntia). Painopiste on strukturoidussa yhteistyössä tekoälyn kanssa.

## 2. Vaihe 1: Ideointi ja suunnittelu Copilotin kanssa (Noin 30-40 minuuttia)

Tämä vaihe on ratkaisevan tärkeä selkeän suunnan asettamisessa. Tehokas suunnittelu ja dokumentointi tässä vaiheessa virtaviivaistavat merkittävästi toteutusvaihetta Copilotin kanssa.

### 2.1. Tutustu projektin vaatimuksiin
Tutustu projektin pääkuvausdokumenttiin (esim. `#file:README.md`) "The Silly Walk Grant Application Orchestrator" -projektia varten ymmärtääksesi projektin tavoitteet ja liiketoiminnalliset vaatimukset (mukaan lukien turvallisuus- ja OpenAPI-määräykset). Varmista, että jokainen tiimin jäsen ymmärtää MVP:n (Minimum Viable Product - Pienin Toimiva Tuote) selkeästi.

### 2.2. Suunnittelutapa Copilotin kanssa
Käytä Copilot Chatia tässä vaiheessa ideoidaksesi ja hioaksesi projektisi suuntaa.
* **Vaihtoehto A (Tekoälyavusteinen ideointi):** Jos tiimisi on epävarma, mistä aloittaa.
    * **Esimerkkikehote (Copilot Chat):**
        ```
        Review the main project description document (e.g., #file:README.md) for 'The Silly Walk Grant Application Orchestrator'. This project involves building a secure backend API with data validation, business logic (scoring), data persistence, API key authentication, and mandatory OpenAPI documentation.
        1. Propose 2 distinct application architectures (e.g., a RESTful API service using a specific backend framework, a microservice-oriented approach for distinct functions like submission and scoring).
        2. For each architecture, suggest suitable primary programming languages (e.g., Node.js/Express, Python/FastAPI, Java/Spring Boot) and relevant key frameworks/libraries for API development, data persistence (e.g., ORMs like Sequelize/SQLAlchemy, or direct DB drivers), security aspects, and OpenAPI generation.
        3. Outline main components for each (e.g., API route handlers, validation service, scoring engine, data access layer).
        Focus on an MVP achievable in 2 hours that meets all core requirements.
        ```
* **Vaihtoehto B (Osallistujajohtoinen, tekoälyn tarkentama):** Jos tiimilläsi on alustavia ideoita.
    * **Esimerkkikehote (Copilot Chat):**
        ```
        For 'The Silly Walk Grant Application Orchestrator' project (described in the main project #file:README.md ), we plan a [describe your architecture, e.g., 'Node.js Express application using Sequelize for SQLite persistence, with API key authentication and generating OpenAPI docs using swagger-jsdoc'].
        1. Is this MVP (including security basics and OpenAPI spec) feasible in 2 hours?
        2. Suggest key libraries/modules for our chosen stack that would be good for request validation, implementing the scoring logic, secure API key handling, and generating the OpenAPI spec from code comments?
        3. Outline the main functional modules (e.g., route files, controller/service files, models).
        ```

### 2.3. Määritä arkkitehtuuri ja teknologiakokonaisuus (tech stack)
Ideoinnin perusteella tiiminne tulisi päättää:
* Korkean tason arkkitehtuuri.
* Ensisijaiset ohjelmointikielet ja keskeiset kehykset/kirjastot taustajärjestelmälle, mukaan lukien API-dokumentaatioon.
Näiden valintojen dokumentointi on seuraava askel.

### 2.4. Luo projektin määrittelydokumentaatio
Selkeät määrittelyt ovat elintärkeitä sekä tiimisi että Copilotin ohjaamisessa. Nämä dokumentit tulisi luoda yhteistyössä ja iteratiivisesti.

**Työnkulku määrittelydokumenttien luomiseen:**
On suositeltavaa luoda nämä määrittelytiedostot (`ARCHITECTURE.md`, `BACKLOG.md`, `PROJECT_SPEC.md`) yksitellen.
1.  Keskustelkaa kunkin osion/tiedoston sisällöstä tiiminä.
2.  Käyttäkää Copilot Chatia, erityisesti **Copilot Edits** -toimintoa (esim. käyttämällä `#file` tai `#selection` Copilot Chatissa kohdistaaksenne muutokset tiettyihin tiedostoihin/tiedostojen osiin), auttamaan kunkin dokumentin luonnostelussa, päivittämisessä ja hiomisessa.
3.  Luokaa manuaalisesti `docs/specifications/` -kansio ja tyhjät markdown-tiedostot ensin. Tämä helpottaa Copilot Edits -toiminnon kohdistamista niihin.

**Keskeiset määrittelytiedostot:**

* **1. Arkkitehtuurikaavio (`docs/specifications/ARCHITECTURE.md`):**
    * **Tarkoitus:** Esittää visuaalisesti valitsemanne sovellusarkkitehtuuri.
    * **Sisältö:** Käytä tekstipohjaisia kaaviotyökaluja, kuten Mermaid JS, PlantUML, tai selkeää tekstimuotoista kuvausta komponenteista (esim. API Gateway/Router, Kontrollerit/Palvelut, Data Access Layer, Tietokanta).
    * **Esimerkkikehote (Copilot Chat ja Edits `ARCHITECTURE.md`-tiedostolle):**
        ```
        #file:docs/specifications/ARCHITECTURE.md
        Based on our decision to build a [e.g., 'RESTful API using {Your Chosen Framework} for The Silly Walk Grant Application Orchestrator'], help me draft a Mermaid JS component diagram illustrating the main backend components (e.g., API Endpoints, Validation Service, Scoring Engine, Persistence Service) and their interactions.
        ```

* **2. Ominaisuuslista (backlog) (`docs/specifications/BACKLOG.md`):**
    * **Tarkoitus:** Listata MVP:hen vaadittavat ominaisuudet jaettuna hallittaviin tehtäviin.
    * **Sisältö:** Lista ominaisuuksista/käyttäjätarinoista. Priorisoi MVP:tä varten.
    * **Esimerkkikehote (Copilot Chat ja Edits `BACKLOG.md`-tiedostolle):**
        ```
        #file:docs/specifications/BACKLOG.md
        Based on 'The Silly Walk Grant Application Orchestrator' MVP requirements (see #file:README.md ), help me create a feature backlog. Key MVP tasks include:
        - Define API contract and create initial OpenAPI specification file (e.g., docs/api/openapi.yaml).
        - Implement POST /applications endpoint.
        - Implement input validation for application submission.
        - Implement API key authentication for the POST endpoint.
        - Develop Silliness Scoring Algorithm logic.
        - Implement data persistence for applications (e.g., using an in-memory store or SQLite).
        - Implement GET /applications/{id} endpoint.
        - Implement GET /applications (list) endpoint.
        - Ensure OpenAPI specification is updated to reflect all implemented endpoints and schemas.
        Break these down into clear backlog items.
        ```

* **3. Projektin päämäärittely (`docs/specifications/PROJECT_SPEC.md`):**
    * **Tarkoitus:** Keskeinen dokumentti, joka tiivistää tärkeimmät päätökset ja linkittää muihin yksityiskohtaisiin määrittelyihin.
    * **Sijainti:** `docs/specifications/PROJECT_SPEC.md`
    * **Sisällön runko:**
        * Projektin tavoite (lyhyesti, Silly Walks Orchestratorin pääasiallisesta `#file:README.md`-tiedostosta)
        * Viittaus arkkitehtuurikaavioon: "Katso `docs/specifications/ARCHITECTURE.md`"
        * Viittaus ominaisuuslistaan: "Katso `docs/specifications/BACKLOG.md`"
        * Valittu teknologiakokonaisuus (tech stack) (tietyt kielet, kehykset, tietokanta, OpenAPI-työkalut)
        * Keskeiset moduulit/komponentit ja niiden päävastuut (korkean tason tekstuaalinen kuvaus)
        * OpenAPI-määrittelytiedoston sijainti (esim. `docs/api/openapi.yaml`).
    * **Esimerkkikehote (Copilot Chat ja Edits `PROJECT_SPEC.md`-tiedostolle, ARCHITECTURE ja BACKLOG -tiedostojen luonnostelun jälkeen):**
        ```
        #file:docs/specifications/PROJECT_SPEC.md
        Help me create the main project specification for 'The Silly Walk Grant Application Orchestrator'.
        It should include:
        - Project Goal (summary, emphasizing secure backend API and OpenAPI, referencing #file:README.md).
        - Reference to #file:docs/specifications/ARCHITECTURE.md.
        - Reference to #file:docs/specifications/BACKLOG.md.
        - Our chosen Technology Stack: [e.g., Python/FastAPI, SQLAlchemy for ORM with SQLite, Pydantic for validation, FastAPI's built-in OpenAPI generation].
        - Brief outline of Key Modules/Components: [e.g., `main.py` (API routes), `services/scoring_service.py`, `db/models.py`, `auth/api_key_auth.py`].
        - Path to OpenAPI file: `docs/api/openapi.json`.
        ```

---

## 3. Vaihe 2: Valmistautuminen Copilot-vetoiseen toteutukseen (Noin 20-25 minuuttia)

Kun suunnitelma on valmis, määritä ympäristösi ja keskeiset ohjetiedostot.

### 3.1. Versionhallinta Gitillä
Alusta Git-repositorio ja tee committeja usein: `git init`, `git add .`, `git commit -m "Initial planning and specification documents created"`.

### 3.2. Yleiset Copilot-ohjeet (`.github/copilot-instructions.md`)
Tämä tiedosto tarjoaa projektikohtaisen, pysyvän kontekstin Copilotille VS Codessa.
* **Sijainti:** `.github/copilot-instructions.md`
* **Esimerkkisisältö:**
    ```markdown
    ## Project: The Silly Walk Grant Application Orchestrator

    **Overall Goal:** Build a secure backend API service for managing silly walk grant applications, including data validation, business logic (scoring), persistence, API key authentication, and comprehensive OpenAPI documentation.
    **Core Requirements Document:** Refer to the main project description #file:README.md for "Silly Walks Orchestrator".
    **MVP Technical Specification:** Detailed in #file:docs/specifications/PROJECT_SPEC.md.
    **OpenAPI Specification:** Located at #file:docs/api/openapi.yaml (or as defined in #file:docs/specifications/PROJECT_SPEC.md). This document MUST be kept up-to-date with API changes. Refer to #file:README.md Section 8 for OpenAPI requirements.
    **Security Requirements:** Detailed in #file:README.md Section 7. These are critical.

    **Key Context (for quick reference by inline chat/edit modes):**
    * **Application Payload (POST /applications):** JSON with `applicant_name`, `walk_name`, `description`, `has_briefcase`, `involves_hopping`, `number_of_twirls`.
    * **Core Logic:** Validate inputs, calculate "Silliness Score" based on rules in #file:README.md, assign unique ID (UUID preferred), store application.
    * **Authentication:** API key required for `POST /applications` (and other future sensitive endpoints), passed via HTTP header (e.g., `X-API-Key`).
    * **Data Store:** Team's choice (MVP can be in-memory, file, or SQLite), using parameterized queries/ORM if SQL.

    ## Role: AI Pair Programmer

    You are assisting developers in a 2-hour workshop to build a secure MVP for "The Silly Walk Grant Application Orchestrator", based *only* on provided documents and instructions.

    ## General Instructions for All Interactions:

    1.  **Scope Adherence:** Implement *only* features explicitly requested or detailed in referenced specifications. Adhere strictly to security (#file:README.md Section 7) and OpenAPI (#file:README.md Section 8) requirements.
    2.  **Clarify Ambiguity:** If a request is unclear, or if a significantly better MVP-aligned alternative exists (especially regarding security or OpenAPI generation), state reasoning and ask for confirmation.
    3.  **Clarity, Simplicity, Security:** Generate readable, well-commented code. Prioritize secure coding practices.
    4.  **Documentation is Truth:** Prioritize #file:README.md, #file:docs/specifications/PROJECT_SPEC.md, and `docs/tasks/` instructions.
    5.  **Tech Stack Adherence:** Follow choices in #file:docs/specifications/PROJECT_SPEC.md.
    6.  **Secure Error Handling:** Error responses must not leak internal details.
    7.  **OpenAPI Upkeep:** Remind users or assist in updating the OpenAPI spec (e.g., #file:docs/api/openapi.yaml) if API-impacting changes are made, as per the `agent_workflow.md`.
    ```

### 3.3. Ohjaavat dokumentit Copilotin Agent-tilalle ja monimutkaisille tehtäville

Tehokkaaseen Copilot Agent-tilan käyttöön (tai monimutkaisten toteutusten ohjaamiseen Chatin kautta) tarvitaan selkeä, dokumentoitu suunnitelma kullekin tehtävälle. Tämä sisältää kaksi avaindokumenttityyppiä:

**Tehtäväkohtaisten dokumenttien luontiprosessi Copilot Chatin avulla:**

Ennen kuin voit tehokkaasti delegoida monimutkaisen tehtävän Copilot Agent-tilalle, tarvitset hyvin määritellyn tehtävänmäärittelyn. Suositeltu työnkulku näiden tehtävädokumenttien (esim. `docs/tasks/`-kansiossa olevien) luomiseen tai hiomiseen on iteratiivinen ja yhteistyöhön perustuva, käyttäen Copilot Chatia:

1.  **Keskustele "Mitä" ja "Miten":** Valitse ominaisuus `#file:docs/specifications/BACKLOG.md`-tiedostostasi. Avaa Copilot Chat. Käytä yleisiä chat-ominaisuuksia (`@workspace` auttaa Copilotia ymmärtämään projektisi kontekstin) tai **Copilot Edits** -tilaa (`#file`, `#selection`, jos sinulla on jo luonnos tiedostosta).
    * Keskustelkaa tavoitteesta: Mitä tällä ominaisuudella tulisi saavuttaa?
    * Tutkikaa toteutusstrategioita: Miten tämä voitaisiin rakentaa? Mitkä ovat keskeiset funktiot tai komponentit *tätä nimenomaista tehtävää varten*? Mitkä ovat mahdolliset haasteet?
    * Hienosäätäkää yksityiskohtia: Selventäkää syötteitä, tulosteita, virheenkäsittelyä ja tarvittavaa erityislogiikkaa.
    * **Esimerkki keskustelunaloitus (Copilot Chat):**
        ```
        @workspace
        Let's plan the implementation for the 'Silliness Scoring Algorithm' feature from our backlog (see #file:docs/specifications/BACKLOG.md).
        The core requirements for scoring are in the main project #file:README.md.
        What would be the key functions or steps involved in implementing this scoring logic in [our chosen language/framework]?
        How should we handle the different scoring rules (base score, briefcase, hopping, twirls, originality)?
        What about input validation for the data used in scoring?
        ```
2.  **Muodosta tehtävänmäärittely:** Tämän Copilot Chatin/Editsin kanssa käydyn keskustelun ja interaktiivisen muokkauksen **tuloksena** tulisi olla uusi tai päivitetty tehtäväkohtainen dokumentti (esim. `docs/tasks/IMPLEMENT_SCORING_ALGORITHM.md`). Tämä dokumentti kokoaa sovitut yksityiskohdat: tavoitteen, kohdemoduulit, erityiset funktiot, logiikan vaiheet, hyväksymiskriteerit jne.
3.  **Delegoi Agent-tilalle:** Kun sinulla on tämä selkeä ja yksityiskohtainen tehtävänmäärittelydokumentti, voit luotettavammin ohjeistaa Copilot Agent-tilaa sen toteuttamiseen viitaten sekä tähän tehtävänmäärittelyyn että yleiseen `agent_workflow.md`-tiedostoon.

Tämä prosessi varmistaa, että te (kehittäjät) pysytte suunnittelun ohjaksissa, käyttäen Copilotia sparrauskumppanina ja luonnosteluapuna, ennen kuin annatte hyvin määritellyn ohjeistuksen automaattisempaan koodin generointiin.

**Dokumenttityypit Copilotin ohjaamiseen:**

1.  **Yleinen agentin työnkulku (`docs/instructions/agent_workflow.md`):**
    Tämä tiedosto määrittelee Copilot Agentin *standardoidun toimintatavan*, kun sitä pyydetään toteuttamaan mikä tahansa tehtävä. Luot tämän kerran. Se kertoo Copilotille, *miten* sen tulisi yleisesti lähestyä työtään. (Tärkeää: Tämä sisältää nyt vaiheen OpenAPI-dokumentaation päivittämisestä.)

2.  **Tehtäväkohtaiset dokumentit (esim. `docs/tasks/TEHTÄVÄN_NIMI.md`):**
    Jokaista merkittävää ominaisuutta `BACKLOG.md`-listaltasi varten luodaan pieni markdown-tiedosto yllä kuvatulla yhteistyöprosessilla. Tämä tiedosto kuvaa yksityiskohtaisesti kyseisen tehtävän *erityisvaatimukset* ja ohjeistaa Copilotia noudattamaan yleistä työnkulkua.

**Esimerkki 1: Yleinen agentin työnkulku -tiedosto (OpenAPI-päivityksellä)**
* **Sijainti:** `docs/instructions/agent_workflow.md`
* **Sisältö:**
    ```markdown
    ## Agent Mode - General Implementation Workflow

    This document outlines the standard operational procedure for GitHub Copilot Agent when tasked with implementing features or modules for this project.

    1.  **Understand Task & Context:**
        * Review specific task requirements (from prompt or #file:docs/tasks/YOUR_TASK_FILE.md).
        * Refer to #file:docs/specifications/PROJECT_SPEC.md (architecture, tech stack, MVP goals).
        * Refer to #file:.github/copilot-instructions.md (global conventions, data context).
        * **Crucially, be aware of the OpenAPI specification requirements (#file:README.md Section 8) and Security Robustness requirements (#file:README.md Section 7).**
    2.  **Assessment & Planning:**
        * Assess existing code for reusability/conflicts. Note dependencies.
    3.  **Adherence to Specifications:** Implement *only* described features.
    4.  **Deviation Protocol:** If deviation is strongly beneficial: state proposal, justify, **ask for permission before implementing.**
    5.  **Code Implementation:** Write clear, concise, well-commented, secure code per task requirements and style guides.
    6.  **Post-Implementation Quality Checks (Simulated for Workshop):**
        * **(Linting):** Assume code is linted/formatted. Aim for passing code.
        * **(Testing):** Assume unit tests are run. Aim for passing code.
        * **(Fixes):** Attempt to fix simulated errors.
    7.  **OpenAPI Specification Update:**
        * Analyze the changes implemented in this task (e.g., by reviewing a conceptual `git diff` of modified code files relevant to API definitions).
        * If any API endpoints (routes, request/response schemas, parameters, authentication methods) were added, modified, or removed:
            * Update the project's OpenAPI specification file (e.g., #file:docs/api/openapi.yaml or as defined in #file:docs/specifications/PROJECT_SPEC.md).
            * Ensure the OpenAPI documentation accurately reflects the current state of the API, adhering to the guidelines in the project #file:README.md (Section 8).
            * If tools are used to auto-generate the OpenAPI spec from code (e.g., from annotations), state that these tools would be run or annotations must be updated.
    8.  **Output:** Provide complete code for module(s)/functions. Indicate changes to existing files. State if OpenAPI spec was (or would need to be) updated.
    9.  **Git Commit (Simulated for Workshop):**
        * Indicate a simulated commit message (e.g., "feat: Implement /applications POST endpoint and update OpenAPI spec"). Max 160 chars.
    ```

**Esimerkki 2: Tehtäväkohtainen dokumentti Silly Walks Orchestratorille**
* **Sijainti (esimerkki):** `docs/tasks/IMPLEMENT_POST_APPLICATIONS_ENDPOINT.md`
* **Sisältö:**
    ```markdown
    ## Task: Implement POST /applications Endpoint

    **Workflow Reference:** When implementing this task, adhere to the general procedure outlined in #file:docs/instructions/agent_workflow.md. **Pay special attention to the OpenAPI Specification Update step.**

    **Project Specification Reference:** #file:docs/specifications/PROJECT_SPEC.md
    **README.md References:** Section 2 (Business Requirements, esp. #1, #2, #7), Section 8 (OpenAPI). (These refer to sections in #file:README.md)
    **Target Module(s):** [e.g., `src/routes/application_routes.js` and `src/controllers/application_controller.js`, or equivalent for chosen stack]
    **Assigned Role:** Backend API Developer with a focus on security and documentation.
    **Goal:** Implement the `POST /applications` endpoint to allow submission of new silly walk grant applications, including input validation, API key authentication, silliness scoring, data persistence, and ensuring the OpenAPI spec is updated.

    ---
    **Specific Requirements & Acceptance Criteria for this Task:**

    1.  **Endpoint Definition:** Create a `POST` endpoint at `/applications`.
    2.  **API Key Authentication:** Implement API key check (from HTTP header) as per #file:README.md Section 7. Reject if invalid/missing.
    3.  **Input Validation:** Rigorously validate the JSON request body against #file:README.md Requirement #1 (fields: `applicant_name`, `walk_name`, etc.) and Requirement #2 (security focus on validation). Return HTTP 400 for invalid data.
    4.  **Silliness Scoring:** If validation passes, calculate the silliness score using the logic from #file:README.md Requirement #3.
    5.  **Data Persistence:** Store the validated application data, generated UUID, calculated score, initial status ("PendingReview"), and submission timestamp. Use parameterized queries/ORM if SQL.
    6.  **Response:** On successful creation (HTTP 201), return the created application object including its new ID and silliness score. On error, return appropriate HTTP status and non-revealing error message.
    7.  **OpenAPI Documentation:** Ensure this new endpoint, its request body, responses (success and error), and security requirements (API key) are accurately documented in the project's OpenAPI specification file (e.g., #file:docs/api/openapi.yaml).
    8.  **Security:** Adhere to all relevant security principles from #file:README.md Section 7.
    ```

### 3.4. Oman tietoturva-auditointiagentin työnkulun rakentaminen (Tiimitehtävä - Noin 10 minuuttia tästä vaiheesta)

Ennen kuin syvennytään ominaisuuksien toteutukseen, tiimisi määrittelee työnkulun "Tietoturva-auditointiagentille". Tämä tarkoittaa ohjetiedoston luomista, joka ohjaa Copilotia toimimaan koodisi tietoturva-auditoijana.

* **Luo tiedosto:** `docs/instructions/security_audit_workflow.md`
* **Tavoite:** Tämä dokumentti kertoo Copilotille, miten tarkastella koodimuutoksia tai olemassa olevaa koodia tietoturvahaavoittuvuuksien varalta.
* **Ohjeistus sisällölle (Käytä Copilot Chatia apuna tämän luonnostelussa!):**
    * **Rooli:** Määrittele Copilotin rooli (esim. "Olet huolellinen Tietoturva-auditoija...").
    * **Tietopohja:** Ohjeista agenttia perustamaan auditointinsa:
        * Projektin `#file:README.md`-tiedoston "Turvallisuuden kestävyys" -vaatimuksiin (Osa 7).
        * **Aivoriihi Copilotin kanssa:** Kysy Copilot Chatilta: "Mitkä ovat yleisiä taustajärjestelmän API-turvallisuushaavoittuvuuksia 'The Silly Walk Grant Application Orchestrator' -tyyppisessä projektissa, joka käyttää [valitsemaanne teknologiakokonaisuutta, esim. Node.js/Express]? Listaa 3-5 lisätarkistusta `#file:README.md`-tiedostomme vaatimusten ulkopuolelta." Sisällytä nämä auditoijan tietopohjaan. (Esimerkkejä: Turvattomat suorat objektiviittaukset (IDOR), massamäärittely (Mass Assignment), arkaluonteisen datan paljastuminen lokeissa/vastauksissa).
    * **Auditoija-agentin työnkulku:**
        1.  Syöte: Määrittele, että agentille annetaan koodia (esim. `git diff`, tiedostopolkuja käyttäen `#file:TIEDOSTOPOLKU`, tai koodivalinta).
        2.  Tarkasteluprosessi: Käy läpi annettu koodi.
        3.  Arviointi: Vertaa koodia määriteltyihin tietoturvakriteereihin (`#file:README.md`:sta ja aivoriihessä tunnistetuista kohdista).
        4.  Raportointimuoto: Jokaisesta tunnistetusta mahdollisesta ongelmasta generoi raporttikohta kiinteässä muodossa:
            * `Löydös:` (Selkeä kuvaus mahdollisesta haavoittuvuudesta).
            * `Sijainti:` (Tiedostopolku ja rivinumerot tarvittaessa).
            * `Vakavuusaste:` (Määritä taso: esim. Kriittinen, Korkea, Keskitaso, Matala, Informatiivinen).
            * `Todiste/Perustelu:` (Miksi tämä on potentiaalinen ongelma).
            * `Ehdotettu korjaustoimenpide:` (Konkreettiset askeleet ongelman korjaamiseksi tai lieventämiseksi).
        5.  Tuloste: Koosta kaikki löydökset "Tietoturva-auditointiraportti"-markdown-osioon. Jos ongelmia ei löydy, totea se.
* **Tehtävänne:** Luonnostelkaa yhteistyössä sisältö `docs/instructions/security_audit_workflow.md`-tiedostolle näiden ohjeiden mukaisesti.

---

## 4. Vaihe 3: Iteratiivinen toteutus Copilotin kanssa (Noin 40-50 minuuttia)

Nyt on aika muuttaa suunnitelmat ja määrittelyt koodiksi.

### 4.1. Toteuta perusrunko
Käynnistä toteutus Copilot Chatin avulla viitaten dokumentaatioosi.
* **Esimerkkikehote (Copilot Chat, ohjaten Copilot Agent-tilaa tai kattavaa chat-vuorovaikutusta):**
    ```
    @workspace
    I need you to implement the `POST /applications` endpoint for 'The Silly Walk Grant Application Orchestrator'.

    **Task Specification:** The detailed requirements are in:
    #file:docs/tasks/IMPLEMENT_POST_APPLICATIONS_ENDPOINT.md

    **Implementation Workflow:** The general instructions on how you should approach implementation are in:
    #file:docs/instructions/agent_workflow.md

    Please proceed with the full task as described in #file:docs/tasks/IMPLEMENT_POST_APPLICATIONS_ENDPOINT.md, ensuring you strictly follow the general workflow outlined in #file:docs/instructions/agent_workflow.md, especially the OpenAPI update step.
    ```

### 4.2. Työstä backlogia ja suorita tietoturva-auditointeja
Käsittele kohteet `#file:docs/specifications/BACKLOG.md`-tiedostostasi. Jokaiselle merkittävälle ominaisuudelle:

1.  **Laadi tehtävänmäärittely yhteistyössä:** Ennen uuden ominaisuuden toteutuksen aloittamista, luo uusi tehtäväkohtainen dokumentti `docs/tasks/`-kansioon (esim. `IMPLEMENT_GET_APPLICATIONS_ENDPOINT.md`).
    * **Käytä Copilot Chatia (hyödyntäen Kysy/Muokkaa-ominaisuuksia kuten `@workspace`, `#file`, `#selection`) sparrauskumppanina tämän uuden tehtävädokumentin sisällön määrittelemisessä.** Keskustele ominaisuuden tavoitteesta, keskeisistä tarvittavista funktioista, syötteistä, tulosteista, virhetilanteista ja mahdollisista reunaehdoista Copilotin kanssa. Iteroi näitä yksityiskohtia chat-keskustelussa.
    * Tämän interaktiivisen keskustelun ja muokkausistunnon **tuloksena** Copilotin kanssa tulisi olla hyvin määritelty tehtävänmäärittely uudessa markdown-tiedostossasi. Tämä dokumentoi tiimisi suunnittelupäätökset ja Copilotin panoksen.

2.  **Viimeistele tehtävädokumentin rakenne:** Varmista, että uusi tehtävädokumenttisi (esim. `IMPLEMENT_GET_APPLICATIONS_ENDPOINT.md`):
    * Viittaa yleiseen agentin työnkulkuun: `**Workflow Reference:** When implementing this task, adhere to the general procedure outlined in #file:docs/instructions/agent_workflow.md.`
    * Kuvaa selkeästi kaikki *kyseisen ominaisuuden* erityisvaatimukset, syötteet, tulosteet ja hyväksymiskriteerit.

3.  **Toteuta Copilotin avulla:** Kun tehtävädokumentti on valmis, käytä Copilot Chatia ( `@workspace`:n kanssa ja viitaten uuteen tehtävädokumenttiisi) tai Copilot Agent-tilaa tehtävän toteuttamiseen, kuten osion 4.1 esimerkissä on esitetty.

4.  **Suorita tietoturva-auditointi:** Toteutuksen ja perustason toiminnallisen testauksen jälkeen:
    * Käytä `#file:docs/instructions/security_audit_workflow.md`-tiedostoasi ohjeistaaksesi Copilotia auditoimaan uuden/muutetun koodin.
    * **Esimerkki auditointikehote (Copilot Chat):**
        ```
        @workspace
        Please perform a security audit on the code recently implemented for the [feature name, e.g., 'GET /applications/{id} endpoint'] located in [#file:PATH_TO_YOUR_CODE_FILE(s)].
        Follow the audit process defined in:
        #file:docs/instructions/security_audit_workflow.md
        And use the security requirements from Section 7 of the main project #file:README.md.
        Generate the Security Audit Report.
        ```
5.  Tarkastele auditointiraporttia ja keskustele löydöksistä Copilotin kanssa tarvittaessa korjausehdotuksista.

### 4.3. Koodin testaus
Varmenna toiminnallisuus ja turvallisuus.
* **Esimerkkikehote (Copilot Chat API-testien kirjoittamiseen):**
    ```
    @workspace
    For the `POST /applications` endpoint (defined in #file:docs/api/openapi.yaml and implemented in [#file:YOUR_RELEVANT_CODE_FILE]), help me write integration tests using [your chosen testing framework, e.g., Jest with Supertest for Node.js, or Pytest for FastAPI].
    Tests should cover:
    1. Successful application submission with a valid API key and data. (Expected: 201 Created)
    2. Attempted submission with an invalid/missing API key. (Expected: 401 Unauthorized or 403 Forbidden)
    3. Attempted submission with invalid input data (e.g., missing required field). (Expected: 400 Bad Request)
    ```

### 4.4. Katselmoi, refaktoroi, committaa -sykli
Katselmoi kriittisesti, refaktoroi selkeyden/turvallisuuden/suorituskyvyn parantamiseksi ja committaa toimivat muutokset usein.

## 5. Vaihe 4: Yhteenveto ja esityksen valmistelu (Noin 15 minuuttia)

* Viimeistele MVP-ominaisuudet `#file:docs/specifications/BACKLOG.md`-tiedostosi mukaisesti.
* Varmista, että API toimii ja OpenAPI-määrittely on ajan tasalla.
* Valmistele lyhyt esittely, mukaan lukien OpenAPI-dokumentaation esittely ja maininta tietoturva-auditointiprosessista.

## 6. Keskeiset opit: Tekoäly-yhteistyön työnkulku (Noin 5 minuuttia)

* **Dokumentaatio koodina tekoälylle:** Strukturoitu dokumentaatio (`PROJECT_SPEC.md`, `agent_workflow.md`, tehtävätiedostot, `copilot-instructions.md`) on välttämätöntä edistyneiden tekoälytoimintojen tehokkaaseen ohjaamiseen.
* **Turvallisuus ensin -ajattelu:** Tietoturvanäkökohtien (ja jopa automatisoitujen auditointikehotteiden) integrointi alusta alkaen on ratkaisevan tärkeää taustajärjestelmien kehityksessä.
* **API-dokumentaatio on avainasemassa:** OpenAPI (tai vastaavien) määrittelyjen pitäminen täsmällisinä ja ajan tasalla on elintärkeä taustakehityksen käytäntö. Tämän osittainen automatisointi tekoälyn avulla on arvokas taito.
* **Iteratiivinen kehitys:** Suunnittele, ohjeista tekoälyä, toteuta, testaa, auditoi, katselmoi, refaktoroi ja committaa on tehokas kehityssykli.