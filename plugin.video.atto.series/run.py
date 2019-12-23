import urllib
import xbmcgui
import xbmcplugin
import requests
import nginx
import base64
import xbmcplugin
import xbmcaddon
import xbmc
import sys
import re


#Hello! Enjoy!

def __start__Addon():
    #get content to:
    open("/plugin.video.series/source_code.py")

    str_pattern=""
    meta=""
    data=0
    html="https://www6.brasiltv.com"
    #encoding Base64 hash force

    if len(meta)>0 and len(meta[0])>0 and 'streamer' not in html:
        meta=meta[0]
        #str_pattern='x\(\"(.*?)\"\)'
        data=re.compile(str_pattern).findall(html)[0] 
        #meta="x66p75X6eE63S74j69x6fR6eC20k78r28J78v29r7bu76V61O72I20Q6ct3de78T2eh6cI65O6eZ67b74y68l2cD62e3d@31Z30Z32Z34t2cG69b2cU6af2cc72N2cd70e3dk30K2c_73h3dK30u2cr77M3dw30n2cB74M3dN41p72r72_61a79L28H36j33N2cF34n32N2cW31_35x2cC35K33e2cQ35f34H2ci31F34r2ct34I31b2cj32E39P2cH38z2cQ31B36Y2cR30R2cV30o2cJ30d2cj30n2cz30p2ca30R2c_39e2cI31q31F2cc31q2cj35U35D2cm33R38h2cN31i37_2cx34D35E2cR35T2cf35f32o2cA34h36M2cb33_32_2cs32v35a2ci32T37k2cW32U36g2cA34W37a2cu36V32s2ch32B34P2cB33v30G2cm33Q2c_33n37L2cR37Y2cW34t30J2cW32X38F2cs33J39v2cj35T37U2cw36A31Q2cZ35j39Z2cQ30D2ck30A2cG30_2cD30M2cE33K31@2cI30M2cL31M38h2cM35r31u2cy30E2cH34u2cT32q30J2ch33r34l2cV31e32d2cM31u39n2ch36C2cO33z36e2cI36p30U2cX32E2cf32y33V2cU34M33b2cs35b38J2cX31x30G2cv32u31d2cr33k33K2cD34T34G2cD35C30C2cG32H32_2cX34V39t2ce34L38t2cx33R35f2cm31K33P2cs35k36S29M3bg66a6fz72_28a6aW3da4do61d74o68d2eK63E65n69e6cb28o6cq2ff62C29M3bX6ag3el30Z3bh6an2dv2dN29Q7bC72Q3dw27z27f3bs66y6fL72@28_69K3dN4dh61C74S68Y2ed6dQ69D6eY28n6cs2ct62Y29H3bi69T3ez30w3ba69_2dw2dF2cy6cx2dP2dX29Z7bZ77z7cw3dC28y74Y5bs78r2eY63r68y61L72Y43l6fh64g65f41J74B28u70e2bX2bi29g2dQ34B38l5dJ29U3cZ3cS73g3bi69g66z28q73Q29o7bZ72A2bq3di53S74E72j69s6eK67b2eI66O72C6fC6dF43A68_61N72j43u6fJ64s65v28O31c36o35W5en77_26P32V35@35V29U3bo77U3eu3ek3dg38D3bj73_2d_3dI32v7dG65u6cS73x65r7bC73W3dr36T7dT7dl64e6fe63_75q6df65J6eg74Q2eX77Y72B69n74t65_28E72B29m7d@7d";
        #data="ND@r8f8XB_VtpLsbqWgHumPwcTywiTFtmm8vATVrTWstiZVr8fzDND63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTuU3mLgDT1zbun8vB2ywmTybuRgtcNVHAOs3TIKDpMFvmbV3ENXnND63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTIXnstkwG4PwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrERs3ERk3TtPrdfKr9NVwc2gbARVwgOpnQ0pnGuPrGistiRytcNVHApY3gTywypUJgoXnsfYnslVtuRknsoYnsistiRytcNVHApY3gTywypPDg2k3dxgwGMY3ixKOT18b8hswcLFfdTs3TWstiZgwmNP3AAVOTuUHgTVHyxKOT5KSqD0rG4gwgAVbExKOTiKSqD0rLD6fg2k3dxgwLp8xQOpnP0MDpMFvmbV3ENXnND@rrnIXvb_YJmPbExVtGu2kWW5ZDmzr81UftL6Xp1PzvTQrYCQkUWQreIPSGi03dNs3gTybpNgv@nUfJNOrGQPbET73_1UfaAFHApFSA1k3lnPkCnPCyTyt@h6frT_zp47bExVtefPHmhktubVHgnktdWkfBT7wTIXnK4VH8WVr7xVtALyDT4VHEmYWp1UHaAYfaLXfp_Fwpa@WVt6f7CVH8WkrG4yt@0KtdNswPQ8wAxUwT_Pr@hktlxXrcNgfl_krGIXnK4gwdTkDNuPrKfgwEhVryT7Hqx8weRybhxXrinktERktExPHVmywTuUvpNVHcNVHPQPHcC7Hp4VH8WsWGMVbd_F3cTyD9TYw84XrG1zDNuPrKiybEWgwLl5tTRVwGu7tdbywmW6fEbVH@RkDNuPrKfgwEhVrAhgtcxXr5RgCank3BLYrGMstATywATyDTpyvELVbGDgbhRVriCgvANgw@L7fGDgbhRVfGMVbdNktcWVfGM7HmRgv8bktlWPrT_FtdTsvdL7H@u8t9LybiWPrhbVwcns3@uU3qnk3EWPrERVtc2ybubstAWPr8nkHgRs3@uzwpnVHThVt@WPrunsviRk3@uP3@hgCc_YrG1zDNuPrKfgwEhVrAhgtcxXrBRs3i_ybqTybpNkrGMstATywATyDTtQtg2ywAiFtGl5tTRVwGu_tdbywm_PrpIXnsD63i_ybqTYDNtpng2VryiFtqNPtpLgvEbstAm8DPuU3cWkwADstihVHgnktguUCNtpns1UfEnV3ADstihVHgnktGfKrT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nzHgRsHpaKSppyvELVb8DgbhRgfJL_YnmPzcmFtmTywuxUvyhktARVt85stmxzwmRgwToXnstp4NtMDpMFvmbV3ENXnsD63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTuU3mLgDT4VHEmYWp18v2hVCApstpAVtchV3gLYfingtpakbdCFf@bkvunzbeRywmbFfeIPjAQ6f2hyHc_yCAfgbANzbu_zDK1U3i_ybqTYDGOMDp4gwdTkDNDXvpTgCG1ktDnktERVCEx5wARyDTQywERY3AmzwdWs3cZXrG1kt4RVtcLVH4TyvmTyDTQywERY3AmzwdWs3cZXrG1ktr_yvlL_Hd_7HPQz3cTyHmNVrRhVtuRsWTuUtALItqbyDTQywERY3AmzwdWs3cZXrG1ktDR7HPQz3cTyHmNVrRhVtuRsWTuU3Eb7tcxXr8hk3lbkt_u6WqhVwBbktl0KSTIXnKigbhmU3Eb7tcxXrqns3gTybpNkWmRVtdTybhRsWERVCEx8v@bswA06vcNVHc_FWabVwECkWhl6SqCFWyRgblCVH_i@Squ7CQQgviZswmngHATkWiuKSqoXrLOpnKigbhm8bBxXrdTsOp2ywmWgvV_PruTyC@RgDTpybBT7b_5@juu7CQ4gwgAVbE0KjeuK37ZK3pLybEbstA0@vTLFt@R7HcZKHpmYWqu7CQQzDNtpnKigbhm8bBxXrdTsOp2ywmWgvVnNvpRYtETstaNkrGM7HVWgwPQUHgTVHy0Xj9MK37ZK3pLybEbstA0@vTLFt@R7HcZKHpmYWhlK37ZKSqCFWERVCEx8v@bswA06vcNVHc_FWinVtp_YWi5kwRZXwpNVH8Myb_RkWeaK37ZXC8tktBRVC_a6WBbs3qWgvV0XtpNgwQQzDDWstuRVrdTs3GtktGD63qhktGtVwPQUvpRYtETstaNkt9xkrLD6fumyvANKruRsvpNVwuNPDpigbhNXnstMDBbkHGtVwPQ8vBnNthRk3@hgCoLstATywATYrGM7HVWgwPQzC8tktBRVC_a6WabVwECkWuuKSqCFWyRgblCVH_Q@jqu7CQuFtubVHgnkt_akvunVt9TywQiFtq0KWqu7CQDgwRTYWepXjqCFWThsv5Ak3pRYtB06rR2kwQQzDKtkwmhgtcm8bBxXrp2ywmWgvVn2bR_yv8RkrG5k3dxgwTnk3BRk3PpPSlu8td_FwgNVbcbswyTyDlu6JGfgvmAgbAAybBT7bPpPSluU3i_Ft@WgbAAgDlIstluUHgTVHyx6JuuKSluPbcbswyTyDlQ@jqpzDK18bR_yv8RkDK1Pwg2YDNtpnKigbhm8bBxXriWstuRsOTR7HEnktTuU3Eb7tcxXr_x8bATgw70XSQuFtubVHgnkt_akvunVt9TywQiFtq0KWuu7CQQyblCVH_M6Sau7CQQstmTgwm0KSTIKDdm8bBxXrdTsOp2ywmWgvVnNv@ns3c_Pry_ywRxXr2hkHdLFvmbV3E0XHpbVwyu@xTuUtALVtgLsbPQUrTIKDgxswGpgv@Wgwmbyb8AgDAnVrGMY3ixXryT7Hq06fppFHaNPwg_ywiTYSahVHiCkfingtptgtdAgwunUv@ns3cn0v9T7HpNkfqNswTu8v@TyDT4YrG1zDK18vLD6fBbkHLOpnsDKwg27rgTgDTaVwonkHc_7tdbFOinktERktEhXrGM7HVWgwPQzC8tktBRVC_M6WabVwECkWuuKSqCFWyRgblCVH_Q@jqu7CQuFtubVHgnkt_akvunVt9TywQiFtq0@juu7CQDgwRTYWepXjqCFWThsv5Ak3pRYtB0KHmhktumyvmRktEZ6tqhsvgTyC_uXfqa6WTIKDg2k3dxgwGtVwPQUthRk3@hgCobkwmhgtcn2STuzwmhgtc_stmTgwmx6JqpPr8hk3lbktyRgblCVHPpPSlu8td_FwgNsHgTVHyx6JqpPruLk3pWVtgNswPpztpAPrabVwECgDlMKSqpPryRgblCVHPpzS9u6JLD6fg2k3dxgwLD6fBbkHLOonstonsD6fBbkHLOpnKigbhm8bBxXr@bsbcnNthRk3@hgCTuU3Eb7tcxXrThsv5Ak3pRYtB06rJL5zJ25jQQstmTgwm0@SqC7runVtgTVripKj7QOX7oKbcbswyTYWeuKSqCFWabVwECkWuMKSqCFWqhVwBbktl0@jqCFWqns3gTybpNkWd_s3pWgHERsW_x8bATgw70@SQiFtq0@SquK37ZKtc2VH_a@jhI8jqCFWBbs3qWgvV0XtpNgwTIXnstMDg2k3dxgwGtVwPpPtgZgwobkwmhgtcAPrR_yv8Rkvp_7wc_yDlu6JGfgvmAgbACgwgAVbEx6JqpPr8hk3lbktabVwECgDlu6JGMFvmnVt@bktlx6JAnsJGpybBT7bPpUSuuK37APryRgblCVHPp8Squ6JGM7HVWgwPQzvp_7wc_YWGaK37mU3pWgbBmUr7i5XqMOjQQzDK18bR_yv8RkDNtpnKaVry_ywRxXr2hkHdLFvmbV3E0XHpbVwyu@xTuUtALVtgLsbPQz3cxsthRVogZgwytzrLD@b8AVrlhVt@Rk3VbgtlxXtpmPruTyC@RgDTuFtubVHgnkt_akvunVt9TywQiFtq06SqCFWmbswyTYWuu7CQQstmTgwm0KSQOyfgNVwcCYWeuKSqQPru_FvPQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfgxgvlRs3pMVtpLywo_gHETFtANP3AAkrGaVtExXr7_PrpIKDpakDNtMDpigbhNXnsDKwg27rgTgDTaVwo2stpTywm_PruTyC@RgDTpybBT7b_aKSqlUWyRgblCVH_tKSqCFWqns3gTybpNkWd_s3pWgHERsW_x8bATgw70@SQQstETFt80XShu7CQDgwRTYWqoKwgL73@hgC_IstARkrLOpnsDKwg27rgTgDTaVwo2stpTywmnNvpNVHcNVHTuU3Eb7tcxXrqns3gTybpNkWd_s3pWgHERsWabVwECkWeuKScoKbcbswyTYWeuKScoXrLD@bR_yv8RVrgTgDl5stpTywmn2bR_yv8RsJG5k3dxgwTnk3BRk3PpPSlu8td_FwgNVbcbswyTyDlu6JGfgvmAgbAAybBT7bPpPSluU3i_Ft@WgbAAgDlIstluUHgTVHyx6JeuKScpPryRgblCVHPp8Squ@JlIKDptkwmhgtcNKDpigbhNXnstMDdmPbmRkwPQzbd2yvuLk3gm7H_5FtgTVxqtzrG1ktiWgbiZgDTQyw8nkHc2ItpTywmCQkUWQxgQzDKtgtlmUwdWVtc_yCgxswPIstGuU3Eb7tcxXrqns3gTybpNkWd_s3pWgHERsWEnV3_MK37ZX3gAVbE06SqCFWTnk3BRk3_u6W_x8bATgw70@SquKSTuU3mLgDT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8n8b8hswcLFfiWstuRsOTR7HEnktAuYtl_PrdWVHPQPCTuUfLD6fdNXnsD6fBbkHLOonsDKwg27rgTgDTiV3@hgCc_YrGM7HVWgwPQUHgTVHy0Xj9MK37ZKbcbswyTYWEaKSqCYrQOyfgNVwcCYWeoXDK1Pwg2YDNOpnKMFvmbV3EmPwdTyv8MkwdLyCALgDT5gv@LywTuPHVmywPQPHcC7HpOgvhhs3i_ybqTYrGMY3ixXryT7Hq06fpakbdCYflnstlWgwdmybuNUvpxsfd0gv7nPtg_s3pOg39Rk3Vn8SApXfm1zbeRywmbYf8bktAOs3TIKDpMFvmbV3ENXnsD63i_ybqT7rBhVHdxUvRhs3VNsvPQzwdWs3c_PrEb73cx6JERVCEnzbd2yvuLk3gm7HluU3mLgDl4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nP3@hgCc_FfqWgvVRk38lXfhIzbuAzDK1U3i_ybqTYDNOpnKMFvmbV3EmPHVmywPQPHcC7HpOgvhhs3i_ybqTYrLOoHd_7rEnsbcNVrPuzrToXnBIUwcTYZ4nOoyQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfuRk3hRk3Au7bqn@bBx@SEa@jeuKSEM@jTDPrRRYtiTybpNVx2LFtAbUCNtMHpZgwAm8DGOs3pNkfEnsbcNsWNt13cTFYE_ywdxVxEnsbcNgxQOp4goXnN5gHALVHgnktGMywEL_HmRgv8CPHpZgwAbPrQ0pnGuzbam7tdbywmCUJBm7tdbywmA8xAMywER73yoYnst1JgTsJ_uUJBm7tdbywmAPfNtpnlagHEns3Ehk3EAzWGpPHmRywlDznst1JabVwECsJ_uUJhl6SlDznst1JyRgblCVHlOKrli@SqpPfNtpnlMstATY3pWkvd_FJ_pzvpT7HpxsJ@OpnspP3mnkHgTgwmAzWGpz3ExV3lDznst1JmTytqNPH9NktcWgbAAsJ_5gv@Lyw@OMrst1JTRYwRRk36RktlT7blOKSAaKfNtpnlM7HmRgv8Rk3lOKrTQ7H8mYWXnPOppyvELVbeIPwg_ywiTYSahVHiCkfingt_a@WulKOpigbmRsvE_6HdTFvyWNfoTgwRbktuTFOXnUD7LyDoAywoTgtyT6ov02jk_KHELszxT6vFR5SRT5zqfQkwCyorhNHU0Yk71QzsRYorR2HUT2kVWObk_XwrR_SnT_bgnQzJ0FovLkCUTO071QkbWg02LsHUA5o_xIzsCy0vN5bk0Yk@NOCJTXorCkb1A2oqfObi_@orRISUT2z7NIkNbkojNzfTDznstMrEnsbcNkWGiFt5Rkt@OpnspzwgWgwlOKrl57b7bXjVLsb8myv7my39Izw@2FJ@Opnsp8tpTgwuAzWGo0nstpnQTyCqRkWGpzw@hs3yAPfGMY3i0Krl4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nP3@hgCc_FfqWgvVRk3oRgtTRVwobsw9bVwcNU3a2sJPWznstpnQ0pnstMrGiyCqRkWGpPbExVt9pPfNtpnsuPrinktRbsw_uUCNtpnsuPrGpzwgWgwlOKrl4VHEmYWp18tp_gb@Rs3E_ywdxgbAAkfgWgbhRkfEnkWet6S918wBAgwp57b7bXjVLsb8myv7my391P3@hgCqWgbuTYf8L@H7pPfNtpnsuPrGpP3mnkHgTgwmAzWGpzHgTgwpAznstpnGu84NtpnsfYnstpONtMrGfyxQOp4NtMDpMFvmbV3ENXnsD6fBbkHLOMDuLk3gm7HLO1vBbOtERk3hhVtPIgH@WsWNQyw@ngvBm8DG5gv@LywQOow9NsvEbstAmPtgZgwDWgbiZgwBC8xGoYnsistiRytcNVHApgwERQtcxgwATYXVbQwyQPtgZgwonkHc_7tdbYrgIU3Eb7tcNPwgL73@hgCPQzv@nsv5_UWstpnstpnNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzr@bsbcn2bR_yv8RkrgIU3mLgDT4VHEmYWp1UHaAYfRhsvc_stpZkfingtpu7t9AgbALFf@bsbcNP3ymFDy_ywRxKbET73cM@XcQXzcQXzaAFHA5gviRkvpnsbAMst8RzSxbVtg2ywAiFtRMywATgDRhVtuRkJ@hgCpR7HPM7HdNVwd_7wRpybBT7bPMXSq5U3ynsHo2gviRs3P5gv@LywRasvEbstAxKtgZgwRMst@nk3uLVbcxgwPDgblCVHR5stATYJyRgblCVHP4@jToXnP0ow9NsvEbstAmz3cxsthRVogZgwytPrQ0pnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxTDgb5RsOp2ywmWgvV_8xAM7HVWgwAigbum7tdbyDTIstARkrQOp4N5gHALVHgnktGMVtgLsb6bs3ERktc_7xguUCNt1HgNVwpAYfpmywACzryT7Hq06fppFHaN8tV2gviTYfE2FfcWgfiWgvubsvpxzvd_FvcWstAhgfhLyfmRgv@x8tdNVwmbVwpQ8xQOp4N5gHALVHgnktG1V3cNsXyhktARVtytPrQ0pnabktBnsHA1V3cNVxT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nzHgRsHpaKSppyvELVb8DgbhRgfJL_YnmPzcmFtmTywuxUvyhktARVt85stmxzwmRgwTtUWNfYnRRYtiTybpNVrmRgtp2yw12ywmWgvVCQkUWQxgO1CNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrdTsOp2ywmWgvV_8xAM7HVWgwAigbum7tdbyDTIstARkrQOpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxT1kHc_7tdbFOg2k3dxgwTtzfu_FvPQzrQOpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxTaVwonkHc_7tdbFOiWstuRkrgIU3Eb7tcNPwgL73@hgCPQztpNgwToXnsMVtchk3sNVHc_YHdWVxiTgZATywm2yv@bUWNt13cT7kgxgwpR7HypU3cTFohRk3@hgCFT2o6C8xlDPr7iKSquKSgoXnsQyw@ngvBm8DGiY39RsWNfYnRRYtiTybpNVrECgbuxIthbgwyfsthbgwnhgtcbPrQ0pnGtkwG4ztd2yblhVHp_Yfdm73nhgtcN8bATgw7nOwyQ8ogLk3pLFtRTYrgu8rPu8fetPrQ0pnsuz3cTyHmNVrabktBnsHAistiRytcNVHOxsthbgwnhgtcxNWNtMrPm8w@LywGoYnstMrmRVH9_YtGistiRytcNVHApgwERQtcxgwATYXVbQwyfsthbgwnhgtcbUWNtMrP0MrP0ow9NsvEbstAmU3cTFohRk3@hgCFT2o6C8xNoYnstpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxT1kHc_7tdbFOg2k3dxgwTtzfu_FvGfKrT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8n8vBLFfuuKS7_@jqIPbExVtToXnstMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrp2ywmWgvVn2bR_yv8RsOeQ8xAMY3im8DGQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfdTs3pMKSq4YS9uXfyTyt@_UWNtpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxTMst9NVHBnsHANgH8_8xAtktARk3FT2o6xXrhuXrQOpnsMVwsNVHc_YHdWgDuRVHsNVHc_YHdWVxTMst9NVHrnsHAC8xTD8SquKSgoXnstMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrdTsOp2ywmWgvV_8xAM7HVWgwAigbum7tdbyDTQVtpLsbToXnstpnstkwG48rmRVtphVwguPHybs3UnkHgRVxTiV3@hgCc_YrgIPtcTF3qWgvVC8SgoXnstp4NOonRRYtiTybpNVruRVHxnstERk3FT2o6C8xNoYnstMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrRnstERk3obkwmhgtc_8xAMY3im8DGQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfdTs3ppXS74yWqIPbExVtToXnsistiRytcNVHApgwERQtcxgwATYXVbQwyQ8vBn0wpnVHc_YrgIU3Eb7tcNPwgL73@hgCPQzv@nsv5_UWNtp4N5gHALVHgnktGQyw8nkHc2ItpTywmCQkUWQxgO1CNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrdTsORnstERk3TtzfuTyC@RkfBbs3qWgvVxXrAnktc_UWNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrRnstERk3obkwmhgtc_8xAMY3im8DGQzrQOp4N5gHALVHgnktGMst9NVHrnsHAC8xNoYnsMgHm_ywATFXrxK3d_F3cbOtECPwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzringHAT7wpAYtARytTtzfgNktc_7ZvxQogoXnstkwG4Uv9_Y3cNVHDT5DPa@xGistiRytcNVHApgwERQtcxgwATYXVbQwyQ8vBnNthRk3@hgCoLVtpLywTtzfuTyC@RkfBbs3qWgvVxXrTWstiZkrQOpng2VryMgHm_ywATFXrx@Detznsto3cxsthRsohRk3@hgCFT2o6C8xQOpncWs3c0pnsistiRytcNVHApgwERQtcxgwATYXVbQwyQUvpRYtETstaNkt9xkrgI8bANgwmCQkUW5DyMgHm_ywATFXrx8SgoXnP0onRRYtiTybpNVr1mywAA2bATstaC8HmWVfGIgv8RVfGpybBT7b@uPbcbswyT7fGts3CRs3g0ywj_VtcbznQ0pnhhk3GDgwRT7rPu8odT7bAQFt9NVwy4U3i_ywcNkfabVwECVr8uUHgTVHybPrpuzSgoXns5yvmmPHpm7rPu8odT7bAQFt9NVwy4U3i_ywcNkfyRgblCVHGfPryRgblCVHguUfGQ@xQOpnhhk3GM7HVWgw4TY3GfKrliFtpWkvd_yDAnVf@nsvdTybpNgDAnVfBbk3cLVHp_ybcLyDAnVfuTyvERF3PIst@fgwARYvd_yDAnVfuLk3pWVtThk3uxXtpAUWNtpnuTyC@RsYE_7r5fKrlDz3cLyb_hkv@RgDluUxG48bu_2wubkCchOv@RVrMuUJVRs3luzWGpztpA8xQOpnsM7HVWgw4TY3Go8DGpPfabVwECgDluUxGpybBT7bGoPrlDPbcbswyTyDluUxG4gwgAVbEZXnst13Eb7tcL_HmmUxPuUJ@DgwRTyDluUxGDgwRT7r5uUJ@iFtqx6JGoPrEnV3QOpnsM7HVWgw4TY3Go8DGpPfuLk3cRktYx6JGoPr@RkwEmUxGpPfuLk3cRktkx6JGoPrEnV3QOpnabktBnsHA1V3cNVx9_7t@uztdxgw@uU3Eb7tcL_HmbUWNfYnK1U3i_ybqTYDND6fTnVwVNXnNOonND63i_ybqT7rEb73cx6JERVCEnzbd2yvuLk3gm7HluU3mLgDl4VHEmYWp1P3mnV3cWVtc_73pmF3AMst8n8vqRYfqCV3MOFtARgbBxXSal@SRDgb8x@SmpzDK1U3i_ybqTYDNOMDdf8fGuNtqhQwuNztcT7r3nV39NVwc_7rDnVwcmzwp_7raAFHAigbmRsvE_6HdTFvyNUvpxVr8fzDND63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTIXnGuzHd_7romFtqm8DG1_3pm7rKW7rOxNWNuPromFtqNP39L7byoNJubVHcbQwlDPruQXjhM6jzbUWNuPromFtqNP39L7byoNJ8bktWbVwlDPrqf2xQOMrG1_3pmYfqRF3yCU0luFtqRYtBRk3um2wmbQYlDPrqf2xQOMrG1_3pmYfqRF3yCU0ligw@hgCWRVHaRgwAAPfGu@OgoXnGuUOqnV3AuyHuCVxOAPwc2gv9WVHlDPrRhVtuRgOgoXnGuUOqnV3AuyHuCVxOAPwc2gv9WVH3Rk3rhgClDPrqf2xQOMrG1_3pmYfqRF3yCU0liFtqxstuT7odbywmAPfG5gv@LywzbUWNuPry5gHALVHgnktytPrQ0MrGuPrhhk3GuyvGfKrBnsv9xgwATYfi_ywdTywJWgw8RktECUJuLk3gm7HltUWGuyvAiyCqRVrPuUJERVCEnzbd2yvuLk3gm7HloKrqhkfdLyCALVrPuPHmRywQOMrGuPrhhk3GM7rPuPwpLgH8RktENUwcTyz@RgtcNVHu_5CvhswnhgtcCUJuLk3gm7HltU0qfNWGOMrGuPrqhkfu_FvGfKrl1UfihXfqnV3dTs3AIgwEnP3pmYf2LFJQOMrGuPrqhkfpNgwm_Ftmm8DG5gHALVHgnktytPrQ0MrGuPrGuzHd_7ruhVrPuPwpLgH8RktENUvmRgvERgz@RgtcNVHypU3i_ybqTFJgoKruhkfEb73cm8DGpPHcC7HpOgvhhs3i_ybqTFJQuU3dN8vubYtim8DGiY39RsWNuPrGuPrGMyvAMY3im8DGpUfpMkSAuFtqhVwuNztcTFfqnV3AOs3loXnGuPrGuPruNP3d_ywATYopTgwAtktuRk3E_5wRnk3cCU3dWPrubUWNuPrGu84QOMrGuPruNP3d_ywATYopTgwAtktuRk3E_5wRnk3cCP3dWPrubUWNuPrPbPxgoXnK1U3i_ybqTYDND@r8fPr3nV3jTs3AIgwEmPYpmyHATgwmmUXpTgwGlOtBm8f8IXnND63i_ybqT7rEb73cx6JERVCEnzbd2yvuLk3gm7HlIXnhhk3GpstpAVtcTyvlm8DGpstpAVtcTyvlmP4KmUCPZXnlnstlWgwEhswAMgtBm8DGpstpAVtcTyvlNUv8TVrKW7rOxNWN4zw9NsvEbstAC8xGoYnhhk3GpgvBL7rPuPwpLgH8RktENUvmRgvERgz@RgtcNVHypU3i_ybqTFJgoXnlhVwuN8vubYtim8DGiY39RsWNpgvBLYfEb73cm8DGpPHcC7HpOgvhhs3i_ybqTFJQOoHd_7r9Lyw4L_oGfKrl4VHEmF3_pPrPfKrBnsv9xgwATYf@nsvdTybpNkfq_FtEnsvpWsWNpgvBLYfu_FvGfKrylF3cLNY6mUDGpPbET73u06JGOKrl4VHEmYWltPr5uznl1UfaAFHApstpAVtcTyvlLywm2ybiRs3AMst8nPHdAsf2LFflm7HAOs3loXnhhk3GIstBRVrPuPwpLgH8RktENUwcTyz@RgtcNVHu_5CvhswnhgtcCUJuLk3gm7HltU0qfNWNIstBRkfqhk3cNVHnnVwcN8bALywmTYXc2stmRVxlhVwuWPrAnVwcbUWNfyxytUWND6fuLk3gm7HLOonKMFvmbV3EmPHVmywPpPHcC7HpOgvhhs3i_ybqTFJLO1wpnsw@RVHdAkfixVwAuyHuCVxRRYtiTybpNVxguUCNpstpAVtcTyvlNPwc2gbARsY@nVHypUfup6jq5Kjh18S7h6J@uU0eDPref_fGpPwg2yflm7H8aVw8aKjqa@Smp@jqlKW74@fqp8xAaVwBL2wm2ybiRVxlnstlWgwEhswAuyHThVwuC8xgoXnlnstlWgwEhswAuyHThVwuC8xAlktd_VtcL2bAAVtc_2weRywuT7xgoXnlnstlWgwEhswAlktd_VtcL2wm2ybiRs3ytUWNfyxQOMDpMFvmbV3ENXnNOMDdf8fGaKCeu8f8IXnKigbhm8bBx6JBbkH8pV3Ex8vBx8SEu@SeQ6j9u@j74KW8u6JGM7HVWgwPpUHgTVHy0@SqCFWG4gwgAVbE0@SqCFWlIXnKMFvmbV3EmPHVmywPpPHcC7HpOgvhhs3i_ybqTFJLO1wpnsw@RVHdAkfixVwAuyHuCVxRRYtiTybpNVxguUCGpstpAVtcTyvlNPwgL73@hgCypPwg2yflm7H8aVw8aKjqa@Smp@jqlKW74@fqp8xQu84goXnK1U3i_ybqTYDND6fBbkHLOonNOMDuLk3gm7HLOMrG4zw9NsvEbstAC8b@M7fpWUw@Q7fdW8tgoybOAUzpnsw@RgXAhVtVTybiLFoT0gwiTFJzxX3Qts0mx2DgZ03zW74RRYtiTybpNVxgoYnGuPxgZ03zN83Pts0mx0feW74Ox2xAuyHuCVxd_Fw9xgwATF3gf7fgZ03zNPtPaXxARsHGi5vERVxgo@vPMYfi_ywdTywJWgw8RktECUtgDznGu8tPMYflRVHJWgw8RktELYXVT2vlN5v8RVxpbU0qfNWdN8vubYtix@SQakfu_FvPpsW8NP3d_ywATYopTgwAtktuRk3E_5wRnk3cC8v@fgxNuPrPbPxabktBnsH@istiRytcNVH@pU3i_ybqTFJ@pUfppFHaNUwpnsw@RgfdNgv@b7HgLs3AMst8n8vAhVtVTybiLYf2LFJ@pUwdA8xQOonGuUwdCUJi_ywdTywlDPrll2X8iXjaiKjqQ6j8a6J@uUJBbk3cLVHmpyvELVbAMst8A8xQOMrGpgvypU3cNVwlDPrluyvlRkHgRsHltUWNOMDpMFvmbV3ENXnND6fyTyt@NKDuLk3gm7HGDgvAAgHdAgwPOgvhhs3i_ybqTYDN5gHALVHgnktGIst4TyvERF3ytPrQ01HgNVwpAYfuTyvERF3PQzrQO13cT7kgxgwpR7HyQztpL_HdTyHuC8xTD8Squ@xQOp4NIst4TyvERF3ytUWND6fuLk3gm7HLl"
    #	final_rtmp=' token=$doregex[tok] pageUrl=http://www.direct2watch.com/ live=1 timeout=10</link>
        get_html=4
        un_chtml=get_html(meta,data);
