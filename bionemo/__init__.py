# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-Apache2
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pathlib import Path
from typing import Sequence

from nemo.core.optim.lr_scheduler import register_scheduler

from bionemo.utils.scheduler import (
    LinearWarmupHoldDecayParams,
    LinearWarmupHoldDecayPolicy,
)


__all__: Sequence[str] = ("BIONEMO_PY_ROOT",)

# TODO [mgreaves]: Refactor, don't modify global state on bionemo import.
#                  Instead, perform this registration on a per-model-train basis.
register_scheduler(
    "LinearWarmupHoldDecayPolicy",
    LinearWarmupHoldDecayPolicy,
    LinearWarmupHoldDecayParams,
)

BIONEMO_PY_ROOT: Path = Path(__file__).parent
"""The directory containg the bionemo Python package.
"""