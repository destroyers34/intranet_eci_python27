(function () {
    tinymce.PluginManager.requireLangPack("grappelli");
    var e = tinymce.DOM;
    tinymce.create("tinymce.plugins.Grappelli", {
        init: function (t, n) {
            var r = this;
            tb = t.getParam("grappelli_adv_toolbar", "toolbar2");
            documentstructure_css = n + "../../../themes/advanced/skins/grappelli/content_documentstructure_" + t.settings.language + ".css";
            cookie_date = new Date;
            var s = cookie_date.getFullYear();
            cookie_date.setYear(s + 1);
            cookie_grappelli_show_documentstructure = tinymce.util.Cookie.get("grappelli_show_documentstructure");
            cookie_grappelli_show_documentstructure != null ? t.settings.grappelli_show_documentstructure = cookie_grappelli_show_documentstructure : tinymce.util.Cookie.set("grappelli_show_documentstructure", t.settings.grappelli_show_documentstructure, cookie_date, "/");
            t.onInit.add(function () {
                "mce_fullscreen" == t.id && t.dom.addClass(t.dom.select("body"), "fullscreen");
                t.settings.grappelli_adv_hidden ? r._hide_adv_menu(t) : r._show_adv_menu(t);
                t.settings.grappelli_show_documentstructure == "on" ? r._show_documentstructure(t) : r._hide_documentstructure(t)
            });
            t.addCommand("Grappelli_Adv", function () {
                e.isHidden(t.controlManager.get(tb).id) ? r._show_adv_menu(t) : r._hide_adv_menu(t)
            });
            t.addCommand("Grappelli_DocumentStructure", function () {
                i = t.controlManager;
                t.settings.grappelli_show_documentstructure == "on" ? r._hide_documentstructure(t) : r._show_documentstructure(t)
            });
            t.addButton("grappelli_adv", {title: "grappelli.grappelli_adv_desc", cmd: "Grappelli_Adv"});
            t.addButton("grappelli_documentstructure", {
                title: "grappelli.grappelli_documentstructure_desc",
                cmd: "Grappelli_DocumentStructure"
            });
            t.onBeforeExecCommand.add(function (e, t, n, i) {
                if ("mceFullScreen" != t)return;
                if ("mce_fullscreen" == e.id) {
                    base_ed = tinyMCE.get(e.settings.fullscreen_editor_id);
                    e.settings.grappelli_adv_hidden ? r._hide_adv_menu(base_ed) : r._show_adv_menu(base_ed);
                    e.settings.grappelli_show_documentstructure == "on" ? r._show_documentstructure(base_ed) : r._hide_documentstructure(base_ed)
                }
            });
            t.addShortcut("alt+shift+z", t.getLang("grappelli_adv_desc"), "Grappelli_Adv")
        }, _resizeIframe: function (t, n, r) {
            var i = t.getContentAreaContainer().firstChild;
            e.setStyle(i, "height", i.clientHeight + r);
            t.theme.deltaHeight += r
        }, _show_documentstructure: function (e) {
            head = e.getBody().previousSibling;
            var t = head.childNodes;
            for (var n = 0; n < t.length; n++)if (t[n].nodeName == "LINK" && t[n].getAttribute("href") == documentstructure_css)return;
            var r = document.createElement("link");
            r.rel = "stylesheet";
            r.mce_href = documentstructure_css;
            r.href = documentstructure_css;
            head.appendChild(r);
            e.settings.grappelli_show_documentstructure = "on";
            tinymce.util.Cookie.set("grappelli_show_documentstructure", "on", cookie_date, "/");
            e.controlManager.setActive("grappelli_documentstructure", !0)
        }, _hide_documentstructure: function (e) {
            head = e.getBody().previousSibling;
            vs_link = null;
            var t = head.childNodes;
            for (var n = 0; n < t.length; n++)if (t[n].nodeName == "LINK" && t[n].getAttribute("href") == documentstructure_css) {
                vs_link = t[n];
                break
            }
            if (vs_link !== null) {
                head.removeChild(vs_link);
                e.settings.grappelli_show_documentstructure = "off";
                tinymce.util.Cookie.set("grappelli_show_documentstructure", "off", cookie_date, "/");
                e.controlManager.setActive("grappelli_documentstructure", !1)
            }
        }, _show_adv_menu: function (t) {
            if (t.controlManager.get(tb, !1)) {
                t.controlManager.setActive("grappelli_adv", 1);
                e.show(t.controlManager.get(tb).id);
                this._resizeIframe(t, tb, -28);
                t.settings.grappelli_adv_hidden = 0
            }
        }, _hide_adv_menu: function (t) {
            if (t.controlManager.get(tb, !1)) {
                t.controlManager.setActive("grappelli_adv", 0);
                e.hide(t.controlManager.get(tb).id);
                this._resizeIframe(t, tb, 28);
                t.settings.grappelli_adv_hidden = 1
            }
        }, getInfo: function () {
            return {
                longname: "Grappelli Plugin",
                author: "vonautomatisch (patrick kranzlmueller)",
                authorurl: "http://vonautomatisch.at",
                infourl: "http://code.google.com/p/django-grappelli/",
                version: "1.1"
            }
        }
    });
    tinymce.PluginManager.add("grappelli", tinymce.plugins.Grappelli)
})();