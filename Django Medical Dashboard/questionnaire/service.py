from transformers import AutoModelForCausalLM, LlamaTokenizer
from sentence_transformers import SentenceTransformer
from .models import PatientResponse
import pinecone

# bert_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
# pinecone.init(api_key="your-pinecone-api-key", environment="your-environment")

# Initialize a Pinecone index
# index_name = "doctor-specialties"
# index = pinecone.Index(index_name)

# llama_model_name = "lmsys/vicuna-7b-v1.5"
# llama_tokenizer = AutoTokenizer.from_pretrained(llama_model_name)
# llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name)

# def load_vicuna_model():
#     model_name = "TheBloke/vicuna-7B-1.1-HF"  # Replace with the specific Vicuna model variant if needed
#     tokenizer = LlamaTokenizer.from_pretrained(model_name)
#     model = AutoModelForCausalLM.from_pretrained(model_name)
#     return model, tokenizer

# def generate_dynamic_questions(previous_answers):
#     # Load the Vicuna model and tokenizer
#     model, tokenizer = load_vicuna_model()
#     # Create prompt based on previous answers
#     conversation_history = "\n".join(previous_answers)
#     prompt = f"Based on the following responses, suggest three follow-up questions to match with respective doctors:\n{conversation_history}"

#     inputs = tokenizer(prompt, return_tensors="pt")
#      # Generate multiple dynamic questions using Vicuna
#     output = model.generate(
#         inputs['input_ids'],
#         max_length=600,  # Adjust this to control the length of generated questions
#         num_return_sequences=5,  # Number of questions or sequences to generate
#         no_repeat_ngram_size=3,  # Avoid repetition
#         temperature=0.7,  # Adjust creativity
#         do_sample=True  # Sampling for variety
#     )
#     # Decode the output into human-readable text
#     generated_questions = tokenizer.decode(output[0], skip_special_tokens=True)
    
#     return generated_questions.split()

# def embed_patient_responses(session_id):
#     # Fetch all patient responses
#     responses = PatientResponse.objects.filter(attempt_id=session_id)
#     combined_responses = "\n".join([f"Q: {r.question}\nA: {r.answer}" for r in responses])

#     # Embed responses with BERT
#     return bert_model.encode(combined_responses)

# def query_matching_doctors(patient_embedding):
#     # Query Pinecone with the patient's embedding
#     result = index.query(patient_embedding, top_k=3, include_metadata=True)
    
#     # Return matched doctors
#     matched_doctors = [
#         {"name": match['metadata']['name'], "specialty": match['metadata']['specialty'], "score": match['score']}
#         for match in result['matches']
#     ]
    
#     return matched_doctors

# def embed_and_store_doctor_in_pinecone(doctor):
#     # Create embedding for doctor's specialty
#     embedding = bert_model.encode(doctor.specialty)
    
#     # Store embedding in Pinecone with doctor’s metadata
#     index.upsert([(str(doctor.id), embedding.tolist(), {"name": doctor.name, "specialty": doctor.specialty})])

#     # Save the Pinecone ID in the Doctor model
#     doctor.pinecone_id = str(doctor.id)
#     doctor.save()
#     doctor = Doctor.objects.get(id=1)
#     embed_and_store_doctor_in_pinecone(doctor)