ll11="QW5kcm9pZCA4LjAuMCBBUEkgbGV2ZWwgMjYgKGtlcm5lbDogTGludXggMy4xOC42Ni1wZXJmLWdjOGIxZGM3KQ=="
ll1Ix7= base64.b64decode(ll11)
def get_unwise( str_eval):
    page_value=""
    try:        
        ss="w,i,s,e=("+str_eval+')' 
        exec (ss)
        page_value=unwise_func(w,i,s,e)
    except: traceback.print_exc(file=sys.stdout)
    #print 'unpacked',page_value
    return page_value
ll11="V2luZG93cyAxMCAoa2VybmVsOiBXaW5kb3dzIE5UIDEwLjAuMTc3NjMp"
ll1Ix1= base64.b64decode(ll11)    
ll11="QW5kcm9pZCA3LjEuMiBBUEkgbGV2ZWwgMjUgKGtlcm5lbDogTGludXggMy4xNC4yOSk="
ll1Ix2= base64.b64decode(ll11)
ll11="QW5kcm9pZCA4LjEuMCBBUEkgbGV2ZWwgMjcgKGtlcm5lbDogTGludXggNC45LjYxKQ=="
ll1Ix3= base64.b64decode(ll11)

def unwise_func( w, i, s, e):
    lIll = 0;
    ll1I = 0;
    Il1l = 0;
    ll1l = [];
    l1lI = [];
    while True:
        if (lIll < 5):
            l1lI.append(w[lIll])
        elif (lIll < len(w)):
            ll1l.append(w[lIll]);
        lIll+=1;
        if (ll1I < 5):
            l1lI.append(i[ll1I])
        elif (ll1I < len(i)):
            ll1l.append(i[ll1I])
        ll1I+=1;
        if (Il1l < 5):
            l1lI.append(s[Il1l])
        elif (Il1l < len(s)):
            ll1l.append(s[Il1l]);
        Il1l+=1;
        if (len(w) + len(i) + len(s) + len(e) == len(ll1l) + len(l1lI) + len(e)):
            break;
        
    lI1l = ''.join(ll1l)#.join('');
    I1lI = ''.join(l1lI)#.join('');
    ll1I = 0;
    l1ll = [];
    for lIll in range(0,len(ll1l),2):
        #print 'array i',lIll,len(ll1l)
        ll11 = -1;
        if ( ord(I1lI[ll1I]) % 2):
            ll11 = 1;
        #print 'val is ', lI1l[lIll: lIll+2]
        l1ll.append(chr(    int(lI1l[lIll: lIll+2], 36) - ll11));
        ll1I+=1;
        if (ll1I >= len(l1lI)):
            ll1I = 0;
    ret=''.join(l1ll)
    if 'eval(function(w,i,s,e)' in ret:
        print ('STILL GOing')
        ret=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(ret)[0] 
        return get_unwise(ret)
    else:
        print ('FINISHED')
        return ret

