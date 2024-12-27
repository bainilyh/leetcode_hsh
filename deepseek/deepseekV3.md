1. Introduction

In recent years, Large Language Models (LLMs) have been undergoing rapid iteration and
evolution (Anthropic, 2024; Google, 2024; OpenAI, 2024a), progressively diminishing the gap towards Artificial General Intelligence (AGI). Beyond closed-source models, open-source models,
including DeepSeek series (DeepSeek-AI, 2024a,b,c; Guo et al., 2024), LLaMA series (AI@Meta,
2024a,b; Touvron et al., 2023a,b), Qwen series (Qwen, 2023, 2024a,b), and Mistral series (Jiang
et al., 2023; Mistral, 2024), are also making significant strides, endeavoring to close the gap with
their closed-source counterparts. To further push the boundaries of open-source model capabilities, we scale up our models and introduce DeepSeek-V3, a large Mixture-of-Experts (MoE)
model with 671B parameters, of which 37B are activated for each token.

1. 引言

近年来，大型语言模型（LLMs）正在快速迭代和演化（Anthropic, 2024; Google, 2024; OpenAI, 2024a），逐步缩小与通用人工智能（AGI）之间的差距。除了闭源模型之外，开源模型也在取得显著进展，包括DeepSeek系列（DeepSeek-AI, 2024a,b,c; Guo et al., 2024）、LLaMA系列（AI@Meta, 2024a,b; Touvron et al., 2023a,b）、Qwen系列（Qwen, 2023, 2024a,b）以及Mistral系列（Jiang et al., 2023; Mistral, 2024），这些模型正努力缩小与闭源模型的差距。为了进一步推动开源模型能力的边界，我们扩大了我们的模型规模，并推出了DeepSeek-V3，这是一种拥有6710亿参数的大型专家混合（MoE）模型，其中每个token激活37亿参数。

With a forward-looking perspective, we consistently strive for strong model performance
and economical costs. Therefore, in terms of architecture, DeepSeek-V3 still adopts Multi-head
Latent Attention (MLA) (DeepSeek-AI, 2024c) for efficient inference and DeepSeekMoE (Dai
et al., 2024) for cost-effective training. These two architectures have been validated in DeepSeekV2 (DeepSeek-AI, 2024c), demonstrating their capability to maintain robust model performance
while achieving efficient training and inference. Beyond the basic architecture, we implement
two additional strategies to further enhance the model capabilities. Firstly, DeepSeek-V3 pioneers an auxiliary-loss-free strategy (Wang et al., 2024a) for load balancing, with the aim of
minimizing the adverse impact on model performance that arises from the effort to encourage
load balancing. Secondly, DeepSeek-V3 employs a multi-token prediction training objective,
which we have observed to enhance the overall performance on evaluation benchmarks.
In order to achieve efficient training, we support the FP8 mixed precision training and
implement comprehensive optimizations for the training framework. Low-precision training
has emerged as a promising solution for efficient training (Dettmers et al., 2022; Kalamkar et al.,
2019; Narang et al., 2017; Peng et al., 2023b), its evolution being closely tied to advancements in
hardware capabilities (Luo et al., 2024; Micikevicius et al., 2022; Rouhani et al., 2023a). In this
work, we introduce an FP8 mixed precision training framework and, for the first time, validate
its effectiveness on an extremely large-scale model. Through the support for FP8 computation
and storage, we achieve both accelerated training and reduced GPU memory usage. As for
the training framework, we design the DualPipe algorithm for efficient pipeline parallelism,
which has fewer pipeline bubbles and hides most of the communication during training through
computation-communication overlap. This overlap ensures that, as the model further scales up,
as long as we maintain a constant computation-to-communication ratio, we can still employ
fine-grained experts across nodes while achieving a near-zero all-to-all communication overhead.
In addition, we also develop efficient cross-node all-to-all communication kernels to fully utilize
InfiniBand (IB) and NVLink bandwidths. Furthermore, we meticulously optimize the memory
footprint, making it possible to train DeepSeek-V3 without using costly tensor parallelism.
Combining these efforts, we achieve high training efficiency.

从前瞻性的角度来看，我们始终致力于实现强大的模型性能和经济的成本。因此，在架构方面，DeepSeek-V3仍然采用多头潜在注意力（MLA）（DeepSeek-AI, 2024c）进行高效推理，并使用DeepSeekMoE（Dai et al., 2024）进行经济高效的训练。这两种架构在DeepSeek-V2（DeepSeek-AI, 2024c）中已被验证，证明了它们在实现高效训练和推理的同时保持稳健模型性能的能力。除了基本架构之外，我们还实施了两种附加策略以进一步增强模型能力。首先，DeepSeek-V3开创了一种无辅助损失策略（Wang et al., 2024a）用于负载均衡，旨在最大限度地减少负载均衡对模型性能的不利影响。其次，DeepSeek-V3采用多token预测训练目标，我们观察到这能提升评估基准上的整体性能。

