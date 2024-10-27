from gating_network import GatingNetwork
from expert_model import ExpertModel
import tensorflow as tf
from tensorflow.keras import Model
from typing import List

class MixtureOfExperts(tf.keras.Model):
  def __init__(self, experts: List[Model] , gating_network: GatingNetwork) -> None:
    super().__init__()

    self.experts = experts
    self.gating_network = gating_network

  def call(self, inputs):
    gating_probs = self.gating_network(inputs)
    expert_outputs = [expert(inputs) for expert in self.experts]

    expert_count = len(self.experts)
    output = sum(
      [gating_probs[:, i, tf.newaxis] * expert_outputs[i] for i in range(expert_count)]
    )

    return output
  
  def compile(self, **kwargs):
    # Set default optimizer and loss args
    if 'optimizer' not in kwargs:
        kwargs['optimizer'] = 'adam'
    if 'loss' not in kwargs:
        kwargs['loss'] = 'sparse_categorical_crossentropy'
    if 'metrics' not in kwargs:
        kwargs['metrics'] = ['accuracy']
        
    # Call the parent compile method with updated kwargs
    super(MixtureOfExperts, self).compile(**kwargs)