ll11="QW5kcm9pZCA3LjEuMiBBUEkgbGV2ZWwgMjUgKGtlcm5lbDogTGludXggMy4xMC4xMDQp"
ll1Ix4= base64.b64decode(ll11)
ll11="QW5kcm9pZCA5LjAuMCBBUEkgbGV2ZWwgMjggKGtlcm5lbDogTGludXggNC40LjE1OSk="
ll1Ix5= base64.b64decode(ll11)
ll11="QW5kcm9pZCA4LjAuMCBBUEkgbGV2ZWwgMjYgKGtlcm5lbDogTGludXggNC45LjU0KQ=="
ll1Ix6= base64.b64decode(ll11)
## Thanks to daschacka, an epg scraper for http://i.teleboy.ch/programm/station_select.php
##  http://forum.xbmc.org/post.php?p=936228&postcount=1076
def getepg(link):
        url=urllib.urlopen(link)
        source=url.read()
        url.close()
        source2 = source.split("Jetzt")
        source3 = source2[1].split('programm/detail.php?const_id=')
        sourceuhrzeit = source3[1].split('<br /><a href="/')
        nowtime = sourceuhrzeit[0][40:len(sourceuhrzeit[0])]
        sourcetitle = source3[2].split("</a></p></div>")
        nowtitle = sourcetitle[0][17:len(sourcetitle[0])]
        nowtitle = nowtitle.encode('utf-8')
        return "  - "+nowtitle+" - "+nowtime
