from mypy_extensions import TypedDict
from speclib import array

#https://www.di-mgt.com.au/sha_testvectors.html
#https://csrc.nist.gov/Projects/Cryptographic-Algorithm-Validation-Program/Secure-Hashing

sha3_test = TypedDict('sha3_test', {
    'msg' : str,
    'expected224':  str,
    'expected256' :  str,
    'expected384' :  str,
    'expected512'  : str}
)

sha3_test_vectors : array[sha3_test] = array([
    {
        'msg' : "",
        'expected224' : "6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7",
        'expected256' : "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a",
        'expected384' : "0c63a75b845e4f7d01107d852e4c2485c51a50aaaa94fc61995e71bbee983a2ac3713831264adb47fb6bd1e058d5f004",
        'expected512' : "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26"
    },
    {
        'msg' : "616263",
        'expected224' : "e642824c3f8cf24ad09234ee7d3c766fc9a3a5168d0c94ad73b46fdf",
        'expected256' : "3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532",
        'expected384' : "ec01498288516fc926459f58e2c6ad8df9b473cb0fc08c2596da7cf0e49be4b298d88cea927ac7f539f1edf228376d25",
        'expected512' : "b751850b1a57168a5693cd924b6b096e08f621827444f70d884f5d0240d2712e10e116e9192af3c91a7ec57647e3934057340b4cf408d5a56592f8274eec53f0"
    },
    {
        'msg' : "6162636462636465636465666465666765666768666768696768696a68696a6b696a6b6c6a6b6c6d6b6c6d6e6c6d6e6f6d6e6f706e6f7071",
        'expected224' : "8a24108b154ada21c9fd5574494479ba5c7e7ab76ef264ead0fcce33",
        'expected256' : "41c0dba2a9d6240849100376a8235e2c82e1b9998a999e21db32dd97496d3376",
        'expected384' : "991c665755eb3a4b6bbdfb75c78a492e8c56a22c5c4d7e429bfdbc32b9d4ad5aa04a1f076e62fea19eef51acd0657c22",
        'expected512' : "04a371e84ecfb5b8b77cb48610fca8182dd457ce6f326a0fd3d7ec2f1e91636dee691fbe0c985302ba1b0d8dc78c086346b533b49c030d99a27daf1139d6e75e"
    },
    {
        'msg' : "61626364656667686263646566676869636465666768696a6465666768696a6b65666768696a6b6c666768696a6b6c6d6768696a6b6c6d6e68696a6b6c6d6e6f696a6b6c6d6e6f706a6b6c6d6e6f70716b6c6d6e6f7071726c6d6e6f707172736d6e6f70717273746e6f707172737475",
        'expected224' : "543e6868e1666c1a643630df77367ae5a62a85070a51c14cbf665cbc",
        'expected256' : "916f6061fe879741ca6469b43971dfdb28b1a32dc36cb3254e812be27aad1d18",
        'expected384' : "79407d3b5916b59c3e30b09822974791c313fb9ecc849e406f23592d04f625dc8c709b98b43b3852b337216179aa7fc7",
        'expected512' : "afebb2ef542e6579c50cad06d2e578f9f8dd6881d7dc824d26360feebf18a4fa73e3261122948efcfd492e74e82e2189ed0fb440d187f382270cb455f21dd185"
    }])

shake_test = TypedDict('shake_test', {
    'msg' : str,
    'output':  str}
)

shake128_test_vectors : array[shake_test] = array([
    {
        'msg' : "",
        'output' : "7f9c2ba4e88f827d616045507605853e"
    },
    {
        'msg' : "52977e532bccdb89dfeff7e9e4ad",
        'output' : "fbfba5c1e179df1469fcc8588ae5d2cc"
    },
    {
        'msg' : "4a206a5b8aa3586c0667a40020d65ff511d52b732ef7a0c569f1ee681a4fc3620065",
        'output' : "7bb433752b98f915be5182bc1f096648"
    },
    {
        'msg' : "2469f101c9b499a930a97ef1b34673ec74393fd9faf658e31f06ee0b29a22b623780ba7bdfed8620151cc4444ebe3339e6d2a223bfbfb4ad2ca0e0fa0ddfbbdf3b057a4f26d0b216bc8763ca8d8a35ff2d2d01",
        'output' : "00ff5ef0cd7f8f90ad94b797e9d4dd30"
    },
    {
        'msg' : "bf95025f0caa0f91a785b72e56260bcfdd910d3e7174c4366f0a90694e3fbcc7d31552fe8346333d5e2b663ecadcb183ce9966e080698039c100ee8d27e62f333bd61f64e56511fa24e41d770286bc49c8c6924d6e038a91556d285e39251b7661a0129a184dd14f617784e2e76c53aa33df368d218b0bc59519e6e46a44a816ab3bd3a706469cc57dad42865fd69f2d77adfda983482a5ee8cccf28a38afd9d836e0993959a9ae3e04e006c530bc75afcf88ca87b8410e3b54d8b31cd41439350025c67af8ff231f322659aac54f4b92a878e92f085e4dc6665c308ceafa17e79c0762a3b6fcd371cf01a1a50f94ed36a24a96fcc95cfd262dc1fb3901c",
        'output' : "35bc5753ede5b5908e8093375523d1c4"
    }
])

shake256_test_vectors : array[shake_test] = array([
    {
        'msg' : "",
        'output' : "46b9dd2b0ba88d13233b3feb743eeb243fcd52ea62b81b82b50c27646ed5762f"
    },
    {
        'msg' : "f9da78c890847040454ba6429882b05409",
        'output' : "a84983c9fe75ad0de19e2c8420a7ea85b25102195614dfa5347de60a1ce13b60"
    },
    {
        'msg' : "ef896cdcb363a6159178a1bb1c993946c50402095cdaea4fd4d419aa47321c88",
        'output' : "7abba4e8b8dd766bbabe98f8f169cb6208674de19a51d73c92b7dc04a4b5ee3d"
    },
    {
        'msg' : "de701f10ad3961b0dacc96873a3cd558558188ff696d8501b2e27b67e94190cd0b2548b65b52a922aae89d63d6dd972c91a979eb6343b658f24db34e828b74dbb89a7493a3dfd429fdbdb840ad0b",
        'output' : "642f3f235ac7e3d434063b5fc9215fc3f0e591e2e7fd17668d1a0c87468735c2"
    },
    {
        'msg' : "104fefe89f08d15d36a2233f42a7defa917c5ad2642e06cac56d5cc51ad914ecfb7d984f4199b9cf5fa5a03bf69207b9a353a9681c9cf6437bea0c49d9c3e3db1f3fc76519c70c40cc1dfdd70a9c150943c272cf9eeb861f485f10100c8f4a3e259c6470501932782512225ba64d70b219cf9d5013a21d25d6d65062dcc6b3deb49d58b90d18933f118df70ff42c807ccc851233a34a221eca56b38971ef858475488988794a975d3894633a19c1ae2f05e9b9c0756affd3cfe823ccf29228f60fa7e025bc39a79943325126409460926b057a3fb28a1b098b938872883804fd2bc245d7fd6d29bcda6ca6198f2eff6ea7e03ef78133de8ba65fc8c45a688160719fa1e7646d878ea44c4b5c2e16f48b",
        'output' : "46293a63c235750d58a24edca5ba637b96cae74325c6c8122c4155c0d15805e6"
    }
])
