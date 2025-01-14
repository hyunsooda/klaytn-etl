# MIT License
#
# Modifications Copyright (c) klaytn authors
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from blockchainetl.jobs.exporters.composite_item_exporter import CompositeItemExporter

BLOCK_FIELDS_TO_EXPORT = [
    "number",
    "hash",
    "parent_hash",
    "logs_bloom",
    "transactions_root",
    "state_root",
    "receipts_root",
    "size",
    "extra_data",
    # 'gas_limit',  # Does not supported by klay_getBlockWithConsensusInfoByNumber
    "gas_used",
    "timestamp",
    "unix_timestamp",
    "transaction_count",
    "block_score",
    "total_block_score",
    "governance_data",
    "vote_data",
    "committee",
    "proposer",
    "reward_address",
    "base_fee_per_gas",
]

TRANSACTION_FIELDS_TO_EXPORT = [
    "hash",
    "nonce",
    "block_hash",
    "block_number",
    "transaction_index",
    "from_address",
    "to_address",
    "value",
    "gas",
    "gas_price",
    "input",
    # Klaytn additional properties
    "fee_payer",
    "fee_payer_signatures",
    "fee_ratio",
    "sender_tx_hash",
    "signatures",
    "tx_type",
    "tx_type_int",
    "max_priority_fee_per_gas",
    "max_fee_per_gas",
    "access_list",
]


def blocks_and_transactions_item_exporter(blocks_output=None, transactions_output=None):
    return CompositeItemExporter(
        filename_mapping={"block": blocks_output, "transaction": transactions_output},
        field_mapping={
            "block": BLOCK_FIELDS_TO_EXPORT,
            "transaction": TRANSACTION_FIELDS_TO_EXPORT,
        },
    )
