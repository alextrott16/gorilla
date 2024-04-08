from collections import defaultdict

from model_handler.gorilla_handler import GorillaHandler
from model_handler.gpt_handler import OpenAIHandler
from model_handler.claude_handler import ClaudeHandler
from model_handler.mistral_handler import MistralHandler
from model_handler.firework_ai_handler import FireworkAIHandler
from model_handler.nexus_handler import NexusHandler
from model_handler.gemini_handler import GeminiHandler
from model_handler.oss_handler import OSSHandler
from model_handler.gemma_handler import GemmaHandler
from model_handler.glaive_handler import GlaiveHandler
from model_handler.deepseek_handler import DeepseekHandler
from model_handler.functionary_handler import FunctionaryHandler
from model_handler.databricks_handler import DatabricksHandler
from model_handler.accelerate_handler import AccelerateHandler

def default_handler_wrapper():
    """The default value of a defaultdict cannot accept parameters (this is
    a feature of Python). So we are unable to make to a Handler class, which
    requires parameters during initialization, the default value of a
    defaultdict. So we use this wrapper, which requires no parameters to get
    around this."""
    return AccelerateHandler

handler_map = defaultdict(default_handler_wrapper)

handler_map.update({
    "gorilla-openfunctions-v0": GorillaHandler,
    "gorilla-openfunctions-v2": GorillaHandler,
    "gpt-4-1106-preview-FC": OpenAIHandler,
    "gpt-4-1106-preview": OpenAIHandler,
    "gpt-4-0125-preview-FC": OpenAIHandler,
    "gpt-4-0125-preview": OpenAIHandler,
    "gpt-4-0613-FC": OpenAIHandler,
    "gpt-4-0613": OpenAIHandler,
    "gpt-3.5-turbo-0125-FC": OpenAIHandler,
    "gpt-3.5-turbo-0125": OpenAIHandler,
    "claude-2.1": ClaudeHandler,
    "claude-instant-1.2": ClaudeHandler,
    "claude-3-opus-20240229": ClaudeHandler,
    "claude-3-opus-20240229-FC": ClaudeHandler,
    "claude-3-sonnet-20240229": ClaudeHandler,
    "claude-3-sonnet-20240229-FC": ClaudeHandler,
    "claude-3-haiku-20240307-FC": ClaudeHandler,
    "mistral-large-2402": MistralHandler,
    "mistral-large-2402-FC-Any": MistralHandler,
    "mistral-large-2402-FC-Auto": MistralHandler,
    "mistral-medium-2312": MistralHandler,
    "mistral-small-2402": MistralHandler,
    "mistral-small-2402-FC-Any": MistralHandler,
    "mistral-small-2402-FC-Auto": MistralHandler,
    "mistral-tiny-2312": MistralHandler,
    "fire-function-v1-FC": FireworkAIHandler,
    "Nexusflow-Raven-v2": NexusHandler,
    "gemini-1.0-pro": GeminiHandler,
    "gemma": OSSHandler,
    "google/gemma-7b-it": GemmaHandler,
    "glaiveai/glaive-function-calling-v1": GlaiveHandler,
    "deepseek-ai/deepseek-coder-6.7b-instruct": DeepseekHandler,
    "meetkai/functionary-small-v2.2-FC": FunctionaryHandler,
    "meetkai/functionary-medium-v2.2-FC": FunctionaryHandler,
    "meetkai/functionary-small-v2.4-FC": FunctionaryHandler,
    "meetkai/functionary-medium-v2.4-FC": FunctionaryHandler,
    "databricks-dbrx-instruct": DatabricksHandler,
})
