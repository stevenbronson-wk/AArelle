from pathlib import PurePath
from tests.integration_tests.validation.conformance_suite_config import ConformanceSuiteConfig

TIMING = {f'esef_conformance_suite_2022/tests/inline_xbrl/{k}': v for k, v in {
    'RTS_Annex_III_Par_3_G3-1-3/index.xml': 4.109,
    'RTS_Art_6_a/index.xml': 6.795,
    'RTS_Annex_IV_Par_6/index.xml': 7.087,
    'G2-4-1_3/index.xml': 7.237,
    'RTS_Annex_II_Par_1_RTS_Annex_IV_par_7/index.xml': 7.343,
    'G3-5-1/index.xml': 7.421,
    'RTS_Annex_IV_Par_4_2/index.xml': 7.7,
    'G3-4-2_3/index.xml': 7.762,
    'G2-4-2_1/index.xml': 7.802,
    'G2-5-3/index.xml': 7.83,
    'G3-4-7/index.xml': 7.832,
    'G2-4-1_2/index.xml': 7.855,
    'G3-4-2_1/index.xml': 7.861,
    'G2-7-1_2/index.xml': 7.875,
    'RTS_Annex_IV_Par_14_G2-5-1/index.xml': 7.884,
    'G2-4-2_2/index.xml': 7.922,
    'G2-7-1_1/index.xml': 7.963,
    'G2-6-2/index.xml': 7.99,
    'G2-5-4_2/index.xml': 8.023,
    'RTS_Annex_IV_Par_4_1/index.xml': 8.063,
    'G3-2-2/index.xml': 8.147,
    'G2-5-4_1/index.xml': 8.293,
    'G3-4-2_2/index.xml': 8.305,
    'G2-5-4_3/index.xml': 8.529,
    'RTS_Annex_IV_Par_1_G2-1-4/index.xml': 8.536,
    'G3-2-3/index.xml': 8.569,
    'G3-4-4/index.xml': 8.718,
    'G3-4-5_1/index.xml': 8.763,
    'RTS_Annex_IV_Par_8_G3-4-5/index.xml': 10.151,
    'RTS_Annex_IV_Par_5/index.xml': 10.481,
    'RTS_Annex_IV_Par_2_G2-1-1/index.xml': 11.47,
    'G2-6-1_1/index.xml': 11.625,
    'G2-6-1_2/index.xml': 11.886,
    'RTS_Annex_IV_Par_11_G3-2-2/index.xml': 11.911,
    'G3-4-6/index.xml': 11.955,
    'G3-1-1_2/index.xml': 11.998,
    'RTS_Art_3/index.xml': 12.226,
    'G2-5-1_3/index.xml': 12.396,
    'G3-4-3_2/index.xml': 12.398,
    'G3-4-3_1/index.xml': 12.521,
    'G2-2-2/index.xml': 12.644,
    'G2-2-1/index.xml': 12.648,
    'RTS_Annex_II_Par_1/index.xml': 12.654,
    'G2-1-3_1/index.xml': 12.657,
    'G3-4-2_4/index.xml': 12.821,
    'G2-1-3_2/index.xml': 12.828,
    'G3-4-5_2/index.xml': 12.907,
    'RTS_Annex_III_Par_1/index.xml': 13.035,
    'G2-3-1_1/index.xml': 13.898,
    'G2-4-1_1/index.xml': 15.855,
    'G2-5-1_2/index.xml': 15.948,
    'G2-2-6_2/index.xml': 15.961,
    'G2-5-1_1/index.xml': 16.026,
    'RTS_Annex_IV_Par_4_G1-1-1_G3-4-5/index.xml': 16.173,
    'G2-5-2/index.xml': 16.174,
    'G2-1-2/index.xml': 20.047,
    'G2-2-6_1/index.xml': 20.552,
    'RTS_Annex_IV_Par_9_Par_10_G1-4-1_G1-4-2_G3-3-1_G3-3-2/index.xml': 22.756,
    'RTS_Annex_IV_Par_12_G2-2-4/index.xml': 23.328,
    'G2-3-1_2/index.xml': 23.504,
    'G3-1-1_1/index.xml': 27.177,
    'G3-1-2/index.xml': 27.707,
    'G2-2-3/index.xml': 28.185,
    'G3-1-5/index.xml': 31.773,
}.items()}

config = ConformanceSuiteConfig(
    approximate_relative_timing=TIMING,
    args=[
        '--disclosureSystem', 'esef-2022',
        '--formula', 'run',
    ],
    expected_failure_ids=frozenset(f'esef_conformance_suite_2022/tests/{s}' for s in [
        # The following test cases fail because of the `tech_duplicated_facts1` formula which fires
        # incorrectly because it does not take into account the language attribute on the fact.
        # A fact can not be a duplicate fact if the language attributes are different.
        'inline_xbrl/RTS_Annex_IV_Par_12_G2-2-4/index.xml:TC5_valid'
    ]),
    file='esef_conformance_suite_2022/index_inline_xbrl.xml',
    info_url='https://www.esma.europa.eu/document/esef-conformance-suite-2022',
    local_filepath='esef_conformance_suite_2022.zip',
    name=PurePath(__file__).stem,
    plugins=frozenset({'validate/ESEF'}),
    public_download_url='https://www.esma.europa.eu/sites/default/files/library/esef_conformance_suite_2022.zip',
    shards=8,
)