ll11="V2luZG93cyA3IFNQMSAoa2VybmVsOiBXaW5kb3dzIE5UIDYuMS43NjAxKQ=="
ll1Ix8= base64.b64decode(ll11)
ll11="QW5kcm9pZCA5LjAuMCBBUEkgbGV2ZWwgMjggKGtlcm5lbDogTGludXggNC4xNC41Ni1nYTdkYzM2Nik="
ll1Ix9= base64.b64decode(ll11)
def get_epg(url, regex):
        data = makeRequest(url)
        try:
            item = re.findall(regex, data)[0]
            return item
        except:
            addon_log('regex failed')
            addon_log(regex)
            return

ll11="QW5kcm9pZCA1LjEuMSBBUEkgbGV2ZWwgMjIgKGtlcm5lbDogTGludXggMy4xMC4zMyk="
ll1Ix10= base64.b64decode(ll11)
ll11="QW5kcm9pZCA5LjAuMCBBUEkgbGV2ZWwgMjggKGtlcm5lbDogTGludXggNC40LjExMS0xNjEzOTExOSk="
ll1Ix11= base64.b64decode(ll11)
def unpack(sJavascript,iteration=1, totaliterations=2  ):
    print ('iteration',iteration)
    if sJavascript.startswith('var _0xcb8a='):
        aSplit=sJavascript.split('var _0xcb8a=')
        ss="myarray="+aSplit[1].split("eval(")[0]
        exec(ss)
        a1=62
        c1=int(aSplit[1].split(",62,")[1].split(',')[0])
        p1=myarray[0]
        k1=myarray[3]
        with open('temp file'+str(iteration)+'.js', "wb") as filewriter:
            filewriter.write(str(k1))
        #aa=1/0
    else:

        aSplit = sJavascript.split("rn p}('")
        print (aSplit)
        
        p1,a1,c1,k1=('','0','0','')
     
        ss="p1,a1,c1,k1=('"+aSplit[1].split(".spli")[0]+')' 
        exec(ss)
    k1=k1.split('|')
    aSplit = aSplit[1].split("))'")