为了实现高效训练，我们支持FP8混合精度训练，并对训练框架进行了全面优化。低精度训练已成为高效训练的有前途的解决方案（Dettmers et al., 2022; Kalamkar et al., 2019; Narang et al., 2017; Peng et al., 2023b），其演变与硬件能力的进步密切相关（Luo et al., 2024; Micikevicius et al., 2022; Rouhani et al., 2023a）。在这项工作中，我们引入了FP8混合精度训练框架，并首次验证了其在超大规模模型上的有效性。通过支持FP8计算和存储，我们实现了加速训练和减少GPU内存使用。至于训练框架，我们设计了DualPipe算法以实现高效的流水线并行性，减少了流水线气泡，并通过计算-通信重叠隐藏了训练过程中的大部分通信。这种重叠确保了随着模型进一步扩展，只要我们保持恒定的计算与通信比率，就仍然可以在节点间使用细粒度专家，同时实现接近零的全对全通信开销。此外，我们还开发了高效的跨节点全对全通信内核，以充分利用InfiniBand（IB）和NVLink带宽。此外，我们精心优化了内存占用，使得无需使用昂贵的张量并行即可训练DeepSeek-V3。结合这些努力，我们实现了高效的训练。

During pre-training, we train DeepSeek-V3 on 14.8T high-quality and diverse tokens. The
pre-training process is remarkably stable. Throughout the entire training process, we did not
encounter any irrecoverable loss spikes or have to roll back. Next, we conduct a two-stage
context length extension for DeepSeek-V3. In the first stage, the maximum context length is
extended to 32K, and in the second stage, it is further extended to 128K. Following this, we
conduct post-training, including Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL)
on the base model of DeepSeek-V3, to align it with human preferences and further unlock its
potential. During the post-training stage, we distill the reasoning capability from the DeepSeekR1 series of models, and meanwhile carefully maintain the balance between model accuracy and generation length.

在预训练期间，我们在14.8万亿高质量且多样化的tokens上训练DeepSeek-V3。整个预训练过程非常稳定。在整个训练过程中，我们没有遇到任何不可恢复的损失峰值，也不需要回滚。接下来，我们对DeepSeek-V3进行两阶段的上下文长度扩展。在第一阶段，最大上下文长度扩展到32K，在第二阶段，进一步扩展到128K。随后，我们进行后续训练，包括对DeepSeek-V3基础模型的监督微调（SFT）和强化学习（RL），以使其与人类偏好对齐，并进一步释放其潜力。在后续训练阶段，我们从DeepSeekR1系列模型中提取推理能力，同时仔细保持模型准确性和生成长度之间的平衡。

Table 1 | Training costs of DeepSeek-V3, assuming the rental price of H800 is $2 per GPU hour.

表 1 | DeepSeek-V3 的训练成本，假设 H800 的租赁价格为每 GPU 每小时 2 美元。

We evaluate DeepSeek-V3 on a comprehensive array of benchmarks. Despite its economical
training costs, comprehensive evaluations reveal that DeepSeek-V3-Base has emerged as the
strongest open-source base model currently available, especially in code and math. Its chat
version also outperforms other open-source models and achieves performance comparable to
leading closed-source models, including GPT-4o and Claude-3.5-Sonnet, on a series of standard
and open-ended benchmarks.
Lastly, we emphasize again the economical training costs of DeepSeek-V3, summarized in
Table 1, achieved through our optimized co-design of algorithms, frameworks, and hardware.
During the pre-training stage, training DeepSeek-V3 on each trillion tokens requires only 180K
H800 GPU hours, i.e., 3.7 days on our cluster with 2048 H800 GPUs. Consequently, our pretraining stage is completed in less than two months and costs 2664K GPU hours. Combined
with 119K GPU hours for the context length extension and 5K GPU hours for post-training,
DeepSeek-V3 costs only 2.788M GPU hours for its full training. Assuming the rental price of
the H800 GPU is $2 per GPU hour, our total training costs amount to only $5.576M. Note that
the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs
associated with prior research and ablation experiments on architectures, algorithms, or data.

我们在一系列全面的基准测试中评估了DeepSeek-V3。尽管其训练成本经济，但综合评估显示，DeepSeek-V3-Base已成为目前最强的开源基础模型，特别是在代码和数学领域。其聊天版本也优于其他开源模型，并在一系列标准和开放式基准测试中表现出与领先的闭源模型（包括GPT-4o和Claude-3.5-Sonnet）相当的性能。

最后，我们再次强调DeepSeek-V3的经济训练成本，如表1所述，这得益于我们在算法、框架和硬件上的优化协同设计。在预训练阶段，训练DeepSeek-V3每万亿tokens仅需180K H800 GPU小时，即在我们拥有2048个H800 GPU的集群上需时3.7天。因此，我们的预训练阶段在不到两个月的时间内完成，总计耗费2664K GPU小时。结合上下文长度扩展的119K GPU小时和后续训练的5K GPU小时，DeepSeek-V3的完整训练仅需2.788M GPU小时。假设H800 GPU的租赁价格为每小时2美元，我们的总训练成本仅为5.576M美元。请注意，上述成本仅包括DeepSeek-V3的正式训练，不包括在架构、算法或数据上的先前研究和消融实验的成本。