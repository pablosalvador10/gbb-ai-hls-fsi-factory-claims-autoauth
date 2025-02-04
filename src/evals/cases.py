import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)  # Base directory of the script

cases = {
    "TEST-001-a": {
        "uploaded_files": os.path.join(BASE_DIR, "utils", "data", "cases", "001", "a"),
        "expected_output": {
            "ocr_ner_results": {
                "patient_info": {
                    "patient_name": "Sarah Sample",
                    "patient_date_of_birth": "10/19/2014",
                    "patient_id": "4567890",
                    "patient_address": "25 W Randolph St, Chicago, IL, 60601",
                    "patient_phone_number": "555-123-4567",
                },
                "physician_info": {
                    "physician_name": "Shiva Pedram, MD",
                    "specialty": "Pediatric Gastroenterology",
                    "physician_contact": {
                        "office_phone": "555-991-2750",
                        "fax": "555-786-5643",
                        "office_address": "5721 S Maryland Ave, Chicago, IL 60637",
                    },
                },
                "clinical_info": {
                    "diagnosis": "Crohn's Disease; Anemia 2/2 blood loss",
                    "icd_10_code": "K50.90; D50.9",
                    "prior_treatments_and_results": "Methylprednisolone 40mg daily; Patient continued to have bloody stools and abdominal pain with no improvement",
                    "specific_drugs_taken_and_failures": "Methylprednisolone 40mg daily; Patient continued to have bloody stools and abdominal pain with no improvement",
                    "alternative_drugs_required": "Not provided",
                    "relevant_lab_results_or_imaging": "Hemoglobin: 9.0 g/dL (11.5 - 15.5 g/dL); Hematocrit: 32% (34.5% - 44.5%); Red Blood Cells (RBC): 3.5 million/µL (4.0 - 5.5 million/µL); Mean Corpuscular Volume (MCV): 78 fL (80 - 100 fL); Mean Corpuscular Hemoglobin (MCH): 28 pg (27 - 31 pg); Mean Corpuscular Hemoglobin Concentration (MCHC): 34 g/dL (32 - 36 g/dL); Platelets: 450,000 cells/µL (150,000 - 400,000 cells/µL); White Blood Cells (WBC): 12,000 cells/µL (4,500 - 13,500 cells/µL); Bands (Immature Neutrophils): 5% (0 - 5%); Neutrophils: 75% (40 - 70%); Lymphocytes: 18% (20 - 50%); Monocytes: 4% (2 - 8%); Eosinophils: 1% (0 - 5%); Basophils: 0% (0 - 1%); Glucose: 90 mg/dL (70 - 100 mg/dL); BUN: 15 mg/dL (7 - 20 mg/dL); Creatinine: 0.5 mg/dL (0.3 - 0.7 mg/dL); Sodium: 138 mEq/L (135 - 145 mEq/L); Potassium: 4.0 mEq/L (3.5 - 5.0 mEq/L); Chloride: 102 mEq/L (98 - 107 mEq/L); Bicarbonate: 24 mEq/L (22 - 30 mEq/L); Calcium: 9.2 mg/dL (8.5 - 10.5 mg/dL); ESR: 30 mm/h (<20 mm/h); CRP: 25 mg/L (<5 mg/L); Fecal Calprotectin: 150 µg/g (<50 µg/g); Fecal Occult Blood: Positive (Negative); AST: 25 U/L (10 - 40 U/L); ALT: 22 U/L (7 - 56 U/L); ALP: 120 U/L (40 - 150 U/L); Bilirubin (Total): 0.6 mg/dL (0.1 - 1.2 mg/dL); Ferritin: 15 ng/mL (12 - 150 ng/mL); Iron: 40 µg/dL (50 - 150 µg/dL); Total Iron Binding Capacity (TIBC): 450 µg/dL (250 - 450 µg/dL); Folate Level: 5 ng/mL (4 - 20 ng/mL); Vitamin B12 Level: 300 pg/mL (200 - 900 pg/mL); EGD Findings: Biopsies obtained and pending; Esophagus: Normal appearance; Stomach: Gastritis, erythema present; Duodenum: Mild to moderate duodenitis with edema; Colonoscopy Findings: Biopsies obtained and pending; Ileum: Patchy inflammation with areas of erythema and ulceration. Segmental strictures observed; Colon: Diffuse inflammation with cobblestone appearance. Multiple aphthous ulcers noted throughout the colon with areas of normal mucosa between inflamed portions. Granularity and friability present; Rectum: Mild inflammation; no significant ulceration; MRI enterography: pending",
                    "symptom_severity_and_impact": "Patient has multiple episodes of abdominal cramping and bowel movements with visible hematochezia; Patient appears pale, tired but interactive; Positive for fatigue, pallor, abdominal pain, hematochezia, dizziness, blood loss (by rectum); Mild tachycardia present",
                    "prognosis_and_risk_if_not_approved": "Patient continues to have frequent blood in stools and anemia as well as abdominal discomfort despite current steroid therapy",
                    "clinical_rationale_for_urgency": "Urgent (In checking this box, I attest to the fact that applying the standard review time frame may seriously jeopardize the customer's life, health, or ability to regain maximum function)",
                    "treatment_request": {
                        "name_of_medication_or_procedure": "Adalimumab",
                        "code_of_medication_or_procedure": "Not provided",
                        "dosage": "160 mg (given as four 40 mg injections on day 1) followed by 80 mg (given as two 40 mg injections) two weeks later. 40mg every other week starting 2 weeks from 2nd dose",
                        "duration": "6 months",
                        "rationale": "Patient will likely need to initiate biologic therapy given severity of symptoms despite current therapy",
                        "presumed_eligibility": "Not provided",
                    },
                },
            },
        },
    },
    "TEST-001-b": {
        "uploaded_files": os.path.join(BASE_DIR, "utils", "data", "cases", "001", "b"),
        "expected_output": {
            "ocr_ner_results": {
                "patient_info": {
                    "patient_name": "Sarah Sample",
                    "patient_date_of_birth": "10/19/2014",
                    "patient_id": "4567890",
                    "patient_address": "28 W Comet Ave, Chicago, IL 60607",
                    "patient_phone_number": "555-123-4567",
                },
                "physician_info": {
                    "physician_name": "Shiva Pedram, MD",
                    "specialty": "Pediatrics",
                    "physician_contact": {
                        "office_phone": "555-991-2750",
                        "fax": "555-786-5643",
                        "office_address": "5721 S Maryland Ave, Chicago, IL 60637",
                    },
                },
                "clinical_info": {
                    "diagnosis": "Crohn's Disease; Anemia 2/2 blood loss",
                    "icd_10_code": "K50.90; D50.9",
                    "prior_treatments_and_results": "Not provided",
                    "specific_drugs_taken_and_failures": "Not provided",
                    "alternative_drugs_required": "Not provided",
                    "relevant_lab_results_or_imaging": "Hemoglobin: 9.0 g/dL (11.5 - 15.5 g/dL); Hematocrit: 32% (34.5% - 44.5%); Red Blood Cells (RBC): 3.5 million/µL (4.0 - 5.5 million/µL); Mean Corpuscular Volume (MCV): 78 fL (80 - 100 fL); Mean Corpuscular Hemoglobin (MCH): 28 pg (27 - 31 pg); Mean Corpuscular Hemoglobin Concentration (MCHC): 34 g/dL (32 - 36 g/dL); Platelets: 450,000 cells/µL (150,000 - 400,000 cells/µL); White Blood Cells (WBC): 12,000 cells/µL (4,500 - 13,500 cells/µL); Bands (Immature Neutrophils): 5% (0 - 5%); Neutrophils: 75% (40 - 70%); Lymphocytes: 18% (20 - 50%); Monocytes: 4% (2 - 8%); Eosinophils: 1% (0 - 5%); Basophils: 0% (0 - 1%); Glucose: 90 mg/dL (70 - 100 mg/dL); BUN: 15 mg/dL (7 - 20 mg/dL); Creatinine: 0.5 mg/dL (0.3 - 0.7 mg/dL); Sodium: 138 mEq/L (135 - 145 mEq/L); Potassium: 4.0 mEq/L (3.5 - 5.0 mEq/L); Chloride: 102 mEq/L (98 - 107 mEq/L); Bicarbonate: 24 mEq/L (22 - 30 mEq/L); Calcium: 9.2 mg/dL (8.5 - 10.5 mg/dL); ESR: 15 mm/h (<20 mm/h); CRP: 12 mg/L (<5 mg/L); Fecal Calprotectin: 100 µg/g (<50 µg/g); Fecal Occult Blood: Positive (Negative); AST: 25 U/L (10 - 40 U/L); ALT: 22 U/L (7 - 56 U/L); ALP: 120 U/L (40 - 150 U/L); Bilirubin (Total): 0.6 mg/dL (0.1 - 1.2 mg/dL); Ferritin: 15 ng/mL (12 - 150 ng/mL); Iron: 40 µg/dL (50 - 150 µg/dL); Total Iron Binding Capacity (TIBC): 450 µg/dL (250 - 450 µg/dL); Folate Level: 5 ng/mL (4 - 20 ng/mL); Vitamin B12 Level: 300 pg/mL (200 - 900 pg/mL); EGD Findings: Biopsies obtained and pending; Esophagus: Normal appearance; Stomach: Gastritis, erythema present; Duodenum: Mild to moderate duodenitis with edema; Colonoscopy Findings: Biopsies obtained and pending; Ileum: Patchy inflammation with areas of erythema and ulceration; Colon: Diffuse inflammation. Granularity and friability present; Rectum: Mild inflammation; no significant ulceration; MRI enterography: pending",
                    "symptom_severity_and_impact": "Patient has multiple episodes of abdominal cramping and bowel movements with visible hematochezia; Patient appears pale, tired but interactive; Positive for fatigue, pallor, abdominal pain, hematochezia, dizziness, blood loss (by rectum); HR 110 bpm; BP 110/70 mmHg; RR: 20 bpm; Temp: 98.6°F (37°C); Mild tachycardia present; Pallor present",
                    "prognosis_and_risk_if_not_approved": "Continues to have frequent blood in stools and anemia as well as abdominal discomfort",
                    "clinical_rationale_for_urgency": "Urgent (In checking this box, I attest to the fact that applying the standard review time frame may seriously jeopardize the customer's life, health, or ability to regain maximum function)",
                    "treatment_request": {
                        "name_of_medication_or_procedure": "Adalimumab",
                        "code_of_medication_or_procedure": "Not provided",
                        "dosage": "160 mg (given as four 40 mg injections on day 1) followed by 80 mg (given as two 40 mg injections) two weeks later. 40 mg every other week starting 2 weeks from 2nd dose.",
                        "duration": "6 months; 16 injections",
                        "rationale": "Patient will likely need to initiate biologic therapy given severity of symptoms",
                        "presumed_eligibility": "Not provided",
                    },
                },
            },
        },
    },
    "TEST-002-a": {
        "uploaded_files": os.path.join(BASE_DIR, "utils", "data", "cases", "002", "a"),
        "expected_output": {
            "ocr_ner_results": {
                "patient_info": {
                    "patient_name": "Maxie Millionaire",
                    "patient_date_of_birth": "06/15/2022",
                    "patient_id": "7656432",
                    "patient_address": "14126 Garnett St, Boston, MA, 02108",
                    "patient_phone_number": "555-987-2254",
                },
                "physician_info": {
                    "physician_name": "Dr. Lennox",
                    "specialty": "Pediatrics",
                    "physician_contact": {
                        "office_phone": "(555) 345-7865",
                        "fax": "(555) 345-7866",
                        "office_address": "84 North Avenue, Boston, MA 02108",
                    },
                },
                "clinical_info": {
                    "diagnosis": "Lennox-Gastaut Syndrome; Infantile Spasms",
                    "icd_10_code": "G40.811; G40.821",
                    "prior_treatments_and_results": "Valproic Acid: 4 weeks, failed; Lamotrigine: current therapy, failed; Rufinamide: 8 weeks, failed; Topiramate: current therapy, failed",
                    "specific_drugs_taken_and_failures": "Valproic Acid: 4 weeks, failed; Lamotrigine: current therapy, failed; Rufinamide: 8 weeks, failed; Topiramate: current therapy, failed",
                    "alternative_drugs_required": "Not provided",
                    "relevant_lab_results_or_imaging": "EEG: Slow spike-and-wave discharges, generalized background slowing, infantile spasms, potential atonic seizures; MRI Brain: Mild cortical atrophy, otherwise unremarkable; CBC: WBC 6.5 x 10^9/L, Hemoglobin 11.5 g/dL, Hematocrit 34%, MCV 72 fL, MCH 23 pg, MCHC 32 g/dL, Platelet Count 250 x 10^9/L; CMP: Glucose 90 mg/dL, BUN 10 mg/dL, Creatinine 0.5 mg/dL, Sodium 140 mEq/L, Potassium 4.1 mEq/L, Chloride 104 mEq/L, Bicarbonate 24 mEq/L, Calcium 9.0 mg/dL, Total Protein 6.5 g/dL, Albumin 4.0 g/dL, Alkaline Phosphatase 150 U/L, AST 20 U/L, ALT 18 U/L, Bilirubin 0.5 mg/dL",
                    "symptom_severity_and_impact": "Increased seizure frequency, new atonic seizure activity, appears more sleepy, mild hypotonia in upper body, hyperreflexia in upper and lower extremities",
                    "prognosis_and_risk_if_not_approved": "Increased seizure frequency and severity, potential for worsening condition",
                    "clinical_rationale_for_urgency": "Patient's seizures are worse in frequency and more varied in semiology despite trial of several AEDs",
                    "treatment_request": {
                        "name_of_medication_or_procedure": "Epidiolex",
                        "code_of_medication_or_procedure": "Not provided",
                        "dosage": "100 mg/mL, take 2.5mg/kg/day divided in two doses for one week, then increase to 5mg/kg/day divided in two doses",
                        "duration": "Ongoing",
                        "rationale": "Patient's seizures are worse in frequency and more varied in semiology despite trial of several AEDs",
                        "presumed_eligibility": "Yes, patient has tried and failed multiple AEDs",
                    },
                },
            },
        },
    },
}
