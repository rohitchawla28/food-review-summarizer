import transformers
from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM
from transformers import BitsAndBytesConfig

import torch

def model_inference(input):
    prompt_types = ["General: ", "Ambience: ", "Food: ", "Service: "]

    prompts = ["Please provide a one sentence, very short, objective summary for the restaurant based on the provided reviews. Ensure the summary focuses on different aspects as mentioned in the reviews, avoiding repetition and first-person narratives. Please do not include numerical ratings, but rather focus on qualitative descriptions that clearly convey the reviewers experiences and opinions.",

            "Based on the provided reviews, please give a one sentence, very short summary that exclusively focuses on the ambiance aspect of this restaurant. The summary should be objective and reflect only the reviewers' experiences and opinions about the ambiance quality, without including information about the food, service, or any other factors. Please avoid using first-person narratives or numerical ratings, and concentrate solely on qualitative descriptions of the ambience.",

            "Based on the provided reviews, please give a one sentence, very short summary that exclusively focuses on the food aspect of this restaurant. The summary should be objective and reflect only the reviewers' experiences and opinions about the food quality, without including information about the service, ambiance, or any other factors. Please avoid using first-person narratives or numerical ratings, and concentrate solely on qualitative descriptions of the food.",

            "Based on the provided reviews, please give a one sentence, very short summary that exclusively focuses on the service aspect of this restaurant. The summary should be objective and reflect only the reviewers' experiences and opinions about the service quality, without including information about the food, ambiance, or any other factors. Please avoid using first-person narratives or numerical ratings, and concentrate solely on qualitative descriptions of the service."]

    summary = ""
    for prompt_type, prompt in enumerate(prompts):
        input_text = input + " " + prompt

        input_ids = tokenizer.encode(input_text, return_tensors='pt')
        input_ids = input_ids.to('cuda')

        attention_mask = torch.ones(input_ids.shape).to(torch.float16)
        attention_mask = attention_mask.to('cuda')

        with torch.no_grad():
            output = model.generate(input_ids,
                                    attention_mask=attention_mask,
                                    max_length=2048,
                                    do_sample=True,
                                    top_k=10,
                                    num_return_sequences=1,
                                    eos_token_id=tokenizer.eos_token_id)

            output_text = tokenizer.decode(output[0], skip_special_tokens=True)


        output_text = output_text[output_text.find(prompt) + len(prompt):]
        summary += prompt_types[prompt_type] + output_text + "/n"

    return summary