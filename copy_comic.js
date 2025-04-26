CryptoJS = require('crypto-js');
dio = "xxxmanga.woo.key"

function decrypt(data) {
    var _0x2e033c = CryptoJS
        , _0x5bf283 = data["substring"](0x0, 0x10)
        , _0x37be9a = data["substring"](0x10, data["length"])
        , _0x3def88 = _0x2e033c["enc"]["Utf8"]["parse"](dio)
        , _0xee2319 = _0x2e033c["enc"]["Utf8"]['parse'](_0x5bf283)
        , _0x2fa5a9 = function (_0x5f5c34) {
            var _0x2f96b7 = _0x2e033c["enc"]["Hex"]["parse"](_0x5f5c34)
            , _0x57ae89 = _0x2e033c["enc"]["Base64"]['stringify'](_0x2f96b7);
            return _0x2e033c["AES"]['decrypt'](_0x57ae89, _0x3def88, {
                'iv': _0xee2319,
                'mode': _0x2e033c['mode']["CBC"],
                'padding': _0x2e033c["pad"]['Pkcs7']
            })["toString"](_0x2e033c['enc']['Utf8'])["toString"]()
    }(_0x37be9a)
    return JSON["parse"](_0x2fa5a9)
}