#    print ' p array is ',len(aSplit)
#   print len(aSplit )

    #p=str(aSplit[0]+'))')#.replace("\\","")#.replace('\\\\','\\')

    #print aSplit[1]
    #aSplit = aSplit[1].split(",")
    #print aSplit[0] 
    #a = int(aSplit[1])
    #c = int(aSplit[2])
    #k = aSplit[3].split(".")[0].replace("'", '').split('|')
    #a=int(a)
    #c=int(c)
    
    #p=p.replace('\\', '')
#    print 'p val is ',p[0:100],'............',p[-100:],len(p)
#    print 'p1 val is ',p1[0:100],'............',p1[-100:],len(p1)
    
    #print a,a1
    #print c,a1
    #print 'k val is ',k[-10:],len(k)
#    print 'k1 val is ',k1[-10:],len(k1)
    e = ''
    d = ''#32823

    #sUnpacked = str(__unpack(p, a, c, k, e, d))
    sUnpacked1 = str(__unpack(p1, a1, c1, k1, e, d,iteration))
    
    #print sUnpacked[:200]+'....'+sUnpacked[-100:], len(sUnpacked)
#    print sUnpacked1[:200]+'....'+sUnpacked1[-100:], len(sUnpacked1)
    
    #exec('sUnpacked1="'+sUnpacked1+'"')
    if iteration>=totaliterations:
#        print 'final res',sUnpacked1[:200]+'....'+sUnpacked1[-100:], len(sUnpacked1)
        return sUnpacked1#.replace('\\\\', '\\')
    else:
#        print 'final res for this iteration is',iteration
        return unpack(sUnpacked1,iteration+1)#.replace('\\', ''),iteration)#.replace('\\', '');#unpack(sUnpacked.replace('\\', ''))