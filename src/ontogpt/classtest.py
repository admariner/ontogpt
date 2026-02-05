from oaklib.utilities.apikey_manager import get_apikey_value

from ontogpt.clients.llm_client import LLMClient
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.template_loader import get_template_details

model_name = "gpt-4o"

client = LLMClient(
    api_key=get_apikey_value("openai"),
    model=model_name,
    custom_llm_provider="openai",
)

ke = SPIRESEngine(template_details=get_template_details(template="treatment"), client=client)
