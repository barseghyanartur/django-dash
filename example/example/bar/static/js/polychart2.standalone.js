;
(function(){var n=this,t=n._,r={},e=Array.prototype,u=Object.prototype,i=Function.prototype,a=e.push,o=e.slice,c=e.concat,l=u.toString,f=u.hasOwnProperty,s=e.forEach,p=e.map,v=e.reduce,h=e.reduceRight,g=e.filter,d=e.every,m=e.some,y=e.indexOf,b=e.lastIndexOf,x=Array.isArray,_=Object.keys,j=i.bind,w=function(n){return n instanceof w?n:this instanceof w?(this._wrapped=n,void 0):new w(n)};"undefined"!=typeof exports?("undefined"!=typeof module&&module.exports&&(exports=module.exports=w),exports._=w):n._=w,w.VERSION="1.4.3";var A=w.each=w.forEach=function(n,t,e){if(null!=n)if(s&&n.forEach===s)n.forEach(t,e);else if(n.length===+n.length){for(var u=0,i=n.length;i>u;u++)if(t.call(e,n[u],u,n)===r)return}else for(var a in n)if(w.has(n,a)&&t.call(e,n[a],a,n)===r)return};w.map=w.collect=function(n,t,r){var e=[];return null==n?e:p&&n.map===p?n.map(t,r):(A(n,function(n,u,i){e[e.length]=t.call(r,n,u,i)}),e)};var O="Reduce of empty array with no initial value";w.reduce=w.foldl=w.inject=function(n,t,r,e){var u=arguments.length>2;if(null==n&&(n=[]),v&&n.reduce===v)return e&&(t=w.bind(t,e)),u?n.reduce(t,r):n.reduce(t);if(A(n,function(n,i,a){u?r=t.call(e,r,n,i,a):(r=n,u=!0)}),!u)throw new TypeError(O);return r},w.reduceRight=w.foldr=function(n,t,r,e){var u=arguments.length>2;if(null==n&&(n=[]),h&&n.reduceRight===h)return e&&(t=w.bind(t,e)),u?n.reduceRight(t,r):n.reduceRight(t);var i=n.length;if(i!==+i){var a=w.keys(n);i=a.length}if(A(n,function(o,c,l){c=a?a[--i]:--i,u?r=t.call(e,r,n[c],c,l):(r=n[c],u=!0)}),!u)throw new TypeError(O);return r},w.find=w.detect=function(n,t,r){var e;return E(n,function(n,u,i){return t.call(r,n,u,i)?(e=n,!0):void 0}),e},w.filter=w.select=function(n,t,r){var e=[];return null==n?e:g&&n.filter===g?n.filter(t,r):(A(n,function(n,u,i){t.call(r,n,u,i)&&(e[e.length]=n)}),e)},w.reject=function(n,t,r){return w.filter(n,function(n,e,u){return!t.call(r,n,e,u)},r)},w.every=w.all=function(n,t,e){t||(t=w.identity);var u=!0;return null==n?u:d&&n.every===d?n.every(t,e):(A(n,function(n,i,a){return(u=u&&t.call(e,n,i,a))?void 0:r}),!!u)};var E=w.some=w.any=function(n,t,e){t||(t=w.identity);var u=!1;return null==n?u:m&&n.some===m?n.some(t,e):(A(n,function(n,i,a){return u||(u=t.call(e,n,i,a))?r:void 0}),!!u)};w.contains=w.include=function(n,t){return null==n?!1:y&&n.indexOf===y?-1!=n.indexOf(t):E(n,function(n){return n===t})},w.invoke=function(n,t){var r=o.call(arguments,2);return w.map(n,function(n){return(w.isFunction(t)?t:n[t]).apply(n,r)})},w.pluck=function(n,t){return w.map(n,function(n){return n[t]})},w.where=function(n,t){return w.isEmpty(t)?[]:w.filter(n,function(n){for(var r in t)if(t[r]!==n[r])return!1;return!0})},w.max=function(n,t,r){if(!t&&w.isArray(n)&&n[0]===+n[0]&&65535>n.length)return Math.max.apply(Math,n);if(!t&&w.isEmpty(n))return-1/0;var e={computed:-1/0,value:-1/0};return A(n,function(n,u,i){var a=t?t.call(r,n,u,i):n;a>=e.computed&&(e={value:n,computed:a})}),e.value},w.min=function(n,t,r){if(!t&&w.isArray(n)&&n[0]===+n[0]&&65535>n.length)return Math.min.apply(Math,n);if(!t&&w.isEmpty(n))return 1/0;var e={computed:1/0,value:1/0};return A(n,function(n,u,i){var a=t?t.call(r,n,u,i):n;e.computed>a&&(e={value:n,computed:a})}),e.value},w.shuffle=function(n){var t,r=0,e=[];return A(n,function(n){t=w.random(r++),e[r-1]=e[t],e[t]=n}),e};var F=function(n){return w.isFunction(n)?n:function(t){return t[n]}};w.sortBy=function(n,t,r){var e=F(t);return w.pluck(w.map(n,function(n,t,u){return{value:n,index:t,criteria:e.call(r,n,t,u)}}).sort(function(n,t){var r=n.criteria,e=t.criteria;if(r!==e){if(r>e||void 0===r)return 1;if(e>r||void 0===e)return-1}return n.index<t.index?-1:1}),"value")};var k=function(n,t,r,e){var u={},i=F(t||w.identity);return A(n,function(t,a){var o=i.call(r,t,a,n);e(u,o,t)}),u};w.groupBy=function(n,t,r){return k(n,t,r,function(n,t,r){(w.has(n,t)?n[t]:n[t]=[]).push(r)})},w.countBy=function(n,t,r){return k(n,t,r,function(n,t){w.has(n,t)||(n[t]=0),n[t]++})},w.sortedIndex=function(n,t,r,e){r=null==r?w.identity:F(r);for(var u=r.call(e,t),i=0,a=n.length;a>i;){var o=i+a>>>1;u>r.call(e,n[o])?i=o+1:a=o}return i},w.toArray=function(n){return n?w.isArray(n)?o.call(n):n.length===+n.length?w.map(n,w.identity):w.values(n):[]},w.size=function(n){return null==n?0:n.length===+n.length?n.length:w.keys(n).length},w.first=w.head=w.take=function(n,t,r){return null==n?void 0:null==t||r?n[0]:o.call(n,0,t)},w.initial=function(n,t,r){return o.call(n,0,n.length-(null==t||r?1:t))},w.last=function(n,t,r){return null==n?void 0:null==t||r?n[n.length-1]:o.call(n,Math.max(n.length-t,0))},w.rest=w.tail=w.drop=function(n,t,r){return o.call(n,null==t||r?1:t)},w.compact=function(n){return w.filter(n,w.identity)};var R=function(n,t,r){return A(n,function(n){w.isArray(n)?t?a.apply(r,n):R(n,t,r):r.push(n)}),r};w.flatten=function(n,t){return R(n,t,[])},w.without=function(n){return w.difference(n,o.call(arguments,1))},w.uniq=w.unique=function(n,t,r,e){w.isFunction(t)&&(e=r,r=t,t=!1);var u=r?w.map(n,r,e):n,i=[],a=[];return A(u,function(r,e){(t?e&&a[a.length-1]===r:w.contains(a,r))||(a.push(r),i.push(n[e]))}),i},w.union=function(){return w.uniq(c.apply(e,arguments))},w.intersection=function(n){var t=o.call(arguments,1);return w.filter(w.uniq(n),function(n){return w.every(t,function(t){return w.indexOf(t,n)>=0})})},w.difference=function(n){var t=c.apply(e,o.call(arguments,1));return w.filter(n,function(n){return!w.contains(t,n)})},w.zip=function(){for(var n=o.call(arguments),t=w.max(w.pluck(n,"length")),r=Array(t),e=0;t>e;e++)r[e]=w.pluck(n,""+e);return r},w.object=function(n,t){if(null==n)return{};for(var r={},e=0,u=n.length;u>e;e++)t?r[n[e]]=t[e]:r[n[e][0]]=n[e][1];return r},w.indexOf=function(n,t,r){if(null==n)return-1;var e=0,u=n.length;if(r){if("number"!=typeof r)return e=w.sortedIndex(n,t),n[e]===t?e:-1;e=0>r?Math.max(0,u+r):r}if(y&&n.indexOf===y)return n.indexOf(t,r);for(;u>e;e++)if(n[e]===t)return e;return-1},w.lastIndexOf=function(n,t,r){if(null==n)return-1;var e=null!=r;if(b&&n.lastIndexOf===b)return e?n.lastIndexOf(t,r):n.lastIndexOf(t);for(var u=e?r:n.length;u--;)if(n[u]===t)return u;return-1},w.range=function(n,t,r){1>=arguments.length&&(t=n||0,n=0),r=arguments[2]||1;for(var e=Math.max(Math.ceil((t-n)/r),0),u=0,i=Array(e);e>u;)i[u++]=n,n+=r;return i};var I=function(){};w.bind=function(n,t){var r,e;if(n.bind===j&&j)return j.apply(n,o.call(arguments,1));if(!w.isFunction(n))throw new TypeError;return r=o.call(arguments,2),e=function(){if(!(this instanceof e))return n.apply(t,r.concat(o.call(arguments)));I.prototype=n.prototype;var u=new I;I.prototype=null;var i=n.apply(u,r.concat(o.call(arguments)));return Object(i)===i?i:u}},w.bindAll=function(n){var t=o.call(arguments,1);return 0==t.length&&(t=w.functions(n)),A(t,function(t){n[t]=w.bind(n[t],n)}),n},w.memoize=function(n,t){var r={};return t||(t=w.identity),function(){var e=t.apply(this,arguments);return w.has(r,e)?r[e]:r[e]=n.apply(this,arguments)}},w.delay=function(n,t){var r=o.call(arguments,2);return setTimeout(function(){return n.apply(null,r)},t)},w.defer=function(n){return w.delay.apply(w,[n,1].concat(o.call(arguments,1)))},w.throttle=function(n,t){var r,e,u,i,a=0,o=function(){a=new Date,u=null,i=n.apply(r,e)};return function(){var c=new Date,l=t-(c-a);return r=this,e=arguments,0>=l?(clearTimeout(u),u=null,a=c,i=n.apply(r,e)):u||(u=setTimeout(o,l)),i}},w.debounce=function(n,t,r){var e,u;return function(){var i=this,a=arguments,o=function(){e=null,r||(u=n.apply(i,a))},c=r&&!e;return clearTimeout(e),e=setTimeout(o,t),c&&(u=n.apply(i,a)),u}},w.once=function(n){var t,r=!1;return function(){return r?t:(r=!0,t=n.apply(this,arguments),n=null,t)}},w.wrap=function(n,t){return function(){var r=[n];return a.apply(r,arguments),t.apply(this,r)}},w.compose=function(){var n=arguments;return function(){for(var t=arguments,r=n.length-1;r>=0;r--)t=[n[r].apply(this,t)];return t[0]}},w.after=function(n,t){return 0>=n?t():function(){return 1>--n?t.apply(this,arguments):void 0}},w.keys=_||function(n){if(n!==Object(n))throw new TypeError("Invalid object");var t=[];for(var r in n)w.has(n,r)&&(t[t.length]=r);return t},w.values=function(n){var t=[];for(var r in n)w.has(n,r)&&t.push(n[r]);return t},w.pairs=function(n){var t=[];for(var r in n)w.has(n,r)&&t.push([r,n[r]]);return t},w.invert=function(n){var t={};for(var r in n)w.has(n,r)&&(t[n[r]]=r);return t},w.functions=w.methods=function(n){var t=[];for(var r in n)w.isFunction(n[r])&&t.push(r);return t.sort()},w.extend=function(n){return A(o.call(arguments,1),function(t){if(t)for(var r in t)n[r]=t[r]}),n},w.pick=function(n){var t={},r=c.apply(e,o.call(arguments,1));return A(r,function(r){r in n&&(t[r]=n[r])}),t},w.omit=function(n){var t={},r=c.apply(e,o.call(arguments,1));for(var u in n)w.contains(r,u)||(t[u]=n[u]);return t},w.defaults=function(n){return A(o.call(arguments,1),function(t){if(t)for(var r in t)null==n[r]&&(n[r]=t[r])}),n},w.clone=function(n){return w.isObject(n)?w.isArray(n)?n.slice():w.extend({},n):n},w.tap=function(n,t){return t(n),n};var S=function(n,t,r,e){if(n===t)return 0!==n||1/n==1/t;if(null==n||null==t)return n===t;n instanceof w&&(n=n._wrapped),t instanceof w&&(t=t._wrapped);var u=l.call(n);if(u!=l.call(t))return!1;switch(u){case"[object String]":return n==t+"";case"[object Number]":return n!=+n?t!=+t:0==n?1/n==1/t:n==+t;case"[object Date]":case"[object Boolean]":return+n==+t;case"[object RegExp]":return n.source==t.source&&n.global==t.global&&n.multiline==t.multiline&&n.ignoreCase==t.ignoreCase}if("object"!=typeof n||"object"!=typeof t)return!1;for(var i=r.length;i--;)if(r[i]==n)return e[i]==t;r.push(n),e.push(t);var a=0,o=!0;if("[object Array]"==u){if(a=n.length,o=a==t.length)for(;a--&&(o=S(n[a],t[a],r,e)););}else{var c=n.constructor,f=t.constructor;if(c!==f&&!(w.isFunction(c)&&c instanceof c&&w.isFunction(f)&&f instanceof f))return!1;for(var s in n)if(w.has(n,s)&&(a++,!(o=w.has(t,s)&&S(n[s],t[s],r,e))))break;if(o){for(s in t)if(w.has(t,s)&&!a--)break;o=!a}}return r.pop(),e.pop(),o};w.isEqual=function(n,t){return S(n,t,[],[])},w.isEmpty=function(n){if(null==n)return!0;if(w.isArray(n)||w.isString(n))return 0===n.length;for(var t in n)if(w.has(n,t))return!1;return!0},w.isElement=function(n){return!(!n||1!==n.nodeType)},w.isArray=x||function(n){return"[object Array]"==l.call(n)},w.isObject=function(n){return n===Object(n)},A(["Arguments","Function","String","Number","Date","RegExp"],function(n){w["is"+n]=function(t){return l.call(t)=="[object "+n+"]"}}),w.isArguments(arguments)||(w.isArguments=function(n){return!(!n||!w.has(n,"callee"))}),w.isFunction=function(n){return"function"==typeof n},w.isFinite=function(n){return isFinite(n)&&!isNaN(parseFloat(n))},w.isNaN=function(n){return w.isNumber(n)&&n!=+n},w.isBoolean=function(n){return n===!0||n===!1||"[object Boolean]"==l.call(n)},w.isNull=function(n){return null===n},w.isUndefined=function(n){return void 0===n},w.has=function(n,t){return f.call(n,t)},w.noConflict=function(){return n._=t,this},w.identity=function(n){return n},w.times=function(n,t,r){for(var e=Array(n),u=0;n>u;u++)e[u]=t.call(r,u);return e},w.random=function(n,t){return null==t&&(t=n,n=0),n+(0|Math.random()*(t-n+1))};var T={escape:{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#x27;","/":"&#x2F;"}};T.unescape=w.invert(T.escape);var M={escape:RegExp("["+w.keys(T.escape).join("")+"]","g"),unescape:RegExp("("+w.keys(T.unescape).join("|")+")","g")};w.each(["escape","unescape"],function(n){w[n]=function(t){return null==t?"":(""+t).replace(M[n],function(t){return T[n][t]})}}),w.result=function(n,t){if(null==n)return null;var r=n[t];return w.isFunction(r)?r.call(n):r},w.mixin=function(n){A(w.functions(n),function(t){var r=w[t]=n[t];w.prototype[t]=function(){var n=[this._wrapped];return a.apply(n,arguments),z.call(this,r.apply(w,n))}})};var N=0;w.uniqueId=function(n){var t=""+ ++N;return n?n+t:t},w.templateSettings={evaluate:/<%([\s\S]+?)%>/g,interpolate:/<%=([\s\S]+?)%>/g,escape:/<%-([\s\S]+?)%>/g};var q=/(.)^/,B={"'":"'","\\":"\\","\r":"r","\n":"n","	":"t","\u2028":"u2028","\u2029":"u2029"},D=/\\|'|\r|\n|\t|\u2028|\u2029/g;w.template=function(n,t,r){r=w.defaults({},r,w.templateSettings);var e=RegExp([(r.escape||q).source,(r.interpolate||q).source,(r.evaluate||q).source].join("|")+"|$","g"),u=0,i="__p+='";n.replace(e,function(t,r,e,a,o){return i+=n.slice(u,o).replace(D,function(n){return"\\"+B[n]}),r&&(i+="'+\n((__t=("+r+"))==null?'':_.escape(__t))+\n'"),e&&(i+="'+\n((__t=("+e+"))==null?'':__t)+\n'"),a&&(i+="';\n"+a+"\n__p+='"),u=o+t.length,t}),i+="';\n",r.variable||(i="with(obj||{}){\n"+i+"}\n"),i="var __t,__p='',__j=Array.prototype.join,print=function(){__p+=__j.call(arguments,'');};\n"+i+"return __p;\n";try{var a=Function(r.variable||"obj","_",i)}catch(o){throw o.source=i,o}if(t)return a(t,w);var c=function(n){return a.call(this,n,w)};return c.source="function("+(r.variable||"obj")+"){\n"+i+"}",c},w.chain=function(n){return w(n).chain()};var z=function(n){return this._chain?w(n).chain():n};w.mixin(w),A(["pop","push","reverse","shift","sort","splice","unshift"],function(n){var t=e[n];w.prototype[n]=function(){var r=this._wrapped;return t.apply(r,arguments),"shift"!=n&&"splice"!=n||0!==r.length||delete r[0],z.call(this,r)}}),A(["concat","join","slice"],function(n){var t=e[n];w.prototype[n]=function(){return z.call(this,t.apply(this._wrapped,arguments))}}),w.extend(w.prototype,{chain:function(){return this._chain=!0,this},value:function(){return this._wrapped}})}).call(this);
;
// moment.js
// version : 2.1.0
// author : Tim Wood
// license : MIT
// momentjs.com

(function (undefined) {

    /************************************
        Constants
    ************************************/

    var moment,
        VERSION = "2.1.0",
        round = Math.round, i,
        // internal storage for language config files
        languages = {},

        // check for nodeJS
        hasModule = (typeof module !== 'undefined' && module.exports),

        // ASP.NET json date format regex
        aspNetJsonRegex = /^\/?Date\((\-?\d+)/i,
        aspNetTimeSpanJsonRegex = /(\-)?(\d*)?\.?(\d+)\:(\d+)\:(\d+)\.?(\d{3})?/,

        // format tokens
        formattingTokens = /(\[[^\[]*\])|(\\)?(Mo|MM?M?M?|Do|DDDo|DD?D?D?|ddd?d?|do?|w[o|w]?|W[o|W]?|YYYYY|YYYY|YY|gg(ggg?)?|GG(GGG?)?|e|E|a|A|hh?|HH?|mm?|ss?|SS?S?|X|zz?|ZZ?|.)/g,
        localFormattingTokens = /(\[[^\[]*\])|(\\)?(LT|LL?L?L?|l{1,4})/g,

        // parsing token regexes
        parseTokenOneOrTwoDigits = /\d\d?/, // 0 - 99
        parseTokenOneToThreeDigits = /\d{1,3}/, // 0 - 999
        parseTokenThreeDigits = /\d{3}/, // 000 - 999
        parseTokenFourDigits = /\d{1,4}/, // 0 - 9999
        parseTokenSixDigits = /[+\-]?\d{1,6}/, // -999,999 - 999,999
        parseTokenWord = /[0-9]*['a-z\u00A0-\u05FF\u0700-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+|[\u0600-\u06FF\/]+(\s*?[\u0600-\u06FF]+){1,2}/i, // any word (or two) characters or numbers including two/three word month in arabic.
        parseTokenTimezone = /Z|[\+\-]\d\d:?\d\d/i, // +00:00 -00:00 +0000 -0000 or Z
        parseTokenT = /T/i, // T (ISO seperator)
        parseTokenTimestampMs = /[\+\-]?\d+(\.\d{1,3})?/, // 123456789 123456789.123

        // preliminary iso regex
        // 0000-00-00 + T + 00 or 00:00 or 00:00:00 or 00:00:00.000 + +00:00 or +0000
        isoRegex = /^\s*\d{4}-\d\d-\d\d((T| )(\d\d(:\d\d(:\d\d(\.\d\d?\d?)?)?)?)?([\+\-]\d\d:?\d\d)?)?/,
        isoFormat = 'YYYY-MM-DDTHH:mm:ssZ',

        // iso time formats and regexes
        isoTimes = [
            ['HH:mm:ss.S', /(T| )\d\d:\d\d:\d\d\.\d{1,3}/],
            ['HH:mm:ss', /(T| )\d\d:\d\d:\d\d/],
            ['HH:mm', /(T| )\d\d:\d\d/],
            ['HH', /(T| )\d\d/]
        ],

        // timezone chunker "+10:00" > ["10", "00"] or "-1530" > ["-15", "30"]
        parseTimezoneChunker = /([\+\-]|\d\d)/gi,

        // getter and setter names
        proxyGettersAndSetters = 'Date|Hours|Minutes|Seconds|Milliseconds'.split('|'),
        unitMillisecondFactors = {
            'Milliseconds' : 1,
            'Seconds' : 1e3,
            'Minutes' : 6e4,
            'Hours' : 36e5,
            'Days' : 864e5,
            'Months' : 2592e6,
            'Years' : 31536e6
        },

        unitAliases = {
            ms : 'millisecond',
            s : 'second',
            m : 'minute',
            h : 'hour',
            d : 'day',
            w : 'week',
            M : 'month',
            y : 'year'
        },

        // format function strings
        formatFunctions = {},

        // tokens to ordinalize and pad
        ordinalizeTokens = 'DDD w W M D d'.split(' '),
        paddedTokens = 'M D H h m s w W'.split(' '),

        formatTokenFunctions = {
            M    : function () {
                return this.month() + 1;
            },
            MMM  : function (format) {
                return this.lang().monthsShort(this, format);
            },
            MMMM : function (format) {
                return this.lang().months(this, format);
            },
            D    : function () {
                return this.date();
            },
            DDD  : function () {
                return this.dayOfYear();
            },
            d    : function () {
                return this.day();
            },
            dd   : function (format) {
                return this.lang().weekdaysMin(this, format);
            },
            ddd  : function (format) {
                return this.lang().weekdaysShort(this, format);
            },
            dddd : function (format) {
                return this.lang().weekdays(this, format);
            },
            w    : function () {
                return this.week();
            },
            W    : function () {
                return this.isoWeek();
            },
            YY   : function () {
                return leftZeroFill(this.year() % 100, 2);
            },
            YYYY : function () {
                return leftZeroFill(this.year(), 4);
            },
            YYYYY : function () {
                return leftZeroFill(this.year(), 5);
            },
            gg   : function () {
                return leftZeroFill(this.weekYear() % 100, 2);
            },
            gggg : function () {
                return this.weekYear();
            },
            ggggg : function () {
                return leftZeroFill(this.weekYear(), 5);
            },
            GG   : function () {
                return leftZeroFill(this.isoWeekYear() % 100, 2);
            },
            GGGG : function () {
                return this.isoWeekYear();
            },
            GGGGG : function () {
                return leftZeroFill(this.isoWeekYear(), 5);
            },
            e : function () {
                return this.weekday();
            },
            E : function () {
                return this.isoWeekday();
            },
            a    : function () {
                return this.lang().meridiem(this.hours(), this.minutes(), true);
            },
            A    : function () {
                return this.lang().meridiem(this.hours(), this.minutes(), false);
            },
            H    : function () {
                return this.hours();
            },
            h    : function () {
                return this.hours() % 12 || 12;
            },
            m    : function () {
                return this.minutes();
            },
            s    : function () {
                return this.seconds();
            },
            S    : function () {
                return ~~(this.milliseconds() / 100);
            },
            SS   : function () {
                return leftZeroFill(~~(this.milliseconds() / 10), 2);
            },
            SSS  : function () {
                return leftZeroFill(this.milliseconds(), 3);
            },
            Z    : function () {
                var a = -this.zone(),
                    b = "+";
                if (a < 0) {
                    a = -a;
                    b = "-";
                }
                return b + leftZeroFill(~~(a / 60), 2) + ":" + leftZeroFill(~~a % 60, 2);
            },
            ZZ   : function () {
                var a = -this.zone(),
                    b = "+";
                if (a < 0) {
                    a = -a;
                    b = "-";
                }
                return b + leftZeroFill(~~(10 * a / 6), 4);
            },
            z : function () {
                return this.zoneAbbr();
            },
            zz : function () {
                return this.zoneName();
            },
            X    : function () {
                return this.unix();
            }
        };

    function padToken(func, count) {
        return function (a) {
            return leftZeroFill(func.call(this, a), count);
        };
    }
    function ordinalizeToken(func, period) {
        return function (a) {
            return this.lang().ordinal(func.call(this, a), period);
        };
    }

    while (ordinalizeTokens.length) {
        i = ordinalizeTokens.pop();
        formatTokenFunctions[i + 'o'] = ordinalizeToken(formatTokenFunctions[i], i);
    }
    while (paddedTokens.length) {
        i = paddedTokens.pop();
        formatTokenFunctions[i + i] = padToken(formatTokenFunctions[i], 2);
    }
    formatTokenFunctions.DDDD = padToken(formatTokenFunctions.DDD, 3);


    /************************************
        Constructors
    ************************************/

    function Language() {

    }

    // Moment prototype object
    function Moment(config) {
        extend(this, config);
    }

    // Duration Constructor
    function Duration(duration) {
        var years = duration.years || duration.year || duration.y || 0,
            months = duration.months || duration.month || duration.M || 0,
            weeks = duration.weeks || duration.week || duration.w || 0,
            days = duration.days || duration.day || duration.d || 0,
            hours = duration.hours || duration.hour || duration.h || 0,
            minutes = duration.minutes || duration.minute || duration.m || 0,
            seconds = duration.seconds || duration.second || duration.s || 0,
            milliseconds = duration.milliseconds || duration.millisecond || duration.ms || 0;

        // store reference to input for deterministic cloning
        this._input = duration;

        // representation for dateAddRemove
        this._milliseconds = milliseconds +
            seconds * 1e3 + // 1000
            minutes * 6e4 + // 1000 * 60
            hours * 36e5; // 1000 * 60 * 60
        // Because of dateAddRemove treats 24 hours as different from a
        // day when working around DST, we need to store them separately
        this._days = days +
            weeks * 7;
        // It is impossible translate months into days without knowing
        // which months you are are talking about, so we have to store
        // it separately.
        this._months = months +
            years * 12;

        this._data = {};

        this._bubble();
    }


    /************************************
        Helpers
    ************************************/


    function extend(a, b) {
        for (var i in b) {
            if (b.hasOwnProperty(i)) {
                a[i] = b[i];
            }
        }
        return a;
    }

    function absRound(number) {
        if (number < 0) {
            return Math.ceil(number);
        } else {
            return Math.floor(number);
        }
    }

    // left zero fill a number
    // see http://jsperf.com/left-zero-filling for performance comparison
    function leftZeroFill(number, targetLength) {
        var output = number + '';
        while (output.length < targetLength) {
            output = '0' + output;
        }
        return output;
    }

    // helper function for _.addTime and _.subtractTime
    function addOrSubtractDurationFromMoment(mom, duration, isAdding, ignoreUpdateOffset) {
        var milliseconds = duration._milliseconds,
            days = duration._days,
            months = duration._months,
            minutes,
            hours,
            currentDate;

        if (milliseconds) {
            mom._d.setTime(+mom._d + milliseconds * isAdding);
        }
        // store the minutes and hours so we can restore them
        if (days || months) {
            minutes = mom.minute();
            hours = mom.hour();
        }
        if (days) {
            mom.date(mom.date() + days * isAdding);
        }
        if (months) {
            mom.month(mom.month() + months * isAdding);
        }
        if (milliseconds && !ignoreUpdateOffset) {
            moment.updateOffset(mom);
        }
        // restore the minutes and hours after possibly changing dst
        if (days || months) {
            mom.minute(minutes);
            mom.hour(hours);
        }
    }

    // check if is an array
    function isArray(input) {
        return Object.prototype.toString.call(input) === '[object Array]';
    }

    // compare two arrays, return the number of differences
    function compareArrays(array1, array2) {
        var len = Math.min(array1.length, array2.length),
            lengthDiff = Math.abs(array1.length - array2.length),
            diffs = 0,
            i;
        for (i = 0; i < len; i++) {
            if (~~array1[i] !== ~~array2[i]) {
                diffs++;
            }
        }
        return diffs + lengthDiff;
    }

    function normalizeUnits(units) {
        return units ? unitAliases[units] || units.toLowerCase().replace(/(.)s$/, '$1') : units;
    }


    /************************************
        Languages
    ************************************/


    Language.prototype = {
        set : function (config) {
            var prop, i;
            for (i in config) {
                prop = config[i];
                if (typeof prop === 'function') {
                    this[i] = prop;
                } else {
                    this['_' + i] = prop;
                }
            }
        },

        _months : "January_February_March_April_May_June_July_August_September_October_November_December".split("_"),
        months : function (m) {
            return this._months[m.month()];
        },

        _monthsShort : "Jan_Feb_Mar_Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_Dec".split("_"),
        monthsShort : function (m) {
            return this._monthsShort[m.month()];
        },

        monthsParse : function (monthName) {
            var i, mom, regex;

            if (!this._monthsParse) {
                this._monthsParse = [];
            }

            for (i = 0; i < 12; i++) {
                // make the regex if we don't have it already
                if (!this._monthsParse[i]) {
                    mom = moment([2000, i]);
                    regex = '^' + this.months(mom, '') + '|^' + this.monthsShort(mom, '');
                    this._monthsParse[i] = new RegExp(regex.replace('.', ''), 'i');
                }
                // test the regex
                if (this._monthsParse[i].test(monthName)) {
                    return i;
                }
            }
        },

        _weekdays : "Sunday_Monday_Tuesday_Wednesday_Thursday_Friday_Saturday".split("_"),
        weekdays : function (m) {
            return this._weekdays[m.day()];
        },

        _weekdaysShort : "Sun_Mon_Tue_Wed_Thu_Fri_Sat".split("_"),
        weekdaysShort : function (m) {
            return this._weekdaysShort[m.day()];
        },

        _weekdaysMin : "Su_Mo_Tu_We_Th_Fr_Sa".split("_"),
        weekdaysMin : function (m) {
            return this._weekdaysMin[m.day()];
        },

        weekdaysParse : function (weekdayName) {
            var i, mom, regex;

            if (!this._weekdaysParse) {
                this._weekdaysParse = [];
            }

            for (i = 0; i < 7; i++) {
                // make the regex if we don't have it already
                if (!this._weekdaysParse[i]) {
                    mom = moment([2000, 1]).day(i);
                    regex = '^' + this.weekdays(mom, '') + '|^' + this.weekdaysShort(mom, '') + '|^' + this.weekdaysMin(mom, '');
                    this._weekdaysParse[i] = new RegExp(regex.replace('.', ''), 'i');
                }
                // test the regex
                if (this._weekdaysParse[i].test(weekdayName)) {
                    return i;
                }
            }
        },

        _longDateFormat : {
            LT : "h:mm A",
            L : "MM/DD/YYYY",
            LL : "MMMM D YYYY",
            LLL : "MMMM D YYYY LT",
            LLLL : "dddd, MMMM D YYYY LT"
        },
        longDateFormat : function (key) {
            var output = this._longDateFormat[key];
            if (!output && this._longDateFormat[key.toUpperCase()]) {
                output = this._longDateFormat[key.toUpperCase()].replace(/MMMM|MM|DD|dddd/g, function (val) {
                    return val.slice(1);
                });
                this._longDateFormat[key] = output;
            }
            return output;
        },

        isPM : function (input) {
            return ((input + '').toLowerCase()[0] === 'p');
        },

        _meridiemParse : /[ap]\.?m?\.?/i,
        meridiem : function (hours, minutes, isLower) {
            if (hours > 11) {
                return isLower ? 'pm' : 'PM';
            } else {
                return isLower ? 'am' : 'AM';
            }
        },

        _calendar : {
            sameDay : '[Today at] LT',
            nextDay : '[Tomorrow at] LT',
            nextWeek : 'dddd [at] LT',
            lastDay : '[Yesterday at] LT',
            lastWeek : '[Last] dddd [at] LT',
            sameElse : 'L'
        },
        calendar : function (key, mom) {
            var output = this._calendar[key];
            return typeof output === 'function' ? output.apply(mom) : output;
        },

        _relativeTime : {
            future : "in %s",
            past : "%s ago",
            s : "a few seconds",
            m : "a minute",
            mm : "%d minutes",
            h : "an hour",
            hh : "%d hours",
            d : "a day",
            dd : "%d days",
            M : "a month",
            MM : "%d months",
            y : "a year",
            yy : "%d years"
        },
        relativeTime : function (number, withoutSuffix, string, isFuture) {
            var output = this._relativeTime[string];
            return (typeof output === 'function') ?
                output(number, withoutSuffix, string, isFuture) :
                output.replace(/%d/i, number);
        },
        pastFuture : function (diff, output) {
            var format = this._relativeTime[diff > 0 ? 'future' : 'past'];
            return typeof format === 'function' ? format(output) : format.replace(/%s/i, output);
        },

        ordinal : function (number) {
            return this._ordinal.replace("%d", number);
        },
        _ordinal : "%d",

        preparse : function (string) {
            return string;
        },

        postformat : function (string) {
            return string;
        },

        week : function (mom) {
            return weekOfYear(mom, this._week.dow, this._week.doy).week;
        },
        _week : {
            dow : 0, // Sunday is the first day of the week.
            doy : 6  // The week that contains Jan 1st is the first week of the year.
        }
    };

    // Loads a language definition into the `languages` cache.  The function
    // takes a key and optionally values.  If not in the browser and no values
    // are provided, it will load the language file module.  As a convenience,
    // this function also returns the language values.
    function loadLang(key, values) {
        values.abbr = key;
        if (!languages[key]) {
            languages[key] = new Language();
        }
        languages[key].set(values);
        return languages[key];
    }

    // Determines which language definition to use and returns it.
    //
    // With no parameters, it will return the global language.  If you
    // pass in a language key, such as 'en', it will return the
    // definition for 'en', so long as 'en' has already been loaded using
    // moment.lang.
    function getLangDefinition(key) {
        if (!key) {
            return moment.fn._lang;
        }
        if (!languages[key] && hasModule) {
            try {
                require('./lang/' + key);
            } catch (e) {
                // call with no params to set to default
                return moment.fn._lang;
            }
        }
        return languages[key];
    }


    /************************************
        Formatting
    ************************************/


    function removeFormattingTokens(input) {
        if (input.match(/\[.*\]/)) {
            return input.replace(/^\[|\]$/g, "");
        }
        return input.replace(/\\/g, "");
    }

    function makeFormatFunction(format) {
        var array = format.match(formattingTokens), i, length;

        for (i = 0, length = array.length; i < length; i++) {
            if (formatTokenFunctions[array[i]]) {
                array[i] = formatTokenFunctions[array[i]];
            } else {
                array[i] = removeFormattingTokens(array[i]);
            }
        }

        return function (mom) {
            var output = "";
            for (i = 0; i < length; i++) {
                output += array[i] instanceof Function ? array[i].call(mom, format) : array[i];
            }
            return output;
        };
    }

    // format date using native date object
    function formatMoment(m, format) {
        var i = 5;

        function replaceLongDateFormatTokens(input) {
            return m.lang().longDateFormat(input) || input;
        }

        while (i-- && localFormattingTokens.test(format)) {
            format = format.replace(localFormattingTokens, replaceLongDateFormatTokens);
        }

        if (!formatFunctions[format]) {
            formatFunctions[format] = makeFormatFunction(format);
        }

        return formatFunctions[format](m);
    }


    /************************************
        Parsing
    ************************************/


    // get the regex to find the next token
    function getParseRegexForToken(token, config) {
        switch (token) {
        case 'DDDD':
            return parseTokenThreeDigits;
        case 'YYYY':
            return parseTokenFourDigits;
        case 'YYYYY':
            return parseTokenSixDigits;
        case 'S':
        case 'SS':
        case 'SSS':
        case 'DDD':
            return parseTokenOneToThreeDigits;
        case 'MMM':
        case 'MMMM':
        case 'dd':
        case 'ddd':
        case 'dddd':
            return parseTokenWord;
        case 'a':
        case 'A':
            return getLangDefinition(config._l)._meridiemParse;
        case 'X':
            return parseTokenTimestampMs;
        case 'Z':
        case 'ZZ':
            return parseTokenTimezone;
        case 'T':
            return parseTokenT;
        case 'MM':
        case 'DD':
        case 'YY':
        case 'HH':
        case 'hh':
        case 'mm':
        case 'ss':
        case 'M':
        case 'D':
        case 'd':
        case 'H':
        case 'h':
        case 'm':
        case 's':
            return parseTokenOneOrTwoDigits;
        default :
            return new RegExp(token.replace('\\', ''));
        }
    }

    function timezoneMinutesFromString(string) {
        var tzchunk = (parseTokenTimezone.exec(string) || [])[0],
            parts = (tzchunk + '').match(parseTimezoneChunker) || ['-', 0, 0],
            minutes = +(parts[1] * 60) + ~~parts[2];

        return parts[0] === '+' ? -minutes : minutes;
    }

    // function to convert string input to date
    function addTimeToArrayFromToken(token, input, config) {
        var a, datePartArray = config._a;

        switch (token) {
        // MONTH
        case 'M' : // fall through to MM
        case 'MM' :
            datePartArray[1] = (input == null) ? 0 : ~~input - 1;
            break;
        case 'MMM' : // fall through to MMMM
        case 'MMMM' :
            a = getLangDefinition(config._l).monthsParse(input);
            // if we didn't find a month name, mark the date as invalid.
            if (a != null) {
                datePartArray[1] = a;
            } else {
                config._isValid = false;
            }
            break;
        // DAY OF MONTH
        case 'D' : // fall through to DDDD
        case 'DD' : // fall through to DDDD
        case 'DDD' : // fall through to DDDD
        case 'DDDD' :
            if (input != null) {
                datePartArray[2] = ~~input;
            }
            break;
        // YEAR
        case 'YY' :
            datePartArray[0] = ~~input + (~~input > 68 ? 1900 : 2000);
            break;
        case 'YYYY' :
        case 'YYYYY' :
            datePartArray[0] = ~~input;
            break;
        // AM / PM
        case 'a' : // fall through to A
        case 'A' :
            config._isPm = getLangDefinition(config._l).isPM(input);
            break;
        // 24 HOUR
        case 'H' : // fall through to hh
        case 'HH' : // fall through to hh
        case 'h' : // fall through to hh
        case 'hh' :
            datePartArray[3] = ~~input;
            break;
        // MINUTE
        case 'm' : // fall through to mm
        case 'mm' :
            datePartArray[4] = ~~input;
            break;
        // SECOND
        case 's' : // fall through to ss
        case 'ss' :
            datePartArray[5] = ~~input;
            break;
        // MILLISECOND
        case 'S' :
        case 'SS' :
        case 'SSS' :
            datePartArray[6] = ~~ (('0.' + input) * 1000);
            break;
        // UNIX TIMESTAMP WITH MS
        case 'X':
            config._d = new Date(parseFloat(input) * 1000);
            break;
        // TIMEZONE
        case 'Z' : // fall through to ZZ
        case 'ZZ' :
            config._useUTC = true;
            config._tzm = timezoneMinutesFromString(input);
            break;
        }

        // if the input is null, the date is not valid
        if (input == null) {
            config._isValid = false;
        }
    }

    // convert an array to a date.
    // the array should mirror the parameters below
    // note: all values past the year are optional and will default to the lowest possible value.
    // [year, month, day , hour, minute, second, millisecond]
    function dateFromArray(config) {
        var i, date, input = [];

        if (config._d) {
            return;
        }

        for (i = 0; i < 7; i++) {
            config._a[i] = input[i] = (config._a[i] == null) ? (i === 2 ? 1 : 0) : config._a[i];
        }

        // add the offsets to the time to be parsed so that we can have a clean array for checking isValid
        input[3] += ~~((config._tzm || 0) / 60);
        input[4] += ~~((config._tzm || 0) % 60);

        date = new Date(0);

        if (config._useUTC) {
            date.setUTCFullYear(input[0], input[1], input[2]);
            date.setUTCHours(input[3], input[4], input[5], input[6]);
        } else {
            date.setFullYear(input[0], input[1], input[2]);
            date.setHours(input[3], input[4], input[5], input[6]);
        }

        config._d = date;
    }

    // date from string and format string
    function makeDateFromStringAndFormat(config) {
        // This array is used to make a Date, either with `new Date` or `Date.UTC`
        var tokens = config._f.match(formattingTokens),
            string = config._i,
            i, parsedInput;

        config._a = [];

        for (i = 0; i < tokens.length; i++) {
            parsedInput = (getParseRegexForToken(tokens[i], config).exec(string) || [])[0];
            if (parsedInput) {
                string = string.slice(string.indexOf(parsedInput) + parsedInput.length);
            }
            // don't parse if its not a known token
            if (formatTokenFunctions[tokens[i]]) {
                addTimeToArrayFromToken(tokens[i], parsedInput, config);
            }
        }

        // add remaining unparsed input to the string
        if (string) {
            config._il = string;
        }

        // handle am pm
        if (config._isPm && config._a[3] < 12) {
            config._a[3] += 12;
        }
        // if is 12 am, change hours to 0
        if (config._isPm === false && config._a[3] === 12) {
            config._a[3] = 0;
        }
        // return
        dateFromArray(config);
    }

    // date from string and array of format strings
    function makeDateFromStringAndArray(config) {
        var tempConfig,
            tempMoment,
            bestMoment,

            scoreToBeat = 99,
            i,
            currentScore;

        for (i = 0; i < config._f.length; i++) {
            tempConfig = extend({}, config);
            tempConfig._f = config._f[i];
            makeDateFromStringAndFormat(tempConfig);
            tempMoment = new Moment(tempConfig);

            currentScore = compareArrays(tempConfig._a, tempMoment.toArray());

            // if there is any input that was not parsed
            // add a penalty for that format
            if (tempMoment._il) {
                currentScore += tempMoment._il.length;
            }

            if (currentScore < scoreToBeat) {
                scoreToBeat = currentScore;
                bestMoment = tempMoment;
            }
        }

        extend(config, bestMoment);
    }

    // date from iso format
    function makeDateFromString(config) {
        var i,
            string = config._i,
            match = isoRegex.exec(string);

        if (match) {
            // match[2] should be "T" or undefined
            config._f = 'YYYY-MM-DD' + (match[2] || " ");
            for (i = 0; i < 4; i++) {
                if (isoTimes[i][1].exec(string)) {
                    config._f += isoTimes[i][0];
                    break;
                }
            }
            if (parseTokenTimezone.exec(string)) {
                config._f += " Z";
            }
            makeDateFromStringAndFormat(config);
        } else {
            config._d = new Date(string);
        }
    }

    function makeDateFromInput(config) {
        var input = config._i,
            matched = aspNetJsonRegex.exec(input);

        if (input === undefined) {
            config._d = new Date();
        } else if (matched) {
            config._d = new Date(+matched[1]);
        } else if (typeof input === 'string') {
            makeDateFromString(config);
        } else if (isArray(input)) {
            config._a = input.slice(0);
            dateFromArray(config);
        } else {
            config._d = input instanceof Date ? new Date(+input) : new Date(input);
        }
    }


    /************************************
        Relative Time
    ************************************/


    // helper function for moment.fn.from, moment.fn.fromNow, and moment.duration.fn.humanize
    function substituteTimeAgo(string, number, withoutSuffix, isFuture, lang) {
        return lang.relativeTime(number || 1, !!withoutSuffix, string, isFuture);
    }

    function relativeTime(milliseconds, withoutSuffix, lang) {
        var seconds = round(Math.abs(milliseconds) / 1000),
            minutes = round(seconds / 60),
            hours = round(minutes / 60),
            days = round(hours / 24),
            years = round(days / 365),
            args = seconds < 45 && ['s', seconds] ||
                minutes === 1 && ['m'] ||
                minutes < 45 && ['mm', minutes] ||
                hours === 1 && ['h'] ||
                hours < 22 && ['hh', hours] ||
                days === 1 && ['d'] ||
                days <= 25 && ['dd', days] ||
                days <= 45 && ['M'] ||
                days < 345 && ['MM', round(days / 30)] ||
                years === 1 && ['y'] || ['yy', years];
        args[2] = withoutSuffix;
        args[3] = milliseconds > 0;
        args[4] = lang;
        return substituteTimeAgo.apply({}, args);
    }


    /************************************
        Week of Year
    ************************************/


    // firstDayOfWeek       0 = sun, 6 = sat
    //                      the day of the week that starts the week
    //                      (usually sunday or monday)
    // firstDayOfWeekOfYear 0 = sun, 6 = sat
    //                      the first week is the week that contains the first
    //                      of this day of the week
    //                      (eg. ISO weeks use thursday (4))
    function weekOfYear(mom, firstDayOfWeek, firstDayOfWeekOfYear) {
        var end = firstDayOfWeekOfYear - firstDayOfWeek,
            daysToDayOfWeek = firstDayOfWeekOfYear - mom.day(),
            adjustedMoment;


        if (daysToDayOfWeek > end) {
            daysToDayOfWeek -= 7;
        }

        if (daysToDayOfWeek < end - 7) {
            daysToDayOfWeek += 7;
        }

        adjustedMoment = moment(mom).add('d', daysToDayOfWeek);
        return {
            week: Math.ceil(adjustedMoment.dayOfYear() / 7),
            year: adjustedMoment.year()
        };
    }


    /************************************
        Top Level Functions
    ************************************/

    function makeMoment(config) {
        var input = config._i,
            format = config._f;

        if (input === null || input === '') {
            return null;
        }

        if (typeof input === 'string') {
            config._i = input = getLangDefinition().preparse(input);
        }

        if (moment.isMoment(input)) {
            config = extend({}, input);
            config._d = new Date(+input._d);
        } else if (format) {
            if (isArray(format)) {
                makeDateFromStringAndArray(config);
            } else {
                makeDateFromStringAndFormat(config);
            }
        } else {
            makeDateFromInput(config);
        }

        return new Moment(config);
    }

    moment = function (input, format, lang) {
        return makeMoment({
            _i : input,
            _f : format,
            _l : lang,
            _isUTC : false
        });
    };

    // creating with utc
    moment.utc = function (input, format, lang) {
        return makeMoment({
            _useUTC : true,
            _isUTC : true,
            _l : lang,
            _i : input,
            _f : format
        });
    };

    // creating with unix timestamp (in seconds)
    moment.unix = function (input) {
        return moment(input * 1000);
    };

    // duration
    moment.duration = function (input, key) {
        var isDuration = moment.isDuration(input),
            isNumber = (typeof input === 'number'),
            duration = (isDuration ? input._input : (isNumber ? {} : input)),
            matched = aspNetTimeSpanJsonRegex.exec(input),
            sign,
            ret;

        if (isNumber) {
            if (key) {
                duration[key] = input;
            } else {
                duration.milliseconds = input;
            }
        } else if (matched) {
            sign = (matched[1] === "-") ? -1 : 1;
            duration = {
                y: 0,
                d: ~~matched[2] * sign,
                h: ~~matched[3] * sign,
                m: ~~matched[4] * sign,
                s: ~~matched[5] * sign,
                ms: ~~matched[6] * sign
            };
        }

        ret = new Duration(duration);

        if (isDuration && input.hasOwnProperty('_lang')) {
            ret._lang = input._lang;
        }

        return ret;
    };

    // version number
    moment.version = VERSION;

    // default format
    moment.defaultFormat = isoFormat;

    // This function will be called whenever a moment is mutated.
    // It is intended to keep the offset in sync with the timezone.
    moment.updateOffset = function () {};

    // This function will load languages and then set the global language.  If
    // no arguments are passed in, it will simply return the current global
    // language key.
    moment.lang = function (key, values) {
        if (!key) {
            return moment.fn._lang._abbr;
        }
        if (values) {
            loadLang(key, values);
        } else if (!languages[key]) {
            getLangDefinition(key);
        }
        moment.duration.fn._lang = moment.fn._lang = getLangDefinition(key);
    };

    // returns language data
    moment.langData = function (key) {
        if (key && key._lang && key._lang._abbr) {
            key = key._lang._abbr;
        }
        return getLangDefinition(key);
    };

    // compare moment object
    moment.isMoment = function (obj) {
        return obj instanceof Moment;
    };

    // for typechecking Duration objects
    moment.isDuration = function (obj) {
        return obj instanceof Duration;
    };


    /************************************
        Moment Prototype
    ************************************/


    moment.fn = Moment.prototype = {

        clone : function () {
            return moment(this);
        },

        valueOf : function () {
            return +this._d + ((this._offset || 0) * 60000);
        },

        unix : function () {
            return Math.floor(+this / 1000);
        },

        toString : function () {
            return this.format("ddd MMM DD YYYY HH:mm:ss [GMT]ZZ");
        },

        toDate : function () {
            return this._offset ? new Date(+this) : this._d;
        },

        toISOString : function () {
            return formatMoment(moment(this).utc(), 'YYYY-MM-DD[T]HH:mm:ss.SSS[Z]');
        },

        toArray : function () {
            var m = this;
            return [
                m.year(),
                m.month(),
                m.date(),
                m.hours(),
                m.minutes(),
                m.seconds(),
                m.milliseconds()
            ];
        },

        isValid : function () {
            if (this._isValid == null) {
                if (this._a) {
                    this._isValid = !compareArrays(this._a, (this._isUTC ? moment.utc(this._a) : moment(this._a)).toArray());
                } else {
                    this._isValid = !isNaN(this._d.getTime());
                }
            }
            return !!this._isValid;
        },

        utc : function () {
            return this.zone(0);
        },

        local : function () {
            this.zone(0);
            this._isUTC = false;
            return this;
        },

        format : function (inputString) {
            var output = formatMoment(this, inputString || moment.defaultFormat);
            return this.lang().postformat(output);
        },

        add : function (input, val) {
            var dur;
            // switch args to support add('s', 1) and add(1, 's')
            if (typeof input === 'string') {
                dur = moment.duration(+val, input);
            } else {
                dur = moment.duration(input, val);
            }
            addOrSubtractDurationFromMoment(this, dur, 1);
            return this;
        },

        subtract : function (input, val) {
            var dur;
            // switch args to support subtract('s', 1) and subtract(1, 's')
            if (typeof input === 'string') {
                dur = moment.duration(+val, input);
            } else {
                dur = moment.duration(input, val);
            }
            addOrSubtractDurationFromMoment(this, dur, -1);
            return this;
        },

        diff : function (input, units, asFloat) {
            var that = this._isUTC ? moment(input).zone(this._offset || 0) : moment(input).local(),
                zoneDiff = (this.zone() - that.zone()) * 6e4,
                diff, output;

            units = normalizeUnits(units);

            if (units === 'year' || units === 'month') {
                // average number of days in the months in the given dates
                diff = (this.daysInMonth() + that.daysInMonth()) * 432e5; // 24 * 60 * 60 * 1000 / 2
                // difference in months
                output = ((this.year() - that.year()) * 12) + (this.month() - that.month());
                // adjust by taking difference in days, average number of days
                // and dst in the given months.
                output += ((this - moment(this).startOf('month')) -
                        (that - moment(that).startOf('month'))) / diff;
                // same as above but with zones, to negate all dst
                output -= ((this.zone() - moment(this).startOf('month').zone()) -
                        (that.zone() - moment(that).startOf('month').zone())) * 6e4 / diff;
                if (units === 'year') {
                    output = output / 12;
                }
            } else {
                diff = (this - that);
                output = units === 'second' ? diff / 1e3 : // 1000
                    units === 'minute' ? diff / 6e4 : // 1000 * 60
                    units === 'hour' ? diff / 36e5 : // 1000 * 60 * 60
                    units === 'day' ? (diff - zoneDiff) / 864e5 : // 1000 * 60 * 60 * 24, negate dst
                    units === 'week' ? (diff - zoneDiff) / 6048e5 : // 1000 * 60 * 60 * 24 * 7, negate dst
                    diff;
            }
            return asFloat ? output : absRound(output);
        },

        from : function (time, withoutSuffix) {
            return moment.duration(this.diff(time)).lang(this.lang()._abbr).humanize(!withoutSuffix);
        },

        fromNow : function (withoutSuffix) {
            return this.from(moment(), withoutSuffix);
        },

        calendar : function () {
            var diff = this.diff(moment().startOf('day'), 'days', true),
                format = diff < -6 ? 'sameElse' :
                diff < -1 ? 'lastWeek' :
                diff < 0 ? 'lastDay' :
                diff < 1 ? 'sameDay' :
                diff < 2 ? 'nextDay' :
                diff < 7 ? 'nextWeek' : 'sameElse';
            return this.format(this.lang().calendar(format, this));
        },

        isLeapYear : function () {
            var year = this.year();
            return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
        },

        isDST : function () {
            return (this.zone() < this.clone().month(0).zone() ||
                this.zone() < this.clone().month(5).zone());
        },

        day : function (input) {
            var day = this._isUTC ? this._d.getUTCDay() : this._d.getDay();
            if (input != null) {
                if (typeof input === 'string') {
                    input = this.lang().weekdaysParse(input);
                    if (typeof input !== 'number') {
                        return this;
                    }
                }
                return this.add({ d : input - day });
            } else {
                return day;
            }
        },

        month : function (input) {
            var utc = this._isUTC ? 'UTC' : '',
                dayOfMonth,
                daysInMonth;

            if (input != null) {
                if (typeof input === 'string') {
                    input = this.lang().monthsParse(input);
                    if (typeof input !== 'number') {
                        return this;
                    }
                }

                dayOfMonth = this.date();
                this.date(1);
                this._d['set' + utc + 'Month'](input);
                this.date(Math.min(dayOfMonth, this.daysInMonth()));

                moment.updateOffset(this);
                return this;
            } else {
                return this._d['get' + utc + 'Month']();
            }
        },

        startOf: function (units) {
            units = normalizeUnits(units);
            // the following switch intentionally omits break keywords
            // to utilize falling through the cases.
            switch (units) {
            case 'year':
                this.month(0);
                /* falls through */
            case 'month':
                this.date(1);
                /* falls through */
            case 'week':
            case 'day':
                this.hours(0);
                /* falls through */
            case 'hour':
                this.minutes(0);
                /* falls through */
            case 'minute':
                this.seconds(0);
                /* falls through */
            case 'second':
                this.milliseconds(0);
                /* falls through */
            }

            // weeks are a special case
            if (units === 'week') {
                this.weekday(0);
            }

            return this;
        },

        endOf: function (units) {
            return this.startOf(units).add(units, 1).subtract('ms', 1);
        },

        isAfter: function (input, units) {
            units = typeof units !== 'undefined' ? units : 'millisecond';
            return +this.clone().startOf(units) > +moment(input).startOf(units);
        },

        isBefore: function (input, units) {
            units = typeof units !== 'undefined' ? units : 'millisecond';
            return +this.clone().startOf(units) < +moment(input).startOf(units);
        },

        isSame: function (input, units) {
            units = typeof units !== 'undefined' ? units : 'millisecond';
            return +this.clone().startOf(units) === +moment(input).startOf(units);
        },

        min: function (other) {
            other = moment.apply(null, arguments);
            return other < this ? this : other;
        },

        max: function (other) {
            other = moment.apply(null, arguments);
            return other > this ? this : other;
        },

        zone : function (input) {
            var offset = this._offset || 0;
            if (input != null) {
                if (typeof input === "string") {
                    input = timezoneMinutesFromString(input);
                }
                if (Math.abs(input) < 16) {
                    input = input * 60;
                }
                this._offset = input;
                this._isUTC = true;
                if (offset !== input) {
                    addOrSubtractDurationFromMoment(this, moment.duration(offset - input, 'm'), 1, true);
                }
            } else {
                return this._isUTC ? offset : this._d.getTimezoneOffset();
            }
            return this;
        },

        zoneAbbr : function () {
            return this._isUTC ? "UTC" : "";
        },

        zoneName : function () {
            return this._isUTC ? "Coordinated Universal Time" : "";
        },

        daysInMonth : function () {
            return moment.utc([this.year(), this.month() + 1, 0]).date();
        },

        dayOfYear : function (input) {
            var dayOfYear = round((moment(this).startOf('day') - moment(this).startOf('year')) / 864e5) + 1;
            return input == null ? dayOfYear : this.add("d", (input - dayOfYear));
        },

        weekYear : function (input) {
            var year = weekOfYear(this, this.lang()._week.dow, this.lang()._week.doy).year;
            return input == null ? year : this.add("y", (input - year));
        },

        isoWeekYear : function (input) {
            var year = weekOfYear(this, 1, 4).year;
            return input == null ? year : this.add("y", (input - year));
        },

        week : function (input) {
            var week = this.lang().week(this);
            return input == null ? week : this.add("d", (input - week) * 7);
        },

        isoWeek : function (input) {
            var week = weekOfYear(this, 1, 4).week;
            return input == null ? week : this.add("d", (input - week) * 7);
        },

        weekday : function (input) {
            var weekday = (this._d.getDay() + 7 - this.lang()._week.dow) % 7;
            return input == null ? weekday : this.add("d", input - weekday);
        },

        isoWeekday : function (input) {
            // behaves the same as moment#day except
            // as a getter, returns 7 instead of 0 (1-7 range instead of 0-6)
            // as a setter, sunday should belong to the previous week.
            return input == null ? this.day() || 7 : this.day(this.day() % 7 ? input : input - 7);
        },

        // If passed a language key, it will set the language for this
        // instance.  Otherwise, it will return the language configuration
        // variables for this instance.
        lang : function (key) {
            if (key === undefined) {
                return this._lang;
            } else {
                this._lang = getLangDefinition(key);
                return this;
            }
        }
    };

    // helper for adding shortcuts
    function makeGetterAndSetter(name, key) {
        moment.fn[name] = moment.fn[name + 's'] = function (input) {
            var utc = this._isUTC ? 'UTC' : '';
            if (input != null) {
                this._d['set' + utc + key](input);
                moment.updateOffset(this);
                return this;
            } else {
                return this._d['get' + utc + key]();
            }
        };
    }

    // loop through and add shortcuts (Month, Date, Hours, Minutes, Seconds, Milliseconds)
    for (i = 0; i < proxyGettersAndSetters.length; i ++) {
        makeGetterAndSetter(proxyGettersAndSetters[i].toLowerCase().replace(/s$/, ''), proxyGettersAndSetters[i]);
    }

    // add shortcut for year (uses different syntax than the getter/setter 'year' == 'FullYear')
    makeGetterAndSetter('year', 'FullYear');

    // add plural methods
    moment.fn.days = moment.fn.day;
    moment.fn.months = moment.fn.month;
    moment.fn.weeks = moment.fn.week;
    moment.fn.isoWeeks = moment.fn.isoWeek;

    // add aliased format methods
    moment.fn.toJSON = moment.fn.toISOString;

    /************************************
        Duration Prototype
    ************************************/


    moment.duration.fn = Duration.prototype = {
        _bubble : function () {
            var milliseconds = this._milliseconds,
                days = this._days,
                months = this._months,
                data = this._data,
                seconds, minutes, hours, years;

            // The following code bubbles up values, see the tests for
            // examples of what that means.
            data.milliseconds = milliseconds % 1000;

            seconds = absRound(milliseconds / 1000);
            data.seconds = seconds % 60;

            minutes = absRound(seconds / 60);
            data.minutes = minutes % 60;

            hours = absRound(minutes / 60);
            data.hours = hours % 24;

            days += absRound(hours / 24);
            data.days = days % 30;

            months += absRound(days / 30);
            data.months = months % 12;

            years = absRound(months / 12);
            data.years = years;
        },

        weeks : function () {
            return absRound(this.days() / 7);
        },

        valueOf : function () {
            return this._milliseconds +
              this._days * 864e5 +
              (this._months % 12) * 2592e6 +
              ~~(this._months / 12) * 31536e6;
        },

        humanize : function (withSuffix) {
            var difference = +this,
                output = relativeTime(difference, !withSuffix, this.lang());

            if (withSuffix) {
                output = this.lang().pastFuture(difference, output);
            }

            return this.lang().postformat(output);
        },

        add : function (input, val) {
            // supports only 2.0-style add(1, 's') or add(moment)
            var dur = moment.duration(input, val);

            this._milliseconds += dur._milliseconds;
            this._days += dur._days;
            this._months += dur._months;

            this._bubble();

            return this;
        },

        subtract : function (input, val) {
            var dur = moment.duration(input, val);

            this._milliseconds -= dur._milliseconds;
            this._days -= dur._days;
            this._months -= dur._months;

            this._bubble();

            return this;
        },

        get : function (units) {
            units = normalizeUnits(units);
            return this[units.toLowerCase() + 's']();
        },

        as : function (units) {
            units = normalizeUnits(units);
            return this['as' + units.charAt(0).toUpperCase() + units.slice(1) + 's']();
        },

        lang : moment.fn.lang
    };

    function makeDurationGetter(name) {
        moment.duration.fn[name] = function () {
            return this._data[name];
        };
    }

    function makeDurationAsGetter(name, factor) {
        moment.duration.fn['as' + name] = function () {
            return +this / factor;
        };
    }

    for (i in unitMillisecondFactors) {
        if (unitMillisecondFactors.hasOwnProperty(i)) {
            makeDurationAsGetter(i, unitMillisecondFactors[i]);
            makeDurationGetter(i.toLowerCase());
        }
    }

    makeDurationAsGetter('Weeks', 6048e5);
    moment.duration.fn.asMonths = function () {
        return (+this - this.years() * 31536e6) / 2592e6 + this.years() * 12;
    };


    /************************************
        Default Lang
    ************************************/


    // Set default language, other languages will inherit from English.
    moment.lang('en', {
        ordinal : function (number) {
            var b = number % 10,
                output = (~~ (number % 100 / 10) === 1) ? 'th' :
                (b === 1) ? 'st' :
                (b === 2) ? 'nd' :
                (b === 3) ? 'rd' : 'th';
            return number + output;
        }
    });


    /************************************
        Exposing Moment
    ************************************/


    // CommonJS module is defined
    if (hasModule) {
        module.exports = moment;
    }
    /*global ender:false */
    if (typeof ender === 'undefined') {
        // here, `this` means `window` in the browser, or `global` on the server
        // add `moment` as a global object via a string identifier,
        // for Closure Compiler "advanced" mode
        this['moment'] = moment;
    }
    /*global define:false */
    if (typeof define === "function" && define.amd) {
        define("moment", [], function () {
            return moment;
        });
    }
}).call(this);
;
// ┌────────────────────────────────────────────────────────────────────┐ \\
// │ Raphaël 2.1.0 - JavaScript Vector Library                          │ \\
// ├────────────────────────────────────────────────────────────────────┤ \\
// │ Copyright © 2008-2012 Dmitry Baranovskiy (http://raphaeljs.com)    │ \\
// │ Copyright © 2008-2012 Sencha Labs (http://sencha.com)              │ \\
// ├────────────────────────────────────────────────────────────────────┤ \\
// │ Licensed under the MIT (http://raphaeljs.com/license.html) license.│ \\
// └────────────────────────────────────────────────────────────────────┘ \\

(function(a){var b="0.3.4",c="hasOwnProperty",d=/[\.\/]/,e="*",f=function(){},g=function(a,b){return a-b},h,i,j={n:{}},k=function(a,b){var c=j,d=i,e=Array.prototype.slice.call(arguments,2),f=k.listeners(a),l=0,m=!1,n,o=[],p={},q=[],r=h,s=[];h=a,i=0;for(var t=0,u=f.length;t<u;t++)"zIndex"in f[t]&&(o.push(f[t].zIndex),f[t].zIndex<0&&(p[f[t].zIndex]=f[t]));o.sort(g);while(o[l]<0){n=p[o[l++]],q.push(n.apply(b,e));if(i){i=d;return q}}for(t=0;t<u;t++){n=f[t];if("zIndex"in n)if(n.zIndex==o[l]){q.push(n.apply(b,e));if(i)break;do{l++,n=p[o[l]],n&&q.push(n.apply(b,e));if(i)break}while(n)}else p[n.zIndex]=n;else{q.push(n.apply(b,e));if(i)break}}i=d,h=r;return q.length?q:null};k.listeners=function(a){var b=a.split(d),c=j,f,g,h,i,k,l,m,n,o=[c],p=[];for(i=0,k=b.length;i<k;i++){n=[];for(l=0,m=o.length;l<m;l++){c=o[l].n,g=[c[b[i]],c[e]],h=2;while(h--)f=g[h],f&&(n.push(f),p=p.concat(f.f||[]))}o=n}return p},k.on=function(a,b){var c=a.split(d),e=j;for(var g=0,h=c.length;g<h;g++)e=e.n,!e[c[g]]&&(e[c[g]]={n:{}}),e=e[c[g]];e.f=e.f||[];for(g=0,h=e.f.length;g<h;g++)if(e.f[g]==b)return f;e.f.push(b);return function(a){+a==+a&&(b.zIndex=+a)}},k.stop=function(){i=1},k.nt=function(a){if(a)return(new RegExp("(?:\\.|\\/|^)"+a+"(?:\\.|\\/|$)")).test(h);return h},k.off=k.unbind=function(a,b){var f=a.split(d),g,h,i,k,l,m,n,o=[j];for(k=0,l=f.length;k<l;k++)for(m=0;m<o.length;m+=i.length-2){i=[m,1],g=o[m].n;if(f[k]!=e)g[f[k]]&&i.push(g[f[k]]);else for(h in g)g[c](h)&&i.push(g[h]);o.splice.apply(o,i)}for(k=0,l=o.length;k<l;k++){g=o[k];while(g.n){if(b){if(g.f){for(m=0,n=g.f.length;m<n;m++)if(g.f[m]==b){g.f.splice(m,1);break}!g.f.length&&delete g.f}for(h in g.n)if(g.n[c](h)&&g.n[h].f){var p=g.n[h].f;for(m=0,n=p.length;m<n;m++)if(p[m]==b){p.splice(m,1);break}!p.length&&delete g.n[h].f}}else{delete g.f;for(h in g.n)g.n[c](h)&&g.n[h].f&&delete g.n[h].f}g=g.n}}},k.once=function(a,b){var c=function(){var d=b.apply(this,arguments);k.unbind(a,c);return d};return k.on(a,c)},k.version=b,k.toString=function(){return"You are running Eve "+b},typeof module!="undefined"&&module.exports?module.exports=k:typeof define!="undefined"?define("eve",[],function(){return k}):a.eve=k})(this),function(){function cF(a){for(var b=0;b<cy.length;b++)cy[b].el.paper==a&&cy.splice(b--,1)}function cE(b,d,e,f,h,i){e=Q(e);var j,k,l,m=[],o,p,q,t=b.ms,u={},v={},w={};if(f)for(y=0,z=cy.length;y<z;y++){var x=cy[y];if(x.el.id==d.id&&x.anim==b){x.percent!=e?(cy.splice(y,1),l=1):k=x,d.attr(x.totalOrigin);break}}else f=+v;for(var y=0,z=b.percents.length;y<z;y++){if(b.percents[y]==e||b.percents[y]>f*b.top){e=b.percents[y],p=b.percents[y-1]||0,t=t/b.top*(e-p),o=b.percents[y+1],j=b.anim[e];break}f&&d.attr(b.anim[b.percents[y]])}if(!!j){if(!k){for(var A in j)if(j[g](A))if(U[g](A)||d.paper.customAttributes[g](A)){u[A]=d.attr(A),u[A]==null&&(u[A]=T[A]),v[A]=j[A];switch(U[A]){case C:w[A]=(v[A]-u[A])/t;break;case"colour":u[A]=a.getRGB(u[A]);var B=a.getRGB(v[A]);w[A]={r:(B.r-u[A].r)/t,g:(B.g-u[A].g)/t,b:(B.b-u[A].b)/t};break;case"path":var D=bR(u[A],v[A]),E=D[1];u[A]=D[0],w[A]=[];for(y=0,z=u[A].length;y<z;y++){w[A][y]=[0];for(var F=1,G=u[A][y].length;F<G;F++)w[A][y][F]=(E[y][F]-u[A][y][F])/t}break;case"transform":var H=d._,I=ca(H[A],v[A]);if(I){u[A]=I.from,v[A]=I.to,w[A]=[],w[A].real=!0;for(y=0,z=u[A].length;y<z;y++){w[A][y]=[u[A][y][0]];for(F=1,G=u[A][y].length;F<G;F++)w[A][y][F]=(v[A][y][F]-u[A][y][F])/t}}else{var J=d.matrix||new cb,K={_:{transform:H.transform},getBBox:function(){return d.getBBox(1)}};u[A]=[J.a,J.b,J.c,J.d,J.e,J.f],b$(K,v[A]),v[A]=K._.transform,w[A]=[(K.matrix.a-J.a)/t,(K.matrix.b-J.b)/t,(K.matrix.c-J.c)/t,(K.matrix.d-J.d)/t,(K.matrix.e-J.e)/t,(K.matrix.f-J.f)/t]}break;case"csv":var L=r(j[A])[s](c),M=r(u[A])[s](c);if(A=="clip-rect"){u[A]=M,w[A]=[],y=M.length;while(y--)w[A][y]=(L[y]-u[A][y])/t}v[A]=L;break;default:L=[][n](j[A]),M=[][n](u[A]),w[A]=[],y=d.paper.customAttributes[A].length;while(y--)w[A][y]=((L[y]||0)-(M[y]||0))/t}}var O=j.easing,P=a.easing_formulas[O];if(!P){P=r(O).match(N);if(P&&P.length==5){var R=P;P=function(a){return cC(a,+R[1],+R[2],+R[3],+R[4],t)}}else P=bf}q=j.start||b.start||+(new Date),x={anim:b,percent:e,timestamp:q,start:q+(b.del||0),status:0,initstatus:f||0,stop:!1,ms:t,easing:P,from:u,diff:w,to:v,el:d,callback:j.callback,prev:p,next:o,repeat:i||b.times,origin:d.attr(),totalOrigin:h},cy.push(x);if(f&&!k&&!l){x.stop=!0,x.start=new Date-t*f;if(cy.length==1)return cA()}l&&(x.start=new Date-x.ms*f),cy.length==1&&cz(cA)}else k.initstatus=f,k.start=new Date-k.ms*f;eve("raphael.anim.start."+d.id,d,b)}}function cD(a,b){var c=[],d={};this.ms=b,this.times=1;if(a){for(var e in a)a[g](e)&&(d[Q(e)]=a[e],c.push(Q(e)));c.sort(bd)}this.anim=d,this.top=c[c.length-1],this.percents=c}function cC(a,b,c,d,e,f){function o(a,b){var c,d,e,f,j,k;for(e=a,k=0;k<8;k++){f=m(e)-a;if(z(f)<b)return e;j=(3*i*e+2*h)*e+g;if(z(j)<1e-6)break;e=e-f/j}c=0,d=1,e=a;if(e<c)return c;if(e>d)return d;while(c<d){f=m(e);if(z(f-a)<b)return e;a>f?c=e:d=e,e=(d-c)/2+c}return e}function n(a,b){var c=o(a,b);return((l*c+k)*c+j)*c}function m(a){return((i*a+h)*a+g)*a}var g=3*b,h=3*(d-b)-g,i=1-g-h,j=3*c,k=3*(e-c)-j,l=1-j-k;return n(a,1/(200*f))}function cq(){return this.x+q+this.y+q+this.width+" × "+this.height}function cp(){return this.x+q+this.y}function cb(a,b,c,d,e,f){a!=null?(this.a=+a,this.b=+b,this.c=+c,this.d=+d,this.e=+e,this.f=+f):(this.a=1,this.b=0,this.c=0,this.d=1,this.e=0,this.f=0)}function bH(b,c,d){b=a._path2curve(b),c=a._path2curve(c);var e,f,g,h,i,j,k,l,m,n,o=d?0:[];for(var p=0,q=b.length;p<q;p++){var r=b[p];if(r[0]=="M")e=i=r[1],f=j=r[2];else{r[0]=="C"?(m=[e,f].concat(r.slice(1)),e=m[6],f=m[7]):(m=[e,f,e,f,i,j,i,j],e=i,f=j);for(var s=0,t=c.length;s<t;s++){var u=c[s];if(u[0]=="M")g=k=u[1],h=l=u[2];else{u[0]=="C"?(n=[g,h].concat(u.slice(1)),g=n[6],h=n[7]):(n=[g,h,g,h,k,l,k,l],g=k,h=l);var v=bG(m,n,d);if(d)o+=v;else{for(var w=0,x=v.length;w<x;w++)v[w].segment1=p,v[w].segment2=s,v[w].bez1=m,v[w].bez2=n;o=o.concat(v)}}}}}return o}function bG(b,c,d){var e=a.bezierBBox(b),f=a.bezierBBox(c);if(!a.isBBoxIntersect(e,f))return d?0:[];var g=bB.apply(0,b),h=bB.apply(0,c),i=~~(g/5),j=~~(h/5),k=[],l=[],m={},n=d?0:[];for(var o=0;o<i+1;o++){var p=a.findDotsAtSegment.apply(a,b.concat(o/i));k.push({x:p.x,y:p.y,t:o/i})}for(o=0;o<j+1;o++)p=a.findDotsAtSegment.apply(a,c.concat(o/j)),l.push({x:p.x,y:p.y,t:o/j});for(o=0;o<i;o++)for(var q=0;q<j;q++){var r=k[o],s=k[o+1],t=l[q],u=l[q+1],v=z(s.x-r.x)<.001?"y":"x",w=z(u.x-t.x)<.001?"y":"x",x=bD(r.x,r.y,s.x,s.y,t.x,t.y,u.x,u.y);if(x){if(m[x.x.toFixed(4)]==x.y.toFixed(4))continue;m[x.x.toFixed(4)]=x.y.toFixed(4);var y=r.t+z((x[v]-r[v])/(s[v]-r[v]))*(s.t-r.t),A=t.t+z((x[w]-t[w])/(u[w]-t[w]))*(u.t-t.t);y>=0&&y<=1&&A>=0&&A<=1&&(d?n++:n.push({x:x.x,y:x.y,t1:y,t2:A}))}}return n}function bF(a,b){return bG(a,b,1)}function bE(a,b){return bG(a,b)}function bD(a,b,c,d,e,f,g,h){if(!(x(a,c)<y(e,g)||y(a,c)>x(e,g)||x(b,d)<y(f,h)||y(b,d)>x(f,h))){var i=(a*d-b*c)*(e-g)-(a-c)*(e*h-f*g),j=(a*d-b*c)*(f-h)-(b-d)*(e*h-f*g),k=(a-c)*(f-h)-(b-d)*(e-g);if(!k)return;var l=i/k,m=j/k,n=+l.toFixed(2),o=+m.toFixed(2);if(n<+y(a,c).toFixed(2)||n>+x(a,c).toFixed(2)||n<+y(e,g).toFixed(2)||n>+x(e,g).toFixed(2)||o<+y(b,d).toFixed(2)||o>+x(b,d).toFixed(2)||o<+y(f,h).toFixed(2)||o>+x(f,h).toFixed(2))return;return{x:l,y:m}}}function bC(a,b,c,d,e,f,g,h,i){if(!(i<0||bB(a,b,c,d,e,f,g,h)<i)){var j=1,k=j/2,l=j-k,m,n=.01;m=bB(a,b,c,d,e,f,g,h,l);while(z(m-i)>n)k/=2,l+=(m<i?1:-1)*k,m=bB(a,b,c,d,e,f,g,h,l);return l}}function bB(a,b,c,d,e,f,g,h,i){i==null&&(i=1),i=i>1?1:i<0?0:i;var j=i/2,k=12,l=[-0.1252,.1252,-0.3678,.3678,-0.5873,.5873,-0.7699,.7699,-0.9041,.9041,-0.9816,.9816],m=[.2491,.2491,.2335,.2335,.2032,.2032,.1601,.1601,.1069,.1069,.0472,.0472],n=0;for(var o=0;o<k;o++){var p=j*l[o]+j,q=bA(p,a,c,e,g),r=bA(p,b,d,f,h),s=q*q+r*r;n+=m[o]*w.sqrt(s)}return j*n}function bA(a,b,c,d,e){var f=-3*b+9*c-9*d+3*e,g=a*f+6*b-12*c+6*d;return a*g-3*b+3*c}function by(a,b){var c=[];for(var d=0,e=a.length;e-2*!b>d;d+=2){var f=[{x:+a[d-2],y:+a[d-1]},{x:+a[d],y:+a[d+1]},{x:+a[d+2],y:+a[d+3]},{x:+a[d+4],y:+a[d+5]}];b?d?e-4==d?f[3]={x:+a[0],y:+a[1]}:e-2==d&&(f[2]={x:+a[0],y:+a[1]},f[3]={x:+a[2],y:+a[3]}):f[0]={x:+a[e-2],y:+a[e-1]}:e-4==d?f[3]=f[2]:d||(f[0]={x:+a[d],y:+a[d+1]}),c.push(["C",(-f[0].x+6*f[1].x+f[2].x)/6,(-f[0].y+6*f[1].y+f[2].y)/6,(f[1].x+6*f[2].x-f[3].x)/6,(f[1].y+6*f[2].y-f[3].y)/6,f[2].x,f[2].y])}return c}function bx(){return this.hex}function bv(a,b,c){function d(){var e=Array.prototype.slice.call(arguments,0),f=e.join("␀"),h=d.cache=d.cache||{},i=d.count=d.count||[];if(h[g](f)){bu(i,f);return c?c(h[f]):h[f]}i.length>=1e3&&delete h[i.shift()],i.push(f),h[f]=a[m](b,e);return c?c(h[f]):h[f]}return d}function bu(a,b){for(var c=0,d=a.length;c<d;c++)if(a[c]===b)return a.push(a.splice(c,1)[0])}function bm(a){if(Object(a)!==a)return a;var b=new a.constructor;for(var c in a)a[g](c)&&(b[c]=bm(a[c]));return b}function a(c){if(a.is(c,"function"))return b?c():eve.on("raphael.DOMload",c);if(a.is(c,E))return a._engine.create[m](a,c.splice(0,3+a.is(c[0],C))).add(c);var d=Array.prototype.slice.call(arguments,0);if(a.is(d[d.length-1],"function")){var e=d.pop();return b?e.call(a._engine.create[m](a,d)):eve.on("raphael.DOMload",function(){e.call(a._engine.create[m](a,d))})}return a._engine.create[m](a,arguments)}a.version="2.1.0",a.eve=eve;var b,c=/[, ]+/,d={circle:1,rect:1,path:1,ellipse:1,text:1,image:1},e=/\{(\d+)\}/g,f="prototype",g="hasOwnProperty",h={doc:document,win:window},i={was:Object.prototype[g].call(h.win,"Raphael"),is:h.win.Raphael},j=function(){this.ca=this.customAttributes={}},k,l="appendChild",m="apply",n="concat",o="createTouch"in h.doc,p="",q=" ",r=String,s="split",t="click dblclick mousedown mousemove mouseout mouseover mouseup touchstart touchmove touchend touchcancel"[s](q),u={mousedown:"touchstart",mousemove:"touchmove",mouseup:"touchend"},v=r.prototype.toLowerCase,w=Math,x=w.max,y=w.min,z=w.abs,A=w.pow,B=w.PI,C="number",D="string",E="array",F="toString",G="fill",H=Object.prototype.toString,I={},J="push",K=a._ISURL=/^url\(['"]?([^\)]+?)['"]?\)$/i,L=/^\s*((#[a-f\d]{6})|(#[a-f\d]{3})|rgba?\(\s*([\d\.]+%?\s*,\s*[\d\.]+%?\s*,\s*[\d\.]+%?(?:\s*,\s*[\d\.]+%?)?)\s*\)|hsba?\(\s*([\d\.]+(?:deg|\xb0|%)?\s*,\s*[\d\.]+%?\s*,\s*[\d\.]+(?:%?\s*,\s*[\d\.]+)?)%?\s*\)|hsla?\(\s*([\d\.]+(?:deg|\xb0|%)?\s*,\s*[\d\.]+%?\s*,\s*[\d\.]+(?:%?\s*,\s*[\d\.]+)?)%?\s*\))\s*$/i,M={NaN:1,Infinity:1,"-Infinity":1},N=/^(?:cubic-)?bezier\(([^,]+),([^,]+),([^,]+),([^\)]+)\)/,O=w.round,P="setAttribute",Q=parseFloat,R=parseInt,S=r.prototype.toUpperCase,T=a._availableAttrs={"arrow-end":"none","arrow-start":"none",blur:0,"clip-rect":"0 0 1e9 1e9",cursor:"default",cx:0,cy:0,fill:"#fff","fill-opacity":1,font:'10px "Arial"',"font-family":'"Arial"',"font-size":"10","font-style":"normal","font-weight":400,gradient:0,height:0,href:"http://raphaeljs.com/","letter-spacing":0,opacity:1,path:"M0,0",r:0,rx:0,ry:0,src:"",stroke:"#000","stroke-dasharray":"","stroke-linecap":"butt","stroke-linejoin":"butt","stroke-miterlimit":0,"stroke-opacity":1,"stroke-width":1,target:"_blank","text-anchor":"middle",title:"Raphael",transform:"",width:0,x:0,y:0},U=a._availableAnimAttrs={blur:C,"clip-rect":"csv",cx:C,cy:C,fill:"colour","fill-opacity":C,"font-size":C,height:C,opacity:C,path:"path",r:C,rx:C,ry:C,stroke:"colour","stroke-opacity":C,"stroke-width":C,transform:"transform",width:C,x:C,y:C},V=/[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]/g,W=/[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*,[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*/,X={hs:1,rg:1},Y=/,?([achlmqrstvxz]),?/gi,Z=/([achlmrqstvz])[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029,]*((-?\d*\.?\d*(?:e[\-+]?\d+)?[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*,?[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*)+)/ig,$=/([rstm])[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029,]*((-?\d*\.?\d*(?:e[\-+]?\d+)?[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*,?[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*)+)/ig,_=/(-?\d*\.?\d*(?:e[\-+]?\d+)?)[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*,?[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*/ig,ba=a._radial_gradient=/^r(?:\(([^,]+?)[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*,[\x09\x0a\x0b\x0c\x0d\x20\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029]*([^\)]+?)\))?/,bb={},bc=function(a,b){return a.key-b.key},bd=function(a,b){return Q(a)-Q(b)},be=function(){},bf=function(a){return a},bg=a._rectPath=function(a,b,c,d,e){if(e)return[["M",a+e,b],["l",c-e*2,0],["a",e,e,0,0,1,e,e],["l",0,d-e*2],["a",e,e,0,0,1,-e,e],["l",e*2-c,0],["a",e,e,0,0,1,-e,-e],["l",0,e*2-d],["a",e,e,0,0,1,e,-e],["z"]];return[["M",a,b],["l",c,0],["l",0,d],["l",-c,0],["z"]]},bh=function(a,b,c,d){d==null&&(d=c);return[["M",a,b],["m",0,-d],["a",c,d,0,1,1,0,2*d],["a",c,d,0,1,1,0,-2*d],["z"]]},bi=a._getPath={path:function(a){return a.attr("path")},circle:function(a){var b=a.attrs;return bh(b.cx,b.cy,b.r)},ellipse:function(a){var b=a.attrs;return bh(b.cx,b.cy,b.rx,b.ry)},rect:function(a){var b=a.attrs;return bg(b.x,b.y,b.width,b.height,b.r)},image:function(a){var b=a.attrs;return bg(b.x,b.y,b.width,b.height)},text:function(a){var b=a._getBBox();return bg(b.x,b.y,b.width,b.height)}},bj=a.mapPath=function(a,b){if(!b)return a;var c,d,e,f,g,h,i;a=bR(a);for(e=0,g=a.length;e<g;e++){i=a[e];for(f=1,h=i.length;f<h;f+=2)c=b.x(i[f],i[f+1]),d=b.y(i[f],i[f+1]),i[f]=c,i[f+1]=d}return a};a._g=h,a.type=h.win.SVGAngle||h.doc.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure","1.1")?"SVG":"VML";if(a.type=="VML"){var bk=h.doc.createElement("div"),bl;bk.innerHTML='<v:shape adj="1"/>',bl=bk.firstChild,bl.style.behavior="url(#default#VML)";if(!bl||typeof bl.adj!="object")return a.type=p;bk=null}a.svg=!(a.vml=a.type=="VML"),a._Paper=j,a.fn=k=j.prototype=a.prototype,a._id=0,a._oid=0,a.is=function(a,b){b=v.call(b);if(b=="finite")return!M[g](+a);if(b=="array")return a instanceof Array;return b=="null"&&a===null||b==typeof a&&a!==null||b=="object"&&a===Object(a)||b=="array"&&Array.isArray&&Array.isArray(a)||H.call(a).slice(8,-1).toLowerCase()==b},a.angle=function(b,c,d,e,f,g){if(f==null){var h=b-d,i=c-e;if(!h&&!i)return 0;return(180+w.atan2(-i,-h)*180/B+360)%360}return a.angle(b,c,f,g)-a.angle(d,e,f,g)},a.rad=function(a){return a%360*B/180},a.deg=function(a){return a*180/B%360},a.snapTo=function(b,c,d){d=a.is(d,"finite")?d:10;if(a.is(b,E)){var e=b.length;while(e--)if(z(b[e]-c)<=d)return b[e]}else{b=+b;var f=c%b;if(f<d)return c-f;if(f>b-d)return c-f+b}return c};var bn=a.createUUID=function(a,b){return function(){return"xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(a,b).toUpperCase()}}(/[xy]/g,function(a){var b=w.random()*16|0,c=a=="x"?b:b&3|8;return c.toString(16)});a.setWindow=function(b){eve("raphael.setWindow",a,h.win,b),h.win=b,h.doc=h.win.document,a._engine.initWin&&a._engine.initWin(h.win)};var bo=function(b){if(a.vml){var c=/^\s+|\s+$/g,d;try{var e=new ActiveXObject("htmlfile");e.write("<body>"),e.close(),d=e.body}catch(f){d=createPopup().document.body}var g=d.createTextRange();bo=bv(function(a){try{d.style.color=r(a).replace(c,p);var b=g.queryCommandValue("ForeColor");b=(b&255)<<16|b&65280|(b&16711680)>>>16;return"#"+("000000"+b.toString(16)).slice(-6)}catch(e){return"none"}})}else{var i=h.doc.createElement("i");i.title="Raphaël Colour Picker",i.style.display="none",h.doc.body.appendChild(i),bo=bv(function(a){i.style.color=a;return h.doc.defaultView.getComputedStyle(i,p).getPropertyValue("color")})}return bo(b)},bp=function(){return"hsb("+[this.h,this.s,this.b]+")"},bq=function(){return"hsl("+[this.h,this.s,this.l]+")"},br=function(){return this.hex},bs=function(b,c,d){c==null&&a.is(b,"object")&&"r"in b&&"g"in b&&"b"in b&&(d=b.b,c=b.g,b=b.r);if(c==null&&a.is(b,D)){var e=a.getRGB(b);b=e.r,c=e.g,d=e.b}if(b>1||c>1||d>1)b/=255,c/=255,d/=255;return[b,c,d]},bt=function(b,c,d,e){b*=255,c*=255,d*=255;var f={r:b,g:c,b:d,hex:a.rgb(b,c,d),toString:br};a.is(e,"finite")&&(f.opacity=e);return f};a.color=function(b){var c;a.is(b,"object")&&"h"in b&&"s"in b&&"b"in b?(c=a.hsb2rgb(b),b.r=c.r,b.g=c.g,b.b=c.b,b.hex=c.hex):a.is(b,"object")&&"h"in b&&"s"in b&&"l"in b?(c=a.hsl2rgb(b),b.r=c.r,b.g=c.g,b.b=c.b,b.hex=c.hex):(a.is(b,"string")&&(b=a.getRGB(b)),a.is(b,"object")&&"r"in b&&"g"in b&&"b"in b?(c=a.rgb2hsl(b),b.h=c.h,b.s=c.s,b.l=c.l,c=a.rgb2hsb(b),b.v=c.b):(b={hex:"none"},b.r=b.g=b.b=b.h=b.s=b.v=b.l=-1)),b.toString=br;return b},a.hsb2rgb=function(a,b,c,d){this.is(a,"object")&&"h"in a&&"s"in a&&"b"in a&&(c=a.b,b=a.s,a=a.h,d=a.o),a*=360;var e,f,g,h,i;a=a%360/60,i=c*b,h=i*(1-z(a%2-1)),e=f=g=c-i,a=~~a,e+=[i,h,0,0,h,i][a],f+=[h,i,i,h,0,0][a],g+=[0,0,h,i,i,h][a];return bt(e,f,g,d)},a.hsl2rgb=function(a,b,c,d){this.is(a,"object")&&"h"in a&&"s"in a&&"l"in a&&(c=a.l,b=a.s,a=a.h);if(a>1||b>1||c>1)a/=360,b/=100,c/=100;a*=360;var e,f,g,h,i;a=a%360/60,i=2*b*(c<.5?c:1-c),h=i*(1-z(a%2-1)),e=f=g=c-i/2,a=~~a,e+=[i,h,0,0,h,i][a],f+=[h,i,i,h,0,0][a],g+=[0,0,h,i,i,h][a];return bt(e,f,g,d)},a.rgb2hsb=function(a,b,c){c=bs(a,b,c),a=c[0],b=c[1],c=c[2];var d,e,f,g;f=x(a,b,c),g=f-y(a,b,c),d=g==0?null:f==a?(b-c)/g:f==b?(c-a)/g+2:(a-b)/g+4,d=(d+360)%6*60/360,e=g==0?0:g/f;return{h:d,s:e,b:f,toString:bp}},a.rgb2hsl=function(a,b,c){c=bs(a,b,c),a=c[0],b=c[1],c=c[2];var d,e,f,g,h,i;g=x(a,b,c),h=y(a,b,c),i=g-h,d=i==0?null:g==a?(b-c)/i:g==b?(c-a)/i+2:(a-b)/i+4,d=(d+360)%6*60/360,f=(g+h)/2,e=i==0?0:f<.5?i/(2*f):i/(2-2*f);return{h:d,s:e,l:f,toString:bq}},a._path2string=function(){return this.join(",").replace(Y,"$1")};var bw=a._preload=function(a,b){var c=h.doc.createElement("img");c.style.cssText="position:absolute;left:-9999em;top:-9999em",c.onload=function(){b.call(this),this.onload=null,h.doc.body.removeChild(this)},c.onerror=function(){h.doc.body.removeChild(this)},h.doc.body.appendChild(c),c.src=a};a.getRGB=bv(function(b){if(!b||!!((b=r(b)).indexOf("-")+1))return{r:-1,g:-1,b:-1,hex:"none",error:1,toString:bx};if(b=="none")return{r:-1,g:-1,b:-1,hex:"none",toString:bx};!X[g](b.toLowerCase().substring(0,2))&&b.charAt()!="#"&&(b=bo(b));var c,d,e,f,h,i,j,k=b.match(L);if(k){k[2]&&(f=R(k[2].substring(5),16),e=R(k[2].substring(3,5),16),d=R(k[2].substring(1,3),16)),k[3]&&(f=R((i=k[3].charAt(3))+i,16),e=R((i=k[3].charAt(2))+i,16),d=R((i=k[3].charAt(1))+i,16)),k[4]&&(j=k[4][s](W),d=Q(j[0]),j[0].slice(-1)=="%"&&(d*=2.55),e=Q(j[1]),j[1].slice(-1)=="%"&&(e*=2.55),f=Q(j[2]),j[2].slice(-1)=="%"&&(f*=2.55),k[1].toLowerCase().slice(0,4)=="rgba"&&(h=Q(j[3])),j[3]&&j[3].slice(-1)=="%"&&(h/=100));if(k[5]){j=k[5][s](W),d=Q(j[0]),j[0].slice(-1)=="%"&&(d*=2.55),e=Q(j[1]),j[1].slice(-1)=="%"&&(e*=2.55),f=Q(j[2]),j[2].slice(-1)=="%"&&(f*=2.55),(j[0].slice(-3)=="deg"||j[0].slice(-1)=="°")&&(d/=360),k[1].toLowerCase().slice(0,4)=="hsba"&&(h=Q(j[3])),j[3]&&j[3].slice(-1)=="%"&&(h/=100);return a.hsb2rgb(d,e,f,h)}if(k[6]){j=k[6][s](W),d=Q(j[0]),j[0].slice(-1)=="%"&&(d*=2.55),e=Q(j[1]),j[1].slice(-1)=="%"&&(e*=2.55),f=Q(j[2]),j[2].slice(-1)=="%"&&(f*=2.55),(j[0].slice(-3)=="deg"||j[0].slice(-1)=="°")&&(d/=360),k[1].toLowerCase().slice(0,4)=="hsla"&&(h=Q(j[3])),j[3]&&j[3].slice(-1)=="%"&&(h/=100);return a.hsl2rgb(d,e,f,h)}k={r:d,g:e,b:f,toString:bx},k.hex="#"+(16777216|f|e<<8|d<<16).toString(16).slice(1),a.is(h,"finite")&&(k.opacity=h);return k}return{r:-1,g:-1,b:-1,hex:"none",error:1,toString:bx}},a),a.hsb=bv(function(b,c,d){return a.hsb2rgb(b,c,d).hex}),a.hsl=bv(function(b,c,d){return a.hsl2rgb(b,c,d).hex}),a.rgb=bv(function(a,b,c){return"#"+(16777216|c|b<<8|a<<16).toString(16).slice(1)}),a.getColor=function(a){var b=this.getColor.start=this.getColor.start||{h:0,s:1,b:a||.75},c=this.hsb2rgb(b.h,b.s,b.b);b.h+=.075,b.h>1&&(b.h=0,b.s-=.2,b.s<=0&&(this.getColor.start={h:0,s:1,b:b.b}));return c.hex},a.getColor.reset=function(){delete this.start},a.parsePathString=function(b){if(!b)return null;var c=bz(b);if(c.arr)return bJ(c.arr);var d={a:7,c:6,h:1,l:2,m:2,r:4,q:4,s:4,t:2,v:1,z:0},e=[];a.is(b,E)&&a.is(b[0],E)&&(e=bJ(b)),e.length||r(b).replace(Z,function(a,b,c){var f=[],g=b.toLowerCase();c.replace(_,function(a,b){b&&f.push(+b)}),g=="m"&&f.length>2&&(e.push([b][n](f.splice(0,2))),g="l",b=b=="m"?"l":"L");if(g=="r")e.push([b][n](f));else while(f.length>=d[g]){e.push([b][n](f.splice(0,d[g])));if(!d[g])break}}),e.toString=a._path2string,c.arr=bJ(e);return e},a.parseTransformString=bv(function(b){if(!b)return null;var c={r:3,s:4,t:2,m:6},d=[];a.is(b,E)&&a.is(b[0],E)&&(d=bJ(b)),d.length||r(b).replace($,function(a,b,c){var e=[],f=v.call(b);c.replace(_,function(a,b){b&&e.push(+b)}),d.push([b][n](e))}),d.toString=a._path2string;return d});var bz=function(a){var b=bz.ps=bz.ps||{};b[a]?b[a].sleep=100:b[a]={sleep:100},setTimeout(function(){for(var c in b)b[g](c)&&c!=a&&(b[c].sleep--,!b[c].sleep&&delete b[c])});return b[a]};a.findDotsAtSegment=function(a,b,c,d,e,f,g,h,i){var j=1-i,k=A(j,3),l=A(j,2),m=i*i,n=m*i,o=k*a+l*3*i*c+j*3*i*i*e+n*g,p=k*b+l*3*i*d+j*3*i*i*f+n*h,q=a+2*i*(c-a)+m*(e-2*c+a),r=b+2*i*(d-b)+m*(f-2*d+b),s=c+2*i*(e-c)+m*(g-2*e+c),t=d+2*i*(f-d)+m*(h-2*f+d),u=j*a+i*c,v=j*b+i*d,x=j*e+i*g,y=j*f+i*h,z=90-w.atan2(q-s,r-t)*180/B;(q>s||r<t)&&(z+=180);return{x:o,y:p,m:{x:q,y:r},n:{x:s,y:t},start:{x:u,y:v},end:{x:x,y:y},alpha:z}},a.bezierBBox=function(b,c,d,e,f,g,h,i){a.is(b,"array")||(b=[b,c,d,e,f,g,h,i]);var j=bQ.apply(null,b);return{x:j.min.x,y:j.min.y,x2:j.max.x,y2:j.max.y,width:j.max.x-j.min.x,height:j.max.y-j.min.y}},a.isPointInsideBBox=function(a,b,c){return b>=a.x&&b<=a.x2&&c>=a.y&&c<=a.y2},a.isBBoxIntersect=function(b,c){var d=a.isPointInsideBBox;return d(c,b.x,b.y)||d(c,b.x2,b.y)||d(c,b.x,b.y2)||d(c,b.x2,b.y2)||d(b,c.x,c.y)||d(b,c.x2,c.y)||d(b,c.x,c.y2)||d(b,c.x2,c.y2)||(b.x<c.x2&&b.x>c.x||c.x<b.x2&&c.x>b.x)&&(b.y<c.y2&&b.y>c.y||c.y<b.y2&&c.y>b.y)},a.pathIntersection=function(a,b){return bH(a,b)},a.pathIntersectionNumber=function(a,b){return bH(a,b,1)},a.isPointInsidePath=function(b,c,d){var e=a.pathBBox(b);return a.isPointInsideBBox(e,c,d)&&bH(b,[["M",c,d],["H",e.x2+10]],1)%2==1},a._removedFactory=function(a){return function(){eve("raphael.log",null,"Raphaël: you are calling to method “"+a+"” of removed object",a)}};var bI=a.pathBBox=function(a){var b=bz(a);if(b.bbox)return b.bbox;if(!a)return{x:0,y:0,width:0,height:0,x2:0,y2:0};a=bR(a);var c=0,d=0,e=[],f=[],g;for(var h=0,i=a.length;h<i;h++){g=a[h];if(g[0]=="M")c=g[1],d=g[2],e.push(c),f.push(d);else{var j=bQ(c,d,g[1],g[2],g[3],g[4],g[5],g[6]);e=e[n](j.min.x,j.max.x),f=f[n](j.min.y,j.max.y),c=g[5],d=g[6]}}var k=y[m](0,e),l=y[m](0,f),o=x[m](0,e),p=x[m](0,f),q={x:k,y:l,x2:o,y2:p,width:o-k,height:p-l};b.bbox=bm(q);return q},bJ=function(b){var c=bm(b);c.toString=a._path2string;return c},bK=a._pathToRelative=function(b){var c=bz(b);if(c.rel)return bJ(c.rel);if(!a.is(b,E)||!a.is(b&&b[0],E))b=a.parsePathString(b);var d=[],e=0,f=0,g=0,h=0,i=0;b[0][0]=="M"&&(e=b[0][1],f=b[0][2],g=e,h=f,i++,d.push(["M",e,f]));for(var j=i,k=b.length;j<k;j++){var l=d[j]=[],m=b[j];if(m[0]!=v.call(m[0])){l[0]=v.call(m[0]);switch(l[0]){case"a":l[1]=m[1],l[2]=m[2],l[3]=m[3],l[4]=m[4],l[5]=m[5],l[6]=+(m[6]-e).toFixed(3),l[7]=+(m[7]-f).toFixed(3);break;case"v":l[1]=+(m[1]-f).toFixed(3);break;case"m":g=m[1],h=m[2];default:for(var n=1,o=m.length;n<o;n++)l[n]=+(m[n]-(n%2?e:f)).toFixed(3)}}else{l=d[j]=[],m[0]=="m"&&(g=m[1]+e,h=m[2]+f);for(var p=0,q=m.length;p<q;p++)d[j][p]=m[p]}var r=d[j].length;switch(d[j][0]){case"z":e=g,f=h;break;case"h":e+=+d[j][r-1];break;case"v":f+=+d[j][r-1];break;default:e+=+d[j][r-2],f+=+d[j][r-1]}}d.toString=a._path2string,c.rel=bJ(d);return d},bL=a._pathToAbsolute=function(b){var c=bz(b);if(c.abs)return bJ(c.abs);if(!a.is(b,E)||!a.is(b&&b[0],E))b=a.parsePathString(b);if(!b||!b.length)return[["M",0,0]];var d=[],e=0,f=0,g=0,h=0,i=0;b[0][0]=="M"&&(e=+b[0][1],f=+b[0][2],g=e,h=f,i++,d[0]=["M",e,f]);var j=b.length==3&&b[0][0]=="M"&&b[1][0].toUpperCase()=="R"&&b[2][0].toUpperCase()=="Z";for(var k,l,m=i,o=b.length;m<o;m++){d.push(k=[]),l=b[m];if(l[0]!=S.call(l[0])){k[0]=S.call(l[0]);switch(k[0]){case"A":k[1]=l[1],k[2]=l[2],k[3]=l[3],k[4]=l[4],k[5]=l[5],k[6]=+(l[6]+e),k[7]=+(l[7]+f);break;case"V":k[1]=+l[1]+f;break;case"H":k[1]=+l[1]+e;break;case"R":var p=[e,f][n](l.slice(1));for(var q=2,r=p.length;q<r;q++)p[q]=+p[q]+e,p[++q]=+p[q]+f;d.pop(),d=d[n](by(p,j));break;case"M":g=+l[1]+e,h=+l[2]+f;default:for(q=1,r=l.length;q<r;q++)k[q]=+l[q]+(q%2?e:f)}}else if(l[0]=="R")p=[e,f][n](l.slice(1)),d.pop(),d=d[n](by(p,j)),k=["R"][n](l.slice(-2));else for(var s=0,t=l.length;s<t;s++)k[s]=l[s];switch(k[0]){case"Z":e=g,f=h;break;case"H":e=k[1];break;case"V":f=k[1];break;case"M":g=k[k.length-2],h=k[k.length-1];default:e=k[k.length-2],f=k[k.length-1]}}d.toString=a._path2string,c.abs=bJ(d);return d},bM=function(a,b,c,d){return[a,b,c,d,c,d]},bN=function(a,b,c,d,e,f){var g=1/3,h=2/3;return[g*a+h*c,g*b+h*d,g*e+h*c,g*f+h*d,e,f]},bO=function(a,b,c,d,e,f,g,h,i,j){var k=B*120/180,l=B/180*(+e||0),m=[],o,p=bv(function(a,b,c){var d=a*w.cos(c)-b*w.sin(c),e=a*w.sin(c)+b*w.cos(c);return{x:d,y:e}});if(!j){o=p(a,b,-l),a=o.x,b=o.y,o=p(h,i,-l),h=o.x,i=o.y;var q=w.cos(B/180*e),r=w.sin(B/180*e),t=(a-h)/2,u=(b-i)/2,v=t*t/(c*c)+u*u/(d*d);v>1&&(v=w.sqrt(v),c=v*c,d=v*d);var x=c*c,y=d*d,A=(f==g?-1:1)*w.sqrt(z((x*y-x*u*u-y*t*t)/(x*u*u+y*t*t))),C=A*c*u/d+(a+h)/2,D=A*-d*t/c+(b+i)/2,E=w.asin(((b-D)/d).toFixed(9)),F=w.asin(((i-D)/d).toFixed(9));E=a<C?B-E:E,F=h<C?B-F:F,E<0&&(E=B*2+E),F<0&&(F=B*2+F),g&&E>F&&(E=E-B*2),!g&&F>E&&(F=F-B*2)}else E=j[0],F=j[1],C=j[2],D=j[3];var G=F-E;if(z(G)>k){var H=F,I=h,J=i;F=E+k*(g&&F>E?1:-1),h=C+c*w.cos(F),i=D+d*w.sin(F),m=bO(h,i,c,d,e,0,g,I,J,[F,H,C,D])}G=F-E;var K=w.cos(E),L=w.sin(E),M=w.cos(F),N=w.sin(F),O=w.tan(G/4),P=4/3*c*O,Q=4/3*d*O,R=[a,b],S=[a+P*L,b-Q*K],T=[h+P*N,i-Q*M],U=[h,i];S[0]=2*R[0]-S[0],S[1]=2*R[1]-S[1];if(j)return[S,T,U][n](m);m=[S,T,U][n](m).join()[s](",");var V=[];for(var W=0,X=m.length;W<X;W++)V[W]=W%2?p(m[W-1],m[W],l).y:p(m[W],m[W+1],l).x;return V},bP=function(a,b,c,d,e,f,g,h,i){var j=1-i;return{x:A(j,3)*a+A(j,2)*3*i*c+j*3*i*i*e+A(i,3)*g,y:A(j,3)*b+A(j,2)*3*i*d+j*3*i*i*f+A(i,3)*h}},bQ=bv(function(a,b,c,d,e,f,g,h){var i=e-2*c+a-(g-2*e+c),j=2*(c-a)-2*(e-c),k=a-c,l=(-j+w.sqrt(j*j-4*i*k))/2/i,n=(-j-w.sqrt(j*j-4*i*k))/2/i,o=[b,h],p=[a,g],q;z(l)>"1e12"&&(l=.5),z(n)>"1e12"&&(n=.5),l>0&&l<1&&(q=bP(a,b,c,d,e,f,g,h,l),p.push(q.x),o.push(q.y)),n>0&&n<1&&(q=bP(a,b,c,d,e,f,g,h,n),p.push(q.x),o.push(q.y)),i=f-2*d+b-(h-2*f+d),j=2*(d-b)-2*(f-d),k=b-d,l=(-j+w.sqrt(j*j-4*i*k))/2/i,n=(-j-w.sqrt(j*j-4*i*k))/2/i,z(l)>"1e12"&&(l=.5),z(n)>"1e12"&&(n=.5),l>0&&l<1&&(q=bP(a,b,c,d,e,f,g,h,l),p.push(q.x),o.push(q.y)),n>0&&n<1&&(q=bP(a,b,c,d,e,f,g,h,n),p.push(q.x),o.push(q.y));return{min:{x:y[m](0,p),y:y[m](0,o)},max:{x:x[m](0,p),y:x[m](0,o)}}}),bR=a._path2curve=bv(function(a,b){var c=!b&&bz(a);if(!b&&c.curve)return bJ(c.curve);var d=bL(a),e=b&&bL(b),f={x:0,y:0,bx:0,by:0,X:0,Y:0,qx:null,qy:null},g={x:0,y:0,bx:0,by:0,X:0,Y:0,qx:null,qy:null},h=function(a,b){var c,d;if(!a)return["C",b.x,b.y,b.x,b.y,b.x,b.y];!(a[0]in{T:1,Q:1})&&(b.qx=b.qy=null);switch(a[0]){case"M":b.X=a[1],b.Y=a[2];break;case"A":a=["C"][n](bO[m](0,[b.x,b.y][n](a.slice(1))));break;case"S":c=b.x+(b.x-(b.bx||b.x)),d=b.y+(b.y-(b.by||b.y)),a=["C",c,d][n](a.slice(1));break;case"T":b.qx=b.x+(b.x-(b.qx||b.x)),b.qy=b.y+(b.y-(b.qy||b.y)),a=["C"][n](bN(b.x,b.y,b.qx,b.qy,a[1],a[2]));break;case"Q":b.qx=a[1],b.qy=a[2],a=["C"][n](bN(b.x,b.y,a[1],a[2],a[3],a[4]));break;case"L":a=["C"][n](bM(b.x,b.y,a[1],a[2]));break;case"H":a=["C"][n](bM(b.x,b.y,a[1],b.y));break;case"V":a=["C"][n](bM(b.x,b.y,b.x,a[1]));break;case"Z":a=["C"][n](bM(b.x,b.y,b.X,b.Y))}return a},i=function(a,b){if(a[b].length>7){a[b].shift();var c=a[b];while(c.length)a.splice(b++,0,["C"][n](c.splice(0,6)));a.splice(b,1),l=x(d.length,e&&e.length||0)}},j=function(a,b,c,f,g){a&&b&&a[g][0]=="M"&&b[g][0]!="M"&&(b.splice(g,0,["M",f.x,f.y]),c.bx=0,c.by=0,c.x=a[g][1],c.y=a[g][2],l=x(d.length,e&&e.length||0))};for(var k=0,l=x(d.length,e&&e.length||0);k<l;k++){d[k]=h(d[k],f),i(d,k),e&&(e[k]=h(e[k],g)),e&&i(e,k),j(d,e,f,g,k),j(e,d,g,f,k);var o=d[k],p=e&&e[k],q=o.length,r=e&&p.length;f.x=o[q-2],f.y=o[q-1],f.bx=Q(o[q-4])||f.x,f.by=Q(o[q-3])||f.y,g.bx=e&&(Q(p[r-4])||g.x),g.by=e&&(Q(p[r-3])||g.y),g.x=e&&p[r-2],g.y=e&&p[r-1]}e||(c.curve=bJ(d));return e?[d,e]:d},null,bJ),bS=a._parseDots=bv(function(b){var c=[];for(var d=0,e=b.length;d<e;d++){var f={},g=b[d].match(/^([^:]*):?([\d\.]*)/);f.color=a.getRGB(g[1]);if(f.color.error)return null;f.color=f.color.hex,g[2]&&(f.offset=g[2]+"%"),c.push(f)}for(d=1,e=c.length-1;d<e;d++)if(!c[d].offset){var h=Q(c[d-1].offset||0),i=0;for(var j=d+1;j<e;j++)if(c[j].offset){i=c[j].offset;break}i||(i=100,j=e),i=Q(i);var k=(i-h)/(j-d+1);for(;d<j;d++)h+=k,c[d].offset=h+"%"}return c}),bT=a._tear=function(a,b){a==b.top&&(b.top=a.prev),a==b.bottom&&(b.bottom=a.next),a.next&&(a.next.prev=a.prev),a.prev&&(a.prev.next=a.next)},bU=a._tofront=function(a,b){b.top!==a&&(bT(a,b),a.next=null,a.prev=b.top,b.top.next=a,b.top=a)},bV=a._toback=function(a,b){b.bottom!==a&&(bT(a,b),a.next=b.bottom,a.prev=null,b.bottom.prev=a,b.bottom=a)},bW=a._insertafter=function(a,b,c){bT(a,c),b==c.top&&(c.top=a),b.next&&(b.next.prev=a),a.next=b.next,a.prev=b,b.next=a},bX=a._insertbefore=function(a,b,c){bT(a,c),b==c.bottom&&(c.bottom=a),b.prev&&(b.prev.next=a),a.prev=b.prev,b.prev=a,a.next=b},bY=a.toMatrix=function(a,b){var c=bI(a),d={_:{transform:p},getBBox:function(){return c}};b$(d,b);return d.matrix},bZ=a.transformPath=function(a,b){return bj(a,bY(a,b))},b$=a._extractTransform=function(b,c){if(c==null)return b._.transform;c=r(c).replace(/\.{3}|\u2026/g,b._.transform||p);var d=a.parseTransformString(c),e=0,f=0,g=0,h=1,i=1,j=b._,k=new cb;j.transform=d||[];if(d)for(var l=0,m=d.length;l<m;l++){var n=d[l],o=n.length,q=r(n[0]).toLowerCase(),s=n[0]!=q,t=s?k.invert():0,u,v,w,x,y;q=="t"&&o==3?s?(u=t.x(0,0),v=t.y(0,0),w=t.x(n[1],n[2]),x=t.y(n[1],n[2]),k.translate(w-u,x-v)):k.translate(n[1],n[2]):q=="r"?o==2?(y=y||b.getBBox(1),k.rotate(n[1],y.x+y.width/2,y.y+y.height/2),e+=n[1]):o==4&&(s?(w=t.x(n[2],n[3]),x=t.y(n[2],n[3]),k.rotate(n[1],w,x)):k.rotate(n[1],n[2],n[3]),e+=n[1]):q=="s"?o==2||o==3?(y=y||b.getBBox(1),k.scale(n[1],n[o-1],y.x+y.width/2,y.y+y.height/2),h*=n[1],i*=n[o-1]):o==5&&(s?(w=t.x(n[3],n[4]),x=t.y(n[3],n[4]),k.scale(n[1],n[2],w,x)):k.scale(n[1],n[2],n[3],n[4]),h*=n[1],i*=n[2]):q=="m"&&o==7&&k.add(n[1],n[2],n[3],n[4],n[5],n[6]),j.dirtyT=1,b.matrix=k}b.matrix=k,j.sx=h,j.sy=i,j.deg=e,j.dx=f=k.e,j.dy=g=k.f,h==1&&i==1&&!e&&j.bbox?(j.bbox.x+=+f,j.bbox.y+=+g):j.dirtyT=1},b_=function(a){var b=a[0];switch(b.toLowerCase()){case"t":return[b,0,0];case"m":return[b,1,0,0,1,0,0];case"r":return a.length==4?[b,0,a[2],a[3]]:[b,0];case"s":return a.length==5?[b,1,1,a[3],a[4]]:a.length==3?[b,1,1]:[b,1]}},ca=a._equaliseTransform=function(b,c){c=r(c).replace(/\.{3}|\u2026/g,b),b=a.parseTransformString(b)||[],c=a.parseTransformString(c)||[];var d=x(b.length,c.length),e=[],f=[],g=0,h,i,j,k;for(;g<d;g++){j=b[g]||b_(c[g]),k=c[g]||b_(j);if(j[0]!=k[0]||j[0].toLowerCase()=="r"&&(j[2]!=k[2]||j[3]!=k[3])||j[0].toLowerCase()=="s"&&(j[3]!=k[3]||j[4]!=k[4]))return;e[g]=[],f[g]=[];for(h=0,i=x(j.length,k.length);h<i;h++)h in j&&(e[g][h]=j[h]),h in k&&(f[g][h]=k[h])}return{from:e,to:f}};a._getContainer=function(b,c,d,e){var f;f=e==null&&!a.is(b,"object")?h.doc.getElementById(b):b;if(f!=null){if(f.tagName)return c==null?{container:f,width:f.style.pixelWidth||f.offsetWidth,height:f.style.pixelHeight||f.offsetHeight}:{container:f,width:c,height:d};return{container:1,x:b,y:c,width:d,height:e}}},a.pathToRelative=bK,a._engine={},a.path2curve=bR,a.matrix=function(a,b,c,d,e,f){return new cb(a,b,c,d,e,f)},function(b){function d(a){var b=w.sqrt(c(a));a[0]&&(a[0]/=b),a[1]&&(a[1]/=b)}function c(a){return a[0]*a[0]+a[1]*a[1]}b.add=function(a,b,c,d,e,f){var g=[[],[],[]],h=[[this.a,this.c,this.e],[this.b,this.d,this.f],[0,0,1]],i=[[a,c,e],[b,d,f],[0,0,1]],j,k,l,m;a&&a instanceof cb&&(i=[[a.a,a.c,a.e],[a.b,a.d,a.f],[0,0,1]]);for(j=0;j<3;j++)for(k=0;k<3;k++){m=0;for(l=0;l<3;l++)m+=h[j][l]*i[l][k];g[j][k]=m}this.a=g[0][0],this.b=g[1][0],this.c=g[0][1],this.d=g[1][1],this.e=g[0][2],this.f=g[1][2]},b.invert=function(){var a=this,b=a.a*a.d-a.b*a.c;return new cb(a.d/b,-a.b/b,-a.c/b,a.a/b,(a.c*a.f-a.d*a.e)/b,(a.b*a.e-a.a*a.f)/b)},b.clone=function(){return new cb(this.a,this.b,this.c,this.d,this.e,this.f)},b.translate=function(a,b){this.add(1,0,0,1,a,b)},b.scale=function(a,b,c,d){b==null&&(b=a),(c||d)&&this.add(1,0,0,1,c,d),this.add(a,0,0,b,0,0),(c||d)&&this.add(1,0,0,1,-c,-d)},b.rotate=function(b,c,d){b=a.rad(b),c=c||0,d=d||0;var e=+w.cos(b).toFixed(9),f=+w.sin(b).toFixed(9);this.add(e,f,-f,e,c,d),this.add(1,0,0,1,-c,-d)},b.x=function(a,b){return a*this.a+b*this.c+this.e},b.y=function(a,b){return a*this.b+b*this.d+this.f},b.get=function(a){return+this[r.fromCharCode(97+a)].toFixed(4)},b.toString=function(){return a.svg?"matrix("+[this.get(0),this.get(1),this.get(2),this.get(3),this.get(4),this.get(5)].join()+")":[this.get(0),this.get(2),this.get(1),this.get(3),0,0].join()},b.toFilter=function(){return"progid:DXImageTransform.Microsoft.Matrix(M11="+this.get(0)+", M12="+this.get(2)+", M21="+this.get(1)+", M22="+this.get(3)+", Dx="+this.get(4)+", Dy="+this.get(5)+", sizingmethod='auto expand')"},b.offset=function(){return[this.e.toFixed(4),this.f.toFixed(4)]},b.split=function(){var b={};b.dx=this.e,b.dy=this.f;var e=[[this.a,this.c],[this.b,this.d]];b.scalex=w.sqrt(c(e[0])),d(e[0]),b.shear=e[0][0]*e[1][0]+e[0][1]*e[1][1],e[1]=[e[1][0]-e[0][0]*b.shear,e[1][1]-e[0][1]*b.shear],b.scaley=w.sqrt(c(e[1])),d(e[1]),b.shear/=b.scaley;var f=-e[0][1],g=e[1][1];g<0?(b.rotate=a.deg(w.acos(g)),f<0&&(b.rotate=360-b.rotate)):b.rotate=a.deg(w.asin(f)),b.isSimple=!+b.shear.toFixed(9)&&(b.scalex.toFixed(9)==b.scaley.toFixed(9)||!b.rotate),b.isSuperSimple=!+b.shear.toFixed(9)&&b.scalex.toFixed(9)==b.scaley.toFixed(9)&&!b.rotate,b.noRotation=!+b.shear.toFixed(9)&&!b.rotate;return b},b.toTransformString=function(a){var b=a||this[s]();if(b.isSimple){b.scalex=+b.scalex.toFixed(4),b.scaley=+b.scaley.toFixed(4),b.rotate=+b.rotate.toFixed(4);return(b.dx||b.dy?"t"+[b.dx,b.dy]:p)+(b.scalex!=1||b.scaley!=1?"s"+[b.scalex,b.scaley,0,0]:p)+(b.rotate?"r"+[b.rotate,0,0]:p)}return"m"+[this.get(0),this.get(1),this.get(2),this.get(3),this.get(4),this.get(5)]}}(cb.prototype);var cc=navigator.userAgent.match(/Version\/(.*?)\s/)||navigator.userAgent.match(/Chrome\/(\d+)/);navigator.vendor=="Apple Computer, Inc."&&(cc&&cc[1]<4||navigator.platform.slice(0,2)=="iP")||navigator.vendor=="Google Inc."&&cc&&cc[1]<8?k.safari=function(){var a=this.rect(-99,-99,this.width+99,this.height+99).attr({stroke:"none"});setTimeout(function(){a.remove()})}:k.safari=be;var cd=function(){this.returnValue=!1},ce=function(){return this.originalEvent.preventDefault()},cf=function(){this.cancelBubble=!0},cg=function(){return this.originalEvent.stopPropagation()},ch=function(){if(h.doc.addEventListener)return function(a,b,c,d){var e=o&&u[b]?u[b]:b,f=function(e){var f=h.doc.documentElement.scrollTop||h.doc.body.scrollTop,i=h.doc.documentElement.scrollLeft||h.doc.body.scrollLeft,j=e.clientX+i,k=e.clientY+f;if(o&&u[g](b))for(var l=0,m=e.targetTouches&&e.targetTouches.length;l<m;l++)if(e.targetTouches[l].target==a){var n=e;e=e.targetTouches[l],e.originalEvent=n,e.preventDefault=ce,e.stopPropagation=cg;break}return c.call(d,e,j,k)};a.addEventListener(e,f,!1);return function(){a.removeEventListener(e,f,!1);return!0}};if(h.doc.attachEvent)return function(a,b,c,d){var e=function(a){a=a||h.win.event;var b=h.doc.documentElement.scrollTop||h.doc.body.scrollTop,e=h.doc.documentElement.scrollLeft||h.doc.body.scrollLeft,f=a.clientX+e,g=a.clientY+b;a.preventDefault=a.preventDefault||cd,a.stopPropagation=a.stopPropagation||cf;return c.call(d,a,f,g)};a.attachEvent("on"+b,e);var f=function(){a.detachEvent("on"+b,e);return!0};return f}}(),ci=[],cj=function(a){var b=a.clientX,c=a.clientY,d=h.doc.documentElement.scrollTop||h.doc.body.scrollTop,e=h.doc.documentElement.scrollLeft||h.doc.body.scrollLeft,f,g=ci.length;while(g--){f=ci[g];if(o){var i=a.touches.length,j;while(i--){j=a.touches[i];if(j.identifier==f.el._drag.id){b=j.clientX,c=j.clientY,(a.originalEvent?a.originalEvent:a).preventDefault();break}}}else a.preventDefault();var k=f.el.node,l,m=k.nextSibling,n=k.parentNode,p=k.style.display;h.win.opera&&n.removeChild(k),k.style.display="none",l=f.el.paper.getElementByPoint(b,c),k.style.display=p,h.win.opera&&(m?n.insertBefore(k,m):n.appendChild(k)),l&&eve("raphael.drag.over."+f.el.id,f.el,l),b+=e,c+=d,eve("raphael.drag.move."+f.el.id,f.move_scope||f.el,b-f.el._drag.x,c-f.el._drag.y,b,c,a)}},ck=function(b){a.unmousemove(cj).unmouseup(ck);var c=ci.length,d;while(c--)d=ci[c],d.el._drag={},eve("raphael.drag.end."+d.el.id,d.end_scope||d.start_scope||d.move_scope||d.el,b);ci=[]},cl=a.el={};for(var cm=t.length;cm--;)(function(b){a[b]=cl[b]=function(c,d){a.is(c,"function")&&(this.events=this.events||[],this.events.push({name:b,f:c,unbind:ch(this.shape||this.node||h.doc,b,c,d||this)}));return this},a["un"+b]=cl["un"+b]=function(a){var c=this.events||[],d=c.length;while(d--)if(c[d].name==b&&c[d].f==a){c[d].unbind(),c.splice(d,1),!c.length&&delete this.events;return this}return this}})(t[cm]);cl.data=function(b,c){var d=bb[this.id]=bb[this.id]||{};if(arguments.length==1){if(a.is(b,"object")){for(var e in b)b[g](e)&&this.data(e,b[e]);return this}eve("raphael.data.get."+this.id,this,d[b],b);return d[b]}d[b]=c,eve("raphael.data.set."+this.id,this,c,b);return this},cl.removeData=function(a){a==null?bb[this.id]={}:bb[this.id]&&delete bb[this.id][a];return this},cl.hover=function(a,b,c,d){return this.mouseover(a,c).mouseout(b,d||c)},cl.unhover=function(a,b){return this.unmouseover(a).unmouseout(b)};var cn=[];cl.drag=function(b,c,d,e,f,g){function i(i){(i.originalEvent||i).preventDefault();var j=h.doc.documentElement.scrollTop||h.doc.body.scrollTop,k=h.doc.documentElement.scrollLeft||h.doc.body.scrollLeft;this._drag.x=i.clientX+k,this._drag.y=i.clientY+j,this._drag.id=i.identifier,!ci.length&&a.mousemove(cj).mouseup(ck),ci.push({el:this,move_scope:e,start_scope:f,end_scope:g}),c&&eve.on("raphael.drag.start."+this.id,c),b&&eve.on("raphael.drag.move."+this.id,b),d&&eve.on("raphael.drag.end."+this.id,d),eve("raphael.drag.start."+this.id,f||e||this,i.clientX+k,i.clientY+j,i)}this._drag={},cn.push({el:this,start:i}),this.mousedown(i);return this},cl.onDragOver=function(a){a?eve.on("raphael.drag.over."+this.id,a):eve.unbind("raphael.drag.over."+this.id)},cl.undrag=function(){var b=cn.length;while(b--)cn[b].el==this&&(this.unmousedown(cn[b].start),cn.splice(b,1),eve.unbind("raphael.drag.*."+this.id));!cn.length&&a.unmousemove(cj).unmouseup(ck)},k.circle=function(b,c,d){var e=a._engine.circle(this,b||0,c||0,d||0);this.__set__&&this.__set__.push(e);return e},k.rect=function(b,c,d,e,f){var g=a._engine.rect(this,b||0,c||0,d||0,e||0,f||0);this.__set__&&this.__set__.push(g);return g},k.ellipse=function(b,c,d,e){var f=a._engine.ellipse(this,b||0,c||0,d||0,e||0);this.__set__&&this.__set__.push(f);return f},k.path=function(b){b&&!a.is(b,D)&&!a.is(b[0],E)&&(b+=p);var c=a._engine.path(a.format[m](a,arguments),this);this.__set__&&this.__set__.push(c);return c},k.image=function(b,c,d,e,f){var g=a._engine.image(this,b||"about:blank",c||0,d||0,e||0,f||0);this.__set__&&this.__set__.push(g);return g},k.text=function(b,c,d){var e=a._engine.text(this,b||0,c||0,r(d));this.__set__&&this.__set__.push(e);return e},k.set=function(b){!a.is(b,"array")&&(b=Array.prototype.splice.call(arguments,0,arguments.length));var c=new cG(b);this.__set__&&this.__set__.push(c);return c},k.setStart=function(a){this.__set__=a||this.set()},k.setFinish=function(a){var b=this.__set__;delete this.__set__;return b},k.setSize=function(b,c){return a._engine.setSize.call(this,b,c)},k.setViewBox=function(b,c,d,e,f){return a._engine.setViewBox.call(this,b,c,d,e,f)},k.top=k.bottom=null,k.raphael=a;var co=function(a){var b=a.getBoundingClientRect(),c=a.ownerDocument,d=c.body,e=c.documentElement,f=e.clientTop||d.clientTop||0,g=e.clientLeft||d.clientLeft||0,i=b.top+(h.win.pageYOffset||e.scrollTop||d.scrollTop)-f,j=b.left+(h.win.pageXOffset||e.scrollLeft||d.scrollLeft)-g;return{y:i,x:j}};k.getElementByPoint=function(a,b){var c=this,d=c.canvas,e=h.doc.elementFromPoint(a,b);if(h.win.opera&&e.tagName=="svg"){var f=co(d),g=d.createSVGRect();g.x=a-f.x,g.y=b-f.y,g.width=g.height=1;var i=d.getIntersectionList(g,null);i.length&&(e=i[i.length-1])}if(!e)return null;while(e.parentNode&&e!=d.parentNode&&!e.raphael)e=e.parentNode;e==c.canvas.parentNode&&(e=d),e=e&&e.raphael?c.getById(e.raphaelid):null;return e},k.getById=function(a){var b=this.bottom;while(b){if(b.id==a)return b;b=b.next}return null},k.forEach=function(a,b){var c=this.bottom;while(c){if(a.call(b,c)===!1)return this;c=c.next}return this},k.getElementsByPoint=function(a,b){var c=this.set();this.forEach(function(d){d.isPointInside(a,b)&&c.push(d)});return c},cl.isPointInside=function(b,c){var d=this.realPath=this.realPath||bi[this.type](this);return a.isPointInsidePath(d,b,c)},cl.getBBox=function(a){if(this.removed)return{};var b=this._;if(a){if(b.dirty||!b.bboxwt)this.realPath=bi[this.type](this),b.bboxwt=bI(this.realPath),b.bboxwt.toString=cq,b.dirty=0;return b.bboxwt}if(b.dirty||b.dirtyT||!b.bbox){if(b.dirty||!this.realPath)b.bboxwt=0,this.realPath=bi[this.type](this);b.bbox=bI(bj(this.realPath,this.matrix)),b.bbox.toString=cq,b.dirty=b.dirtyT=0}return b.bbox},cl.clone=function(){if(this.removed)return null;var a=this.paper[this.type]().attr(this.attr());this.__set__&&this.__set__.push(a);return a},cl.glow=function(a){if(this.type=="text")return null;a=a||{};var b={width:(a.width||10)+(+this.attr("stroke-width")||1),fill:a.fill||!1,opacity:a.opacity||.5,offsetx:a.offsetx||0,offsety:a.offsety||0,color:a.color||"#000"},c=b.width/2,d=this.paper,e=d.set(),f=this.realPath||bi[this.type](this);f=this.matrix?bj(f,this.matrix):f;for(var g=1;g<c+1;g++)e.push(d.path(f).attr({stroke:b.color,fill:b.fill?b.color:"none","stroke-linejoin":"round","stroke-linecap":"round","stroke-width":+(b.width/c*g).toFixed(3),opacity:+(b.opacity/c).toFixed(3)}));return e.insertBefore(this).translate(b.offsetx,b.offsety)};var cr={},cs=function(b,c,d,e,f,g,h,i,j){return j==null?bB(b,c,d,e,f,g,h,i):a.findDotsAtSegment(b,c,d,e,f,g,h,i,bC(b,c,d,e,f,g,h,i,j))},ct=function(b,c){return function(d,e,f){d=bR(d);var g,h,i,j,k="",l={},m,n=0;for(var o=0,p=d.length;o<p;o++){i=d[o];if(i[0]=="M")g=+i[1],h=+i[2];else{j=cs(g,h,i[1],i[2],i[3],i[4],i[5],i[6]);if(n+j>e){if(c&&!l.start){m=cs(g,h,i[1],i[2],i[3],i[4],i[5],i[6],e-n),k+=["C"+m.start.x,m.start.y,m.m.x,m.m.y,m.x,m.y];if(f)return k;l.start=k,k=["M"+m.x,m.y+"C"+m.n.x,m.n.y,m.end.x,m.end.y,i[5],i[6]].join(),n+=j,g=+i[5],h=+i[6];continue}if(!b&&!c){m=cs(g,h,i[1],i[2],i[3],i[4],i[5],i[6],e-n);return{x:m.x,y:m.y,alpha:m.alpha}}}n+=j,g=+i[5],h=+i[6]}k+=i.shift()+i}l.end=k,m=b?n:c?l:a.findDotsAtSegment(g,h,i[0],i[1],i[2],i[3],i[4],i[5],1),m.alpha&&(m={x:m.x,y:m.y,alpha:m.alpha});return m}},cu=ct(1),cv=ct(),cw=ct(0,1);a.getTotalLength=cu,a.getPointAtLength=cv,a.getSubpath=function(a,b,c){if(this.getTotalLength(a)-c<1e-6)return cw(a,b).end;var d=cw(a,c,1);return b?cw(d,b).end:d},cl.getTotalLength=function(){if(this.type=="path"){if(this.node.getTotalLength)return this.node.getTotalLength();return cu(this.attrs.path)}},cl.getPointAtLength=function(a){if(this.type=="path")return cv(this.attrs.path,a)},cl.getSubpath=function(b,c){if(this.type=="path")return a.getSubpath(this.attrs.path,b,c)};var cx=a.easing_formulas={linear:function(a){return a},"<":function(a){return A(a,1.7)},">":function(a){return A(a,.48)},"<>":function(a){var b=.48-a/1.04,c=w.sqrt(.1734+b*b),d=c-b,e=A(z(d),1/3)*(d<0?-1:1),f=-c-b,g=A(z(f),1/3)*(f<0?-1:1),h=e+g+.5;return(1-h)*3*h*h+h*h*h},backIn:function(a){var b=1.70158;return a*a*((b+1)*a-b)},backOut:function(a){a=a-1;var b=1.70158;return a*a*((b+1)*a+b)+1},elastic:function(a){if(a==!!a)return a;return A(2,-10*a)*w.sin((a-.075)*2*B/.3)+1},bounce:function(a){var b=7.5625,c=2.75,d;a<1/c?d=b*a*a:a<2/c?(a-=1.5/c,d=b*a*a+.75):a<2.5/c?(a-=2.25/c,d=b*a*a+.9375):(a-=2.625/c,d=b*a*a+.984375);return d}};cx.easeIn=cx["ease-in"]=cx["<"],cx.easeOut=cx["ease-out"]=cx[">"],cx.easeInOut=cx["ease-in-out"]=cx["<>"],cx["back-in"]=cx.backIn,cx["back-out"]=cx.backOut;var cy=[],cz=window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||window.oRequestAnimationFrame||window.msRequestAnimationFrame||function(a){setTimeout(a,16)},cA=function(){var b=+(new Date),c=0;for(;c<cy.length;c++){var d=cy[c];if(d.el.removed||d.paused)continue;var e=b-d.start,f=d.ms,h=d.easing,i=d.from,j=d.diff,k=d.to,l=d.t,m=d.el,o={},p,r={},s;d.initstatus?(e=(d.initstatus*d.anim.top-d.prev)/(d.percent-d.prev)*f,d.status=d.initstatus,delete d.initstatus,d.stop&&cy.splice(c--,1)):d.status=(d.prev+(d.percent-d.prev)*(e/f))/d.anim.top;if(e<0)continue;if(e<f){var t=h(e/f);for(var u in i)if(i[g](u)){switch(U[u]){case C:p=+i[u]+t*f*j[u];break;case"colour":p="rgb("+[cB(O(i[u].r+t*f*j[u].r)),cB(O(i[u].g+t*f*j[u].g)),cB(O(i[u].b+t*f*j[u].b))].join(",")+")";break;case"path":p=[];for(var v=0,w=i[u].length;v<w;v++){p[v]=[i[u][v][0]];for(var x=1,y=i[u][v].length;x<y;x++)p[v][x]=+i[u][v][x]+t*f*j[u][v][x];p[v]=p[v].join(q)}p=p.join(q);break;case"transform":if(j[u].real){p=[];for(v=0,w=i[u].length;v<w;v++){p[v]=[i[u][v][0]];for(x=1,y=i[u][v].length;x<y;x++)p[v][x]=i[u][v][x]+t*f*j[u][v][x]}}else{var z=function(a){return+i[u][a]+t*f*j[u][a]};p=[["m",z(0),z(1),z(2),z(3),z(4),z(5)]]}break;case"csv":if(u=="clip-rect"){p=[],v=4;while(v--)p[v]=+i[u][v]+t*f*j[u][v]}break;default:var A=[][n](i[u]);p=[],v=m.paper.customAttributes[u].length;while(v--)p[v]=+A[v]+t*f*j[u][v]}o[u]=p}m.attr(o),function(a,b,c){setTimeout(function(){eve("raphael.anim.frame."+a,b,c)})}(m.id,m,d.anim)}else{(function(b,c,d){setTimeout(function(){eve("raphael.anim.frame."+c.id,c,d),eve("raphael.anim.finish."+c.id,c,d),a.is(b,"function")&&b.call(c)})})(d.callback,m,d.anim),m.attr(k),cy.splice(c--,1);if(d.repeat>1&&!d.next){for(s in k)k[g](s)&&(r[s]=d.totalOrigin[s]);d.el.attr(r),cE(d.anim,d.el,d.anim.percents[0],null,d.totalOrigin,d.repeat-1)}d.next&&!d.stop&&cE(d.anim,d.el,d.next,null,d.totalOrigin,d.repeat)}}a.svg&&m&&m.paper&&m.paper.safari(),cy.length&&cz(cA)},cB=function(a){return a>255?255:a<0?0:a};cl.animateWith=function(b,c,d,e,f,g){var h=this;if(h.removed){g&&g.call(h);return h}var i=d instanceof cD?d:a.animation(d,e,f,g),j,k;cE(i,h,i.percents[0],null,h.attr());for(var l=0,m=cy.length;l<m;l++)if(cy[l].anim==c&&cy[l].el==b){cy[m-1].start=cy[l].start;break}return h},cl.onAnimation=function(a){a?eve.on("raphael.anim.frame."+this.id,a):eve.unbind("raphael.anim.frame."+this.id);return this},cD.prototype.delay=function(a){var b=new cD(this.anim,this.ms);b.times=this.times,b.del=+a||0;return b},cD.prototype.repeat=function(a){var b=new cD(this.anim,this.ms);b.del=this.del,b.times=w.floor(x(a,0))||1;return b},a.animation=function(b,c,d,e){if(b instanceof cD)return b;if(a.is(d,"function")||!d)e=e||d||null,d=null;b=Object(b),c=+c||0;var f={},h,i;for(i in b)b[g](i)&&Q(i)!=i&&Q(i)+"%"!=i&&(h=!0,f[i]=b[i]);if(!h)return new cD(b,c);d&&(f.easing=d),e&&(f.callback=e);return new cD({100:f},c)},cl.animate=function(b,c,d,e){var f=this;if(f.removed){e&&e.call(f);return f}var g=b instanceof cD?b:a.animation(b,c,d,e);cE(g,f,g.percents[0],null,f.attr());return f},cl.setTime=function(a,b){a&&b!=null&&this.status(a,y(b,a.ms)/a.ms);return this},cl.status=function(a,b){var c=[],d=0,e,f;if(b!=null){cE(a,this,-1,y(b,1));return this}e=cy.length;for(;d<e;d++){f=cy[d];if(f.el.id==this.id&&(!a||f.anim==a)){if(a)return f.status;c.push({anim:f.anim,status:f.status})}}if(a)return 0;return c},cl.pause=function(a){for(var b=0;b<cy.length;b++)cy[b].el.id==this.id&&(!a||cy[b].anim==a)&&eve("raphael.anim.pause."+this.id,this,cy[b].anim)!==!1&&(cy[b].paused=!0);return this},cl.resume=function(a){for(var b=0;b<cy.length;b++)if(cy[b].el.id==this.id&&(!a||cy[b].anim==a)){var c=cy[b];eve("raphael.anim.resume."+this.id,this,c.anim)!==!1&&(delete c.paused,this.status(c.anim,c.status))}return this},cl.stop=function(a){for(var b=0;b<cy.length;b++)cy[b].el.id==this.id&&(!a||cy[b].anim==a)&&eve("raphael.anim.stop."+this.id,this,cy[b].anim)!==!1&&cy.splice(b--,1);return this},eve.on("raphael.remove",cF),eve.on("raphael.clear",cF),cl.toString=function(){return"Raphaël’s object"};var cG=function(a){this.items=[],this.length=0,this.type="set";if(a)for(var b=0,c=a.length;b<c;b++)a[b]&&(a[b].constructor==cl.constructor||a[b].constructor==cG)&&(this[this.items.length]=this.items[this.items.length]=a[b],this.length++)},cH=cG.prototype;cH.push=function(){var a,b;for(var c=0,d=arguments.length;c<d;c++)a=arguments[c],a&&(a.constructor==cl.constructor||a.constructor==cG)&&(b=this.items.length,this[b]=this.items[b]=a,this.length++);return this},cH.pop=function(){this.length&&delete this[this.length--];return this.items.pop()},cH.forEach=function(a,b){for(var c=0,d=this.items.length;c<d;c++)if(a.call(b,this.items[c],c)===!1)return this;return this};for(var cI in cl)cl[g](cI)&&(cH[cI]=function(a){return function(){var b=arguments;return this.forEach(function(c){c[a][m](c,b)})}}(cI));cH.attr=function(b,c){if(b&&a.is(b,E)&&a.is(b[0],"object"))for(var d=0,e=b.length;d<e;d++)this.items[d].attr(b[d]);else for(var f=0,g=this.items.length;f<g;f++)this.items[f].attr(b,c);return this},cH.clear=function(){while(this.length)this.pop()},cH.splice=function(a,b,c){a=a<0?x(this.length+a,0):a,b=x(0,y(this.length-a,b));var d=[],e=[],f=[],g;for(g=2;g<arguments.length;g++)f.push(arguments[g]);for(g=0;g<b;g++)e.push(this[a+g]);for(;g<this.length-a;g++)d.push(this[a+g]);var h=f.length;for(g=0;g<h+d.length;g++)this.items[a+g]=this[a+g]=g<h?f[g]:d[g-h];g=this.items.length=this.length-=b-h;while(this[g])delete this[g++];return new cG(e)},cH.exclude=function(a){for(var b=0,c=this.length;b<c;b++)if(this[b]==a){this.splice(b,1);return!0}},cH.animate=function(b,c,d,e){(a.is(d,"function")||!d)&&(e=d||null);var f=this.items.length,g=f,h,i=this,j;if(!f)return this;e&&(j=function(){!--f&&e.call(i)}),d=a.is(d,D)?d:j;var k=a.animation(b,c,d,j);h=this.items[--g].animate(k);while(g--)this.items[g]&&!this.items[g].removed&&this.items[g].animateWith(h,k,k);return this},cH.insertAfter=function(a){var b=this.items.length;while(b--)this.items[b].insertAfter(a);return this},cH.getBBox=function(){var a=[],b=[],c=[],d=[];for(var e=this.items.length;e--;)if(!this.items[e].removed){var f=this.items[e].getBBox();a.push(f.x),b.push(f.y),c.push(f.x+f.width),d.push(f.y+f.height)}a=y[m](0,a),b=y[m](0,b),c=x[m](0,c),d=x[m](0,d);return{x:a,y:b,x2:c,y2:d,width:c-a,height:d-b}},cH.clone=function(a){a=new cG;for(var b=0,c=this.items.length;b<c;b++)a.push(this.items[b].clone());return a},cH.toString=function(){return"Raphaël‘s set"},a.registerFont=function(a){if(!a.face)return a;this.fonts=this.fonts||{};var b={w:a.w,face:{},glyphs:{}},c=a.face["font-family"];for(var d in a.face)a.face[g](d)&&(b.face[d]=a.face[d]);this.fonts[c]?this.fonts[c].push(b):this.fonts[c]=[b];if(!a.svg){b.face["units-per-em"]=R(a.face["units-per-em"],10);for(var e in a.glyphs)if(a.glyphs[g](e)){var f=a.glyphs[e];b.glyphs[e]={w:f.w,k:{},d:f.d&&"M"+f.d.replace(/[mlcxtrv]/g,function(a){return{l:"L",c:"C",x:"z",t:"m",r:"l",v:"c"}[a]||"M"})+"z"};if(f.k)for(var h in f.k)f[g](h)&&(b.glyphs[e].k[h]=f.k[h])}}return a},k.getFont=function(b,c,d,e){e=e||"normal",d=d||"normal",c=+c||{normal:400,bold:700,lighter:300,bolder:800}[c]||400;if(!!a.fonts){var f=a.fonts[b];if(!f){var h=new RegExp("(^|\\s)"+b.replace(/[^\w\d\s+!~.:_-]/g,p)+"(\\s|$)","i");for(var i in a.fonts)if(a.fonts[g](i)&&h.test(i)){f=a.fonts[i];break}}var j;if(f)for(var k=0,l=f.length;k<l;k++){j=f[k];if(j.face["font-weight"]==c&&(j.face["font-style"]==d||!j.face["font-style"])&&j.face["font-stretch"]==e)break}return j}},k.print=function(b,d,e,f,g,h,i){h=h||"middle",i=x(y(i||0,1),-1);var j=r(e)[s](p),k=0,l=0,m=p,n;a.is(f,e)&&(f=this.getFont(f));if(f){n=(g||16)/f.face["units-per-em"];var o=f.face.bbox[s](c),q=+o[0],t=o[3]-o[1],u=0,v=+o[1]+(h=="baseline"?t+ +f.face.descent:t/2);for(var w=0,z=j.length;w<z;w++){if(j[w]=="\n")k=0,B=0,l=0,u+=t;else{var A=l&&f.glyphs[j[w-1]]||{},B=f.glyphs[j[w]];k+=l?(A.w||f.w)+(A.k&&A.k[j[w]]||0)+f.w*i:0,l=1}B&&B.d&&(m+=a.transformPath(B.d,["t",k*n,u*n,"s",n,n,q,v,"t",(b-q)/n,(d-v)/n]))}}return this.path(m).attr({fill:"#000",stroke:"none"})},k.add=function(b){if(a.is(b,"array")){var c=this.set(),e=0,f=b.length,h;for(;e<f;e++)h=b[e]||{},d[g](h.type)&&c.push(this[h.type]().attr(h))}return c},a.format=function(b,c){var d=a.is(c,E)?[0][n](c):arguments;b&&a.is(b,D)&&d.length-1&&(b=b.replace(e,function(a,b){return d[++b]==null?p:d[b]}));return b||p},a.fullfill=function(){var a=/\{([^\}]+)\}/g,b=/(?:(?:^|\.)(.+?)(?=\[|\.|$|\()|\[('|")(.+?)\2\])(\(\))?/g,c=function(a,c,d){var e=d;c.replace(b,function(a,b,c,d,f){b=b||d,e&&(b in e&&(e=e[b]),typeof e=="function"&&f&&(e=e()))}),e=(e==null||e==d?a:e)+"";return e};return function(b,d){return String(b).replace(a,function(a,b){return c(a,b,d)})}}(),a.ninja=function(){i.was?h.win.Raphael=i.is:delete Raphael;return a},a.st=cH,function(b,c,d){function e(){/in/.test(b.readyState)?setTimeout(e,9):a.eve("raphael.DOMload")}b.readyState==null&&b.addEventListener&&(b.addEventListener(c,d=function(){b.removeEventListener(c,d,!1),b.readyState="complete"},!1),b.readyState="loading"),e()}(document,"DOMContentLoaded"),i.was?h.win.Raphael=a:Raphael=a,eve.on("raphael.DOMload",function(){b=!0})}(),window.Raphael.svg&&function(a){var b="hasOwnProperty",c=String,d=parseFloat,e=parseInt,f=Math,g=f.max,h=f.abs,i=f.pow,j=/[, ]+/,k=a.eve,l="",m=" ",n="http://www.w3.org/1999/xlink",o={block:"M5,0 0,2.5 5,5z",classic:"M5,0 0,2.5 5,5 3.5,3 3.5,2z",diamond:"M2.5,0 5,2.5 2.5,5 0,2.5z",open:"M6,1 1,3.5 6,6",oval:"M2.5,0A2.5,2.5,0,0,1,2.5,5 2.5,2.5,0,0,1,2.5,0z"},p={};a.toString=function(){return"Your browser supports SVG.\nYou are running Raphaël "+this.version};var q=function(d,e){if(e){typeof d=="string"&&(d=q(d));for(var f in e)e[b](f)&&(f.substring(0,6)=="xlink:"?d.setAttributeNS(n,f.substring(6),c(e[f])):d.setAttribute(f,c(e[f])))}else d=a._g.doc.createElementNS("http://www.w3.org/2000/svg",d),d.style&&(d.style.webkitTapHighlightColor="rgba(0,0,0,0)");return d},r=function(b,e){var j="linear",k=b.id+e,m=.5,n=.5,o=b.node,p=b.paper,r=o.style,s=a._g.doc.getElementById(k);if(!s){e=c(e).replace(a._radial_gradient,function(a,b,c){j="radial";if(b&&c){m=d(b),n=d(c);var e=(n>.5)*2-1;i(m-.5,2)+i(n-.5,2)>.25&&(n=f.sqrt(.25-i(m-.5,2))*e+.5)&&n!=.5&&(n=n.toFixed(5)-1e-5*e)}return l}),e=e.split(/\s*\-\s*/);if(j=="linear"){var t=e.shift();t=-d(t);if(isNaN(t))return null;var u=[0,0,f.cos(a.rad(t)),f.sin(a.rad(t))],v=1/(g(h(u[2]),h(u[3]))||1);u[2]*=v,u[3]*=v,u[2]<0&&(u[0]=-u[2],u[2]=0),u[3]<0&&(u[1]=-u[3],u[3]=0)}var w=a._parseDots(e);if(!w)return null;k=k.replace(/[\(\)\s,\xb0#]/g,"_"),b.gradient&&k!=b.gradient.id&&(p.defs.removeChild(b.gradient),delete b.gradient);if(!b.gradient){s=q(j+"Gradient",{id:k}),b.gradient=s,q(s,j=="radial"?{fx:m,fy:n}:{x1:u[0],y1:u[1],x2:u[2],y2:u[3],gradientTransform:b.matrix.invert()}),p.defs.appendChild(s);for(var x=0,y=w.length;x<y;x++)s.appendChild(q("stop",{offset:w[x].offset?w[x].offset:x?"100%":"0%","stop-color":w[x].color||"#fff"}))}}q(o,{fill:"url(#"+k+")",opacity:1,"fill-opacity":1}),r.fill=l,r.opacity=1,r.fillOpacity=1;return 1},s=function(a){var b=a.getBBox(1);q(a.pattern,{patternTransform:a.matrix.invert()+" translate("+b.x+","+b.y+")"})},t=function(d,e,f){if(d.type=="path"){var g=c(e).toLowerCase().split("-"),h=d.paper,i=f?"end":"start",j=d.node,k=d.attrs,m=k["stroke-width"],n=g.length,r="classic",s,t,u,v,w,x=3,y=3,z=5;while(n--)switch(g[n]){case"block":case"classic":case"oval":case"diamond":case"open":case"none":r=g[n];break;case"wide":y=5;break;case"narrow":y=2;break;case"long":x=5;break;case"short":x=2}r=="open"?(x+=2,y+=2,z+=2,u=1,v=f?4:1,w={fill:"none",stroke:k.stroke}):(v=u=x/2,w={fill:k.stroke,stroke:"none"}),d._.arrows?f?(d._.arrows.endPath&&p[d._.arrows.endPath]--,d._.arrows.endMarker&&p[d._.arrows.endMarker]--):(d._.arrows.startPath&&p[d._.arrows.startPath]--,d._.arrows.startMarker&&p[d._.arrows.startMarker]--):d._.arrows={};if(r!="none"){var A="raphael-marker-"+r,B="raphael-marker-"+i+r+x+y;a._g.doc.getElementById(A)?p[A]++:(h.defs.appendChild(q(q("path"),{"stroke-linecap":"round",d:o[r],id:A})),p[A]=1);var C=a._g.doc.getElementById(B),D;C?(p[B]++,D=C.getElementsByTagName("use")[0]):(C=q(q("marker"),{id:B,markerHeight:y,markerWidth:x,orient:"auto",refX:v,refY:y/2}),D=q(q("use"),{"xlink:href":"#"+A,transform:(f?"rotate(180 "+x/2+" "+y/2+") ":l)+"scale("+x/z+","+y/z+")","stroke-width":(1/((x/z+y/z)/2)).toFixed(4)}),C.appendChild(D),h.defs.appendChild(C),p[B]=1),q(D,w);var F=u*(r!="diamond"&&r!="oval");f?(s=d._.arrows.startdx*m||0,t=a.getTotalLength(k.path)-F*m):(s=F*m,t=a.getTotalLength(k.path)-(d._.arrows.enddx*m||0)),w={},w["marker-"+i]="url(#"+B+")";if(t||s)w.d=Raphael.getSubpath(k.path,s,t);q(j,w),d._.arrows[i+"Path"]=A,d._.arrows[i+"Marker"]=B,d._.arrows[i+"dx"]=F,d._.arrows[i+"Type"]=r,d._.arrows[i+"String"]=e}else f?(s=d._.arrows.startdx*m||0,t=a.getTotalLength(k.path)-s):(s=0,t=a.getTotalLength(k.path)-(d._.arrows.enddx*m||0)),d._.arrows[i+"Path"]&&q(j,{d:Raphael.getSubpath(k.path,s,t)}),delete d._.arrows[i+"Path"],delete d._.arrows[i+"Marker"],delete d._.arrows[i+"dx"],delete d._.arrows[i+"Type"],delete d._.arrows[i+"String"];for(w in p)if(p[b](w)&&!p[w]){var G=a._g.doc.getElementById(w);G&&G.parentNode.removeChild(G)}}},u={"":[0],none:[0],"-":[3,1],".":[1,1],"-.":[3,1,1,1],"-..":[3,1,1,1,1,1],". ":[1,3],"- ":[4,3],"--":[8,3],"- .":[4,3,1,3],"--.":[8,3,1,3],"--..":[8,3,1,3,1,3]},v=function(a,b,d){b=u[c(b).toLowerCase()];if(b){var e=a.attrs["stroke-width"]||"1",f={round:e,square:e,butt:0}[a.attrs["stroke-linecap"]||d["stroke-linecap"]]||0,g=[],h=b.length;while(h--)g[h]=b[h]*e+(h%2?1:-1)*f;q(a.node,{"stroke-dasharray":g.join(",")})}},w=function(d,f){var i=d.node,k=d.attrs,m=i.style.visibility;i.style.visibility="hidden";for(var o in f)if(f[b](o)){if(!a._availableAttrs[b](o))continue;var p=f[o];k[o]=p;switch(o){case"blur":d.blur(p);break;case"href":case"title":case"target":var u=i.parentNode;if(u.tagName.toLowerCase()!="a"){var w=q("a");u.insertBefore(w,i),w.appendChild(i),u=w}o=="target"?u.setAttributeNS(n,"show",p=="blank"?"new":p):u.setAttributeNS(n,o,p);break;case"cursor":i.style.cursor=p;break;case"transform":d.transform(p);break;case"arrow-start":t(d,p);break;case"arrow-end":t(d,p,1);break;case"clip-rect":var x=c(p).split(j);if(x.length==4){d.clip&&d.clip.parentNode.parentNode.removeChild(d.clip.parentNode);var z=q("clipPath"),A=q("rect");z.id=a.createUUID(),q(A,{x:x[0],y:x[1],width:x[2],height:x[3]}),z.appendChild(A),d.paper.defs.appendChild(z),q(i,{"clip-path":"url(#"+z.id+")"}),d.clip=A}if(!p){var B=i.getAttribute("clip-path");if(B){var C=a._g.doc.getElementById(B.replace(/(^url\(#|\)$)/g,l));C&&C.parentNode.removeChild(C),q(i,{"clip-path":l}),delete d.clip}}break;case"path":d.type=="path"&&(q(i,{d:p?k.path=a._pathToAbsolute(p):"M0,0"}),d._.dirty=1,d._.arrows&&("startString"in d._.arrows&&t(d,d._.arrows.startString),"endString"in d._.arrows&&t(d,d._.arrows.endString,1)));break;case"width":i.setAttribute(o,p),d._.dirty=1;if(k.fx)o="x",p=k.x;else break;case"x":k.fx&&(p=-k.x-(k.width||0));case"rx":if(o=="rx"&&d.type=="rect")break;case"cx":i.setAttribute(o,p),d.pattern&&s(d),d._.dirty=1;break;case"height":i.setAttribute(o,p),d._.dirty=1;if(k.fy)o="y",p=k.y;else break;case"y":k.fy&&(p=-k.y-(k.height||0));case"ry":if(o=="ry"&&d.type=="rect")break;case"cy":i.setAttribute(o,p),d.pattern&&s(d),d._.dirty=1;break;case"r":d.type=="rect"?q(i,{rx:p,ry:p}):i.setAttribute(o,p),d._.dirty=1;break;case"src":d.type=="image"&&i.setAttributeNS(n,"href",p);break;case"stroke-width":if(d._.sx!=1||d._.sy!=1)p/=g(h(d._.sx),h(d._.sy))||1;d.paper._vbSize&&(p*=d.paper._vbSize),i.setAttribute(o,p),k["stroke-dasharray"]&&v(d,k["stroke-dasharray"],f),d._.arrows&&("startString"in d._.arrows&&t(d,d._.arrows.startString),"endString"in d._.arrows&&t(d,d._.arrows.endString,1));break;case"stroke-dasharray":v(d,p,f);break;case"fill":var D=c(p).match(a._ISURL);if(D){z=q("pattern");var F=q("image");z.id=a.createUUID(),q(z,{x:0,y:0,patternUnits:"userSpaceOnUse",height:1,width:1}),q(F,{x:0,y:0,"xlink:href":D[1]}),z.appendChild(F),function(b){a._preload(D[1],function(){var a=this.offsetWidth,c=this.offsetHeight;q(b,{width:a,height:c}),q(F,{width:a,height:c}),d.paper.safari()})}(z),d.paper.defs.appendChild(z),q(i,{fill:"url(#"+z.id+")"}),d.pattern=z,d.pattern&&s(d);break}var G=a.getRGB(p);if(!G.error)delete f.gradient,delete k.gradient,!a.is(k.opacity,"undefined")&&a.is(f.opacity,"undefined")&&q(i,{opacity:k.opacity}),!a.is(k["fill-opacity"],"undefined")&&a.is(f["fill-opacity"],"undefined")&&q(i,{"fill-opacity":k["fill-opacity"]});else if((d.type=="circle"||d.type=="ellipse"||c(p).charAt()!="r")&&r(d,p)){if("opacity"in k||"fill-opacity"in k){var H=a._g.doc.getElementById(i.getAttribute("fill").replace(/^url\(#|\)$/g,l));if(H){var I=H.getElementsByTagName("stop");q(I[I.length-1],{"stop-opacity":("opacity"in k?k.opacity:1)*("fill-opacity"in k?k["fill-opacity"]:1)})}}k.gradient=p,k.fill="none";break}G[b]("opacity")&&q(i,{"fill-opacity":G.opacity>1?G.opacity/100:G.opacity});case"stroke":G=a.getRGB(p),i.setAttribute(o,G.hex),o=="stroke"&&G[b]("opacity")&&q(i,{"stroke-opacity":G.opacity>1?G.opacity/100:G.opacity}),o=="stroke"&&d._.arrows&&("startString"in d._.arrows&&t(d,d._.arrows.startString),"endString"in d._.arrows&&t(d,d._.arrows.endString,1));break;case"gradient":(d.type=="circle"||d.type=="ellipse"||c(p).charAt()!="r")&&r(d,p);break;case"opacity":k.gradient&&!k[b]("stroke-opacity")&&q(i,{"stroke-opacity":p>1?p/100:p});case"fill-opacity":if(k.gradient){H=a._g.doc.getElementById(i.getAttribute("fill").replace(/^url\(#|\)$/g,l)),H&&(I=H.getElementsByTagName("stop"),q(I[I.length-1],{"stop-opacity":p}));break};default:o=="font-size"&&(p=e(p,10)+"px");var J=o.replace(/(\-.)/g,function(a){return a.substring(1).toUpperCase()});i.style[J]=p,d._.dirty=1,i.setAttribute(o,p)}}y(d,f),i.style.visibility=m},x=1.2,y=function(d,f){if(d.type=="text"&&!!(f[b]("text")||f[b]("font")||f[b]("font-size")||f[b]("x")||f[b]("y"))){var g=d.attrs,h=d.node,i=h.firstChild?e(a._g.doc.defaultView.getComputedStyle(h.firstChild,l).getPropertyValue("font-size"),10):10;if(f[b]("text")){g.text=f.text;while(h.firstChild)h.removeChild(h.firstChild);var j=c(f.text).split("\n"),k=[],m;for(var n=0,o=j.length;n<o;n++)m=q("tspan"),n&&q(m,{dy:i*x,x:g.x}),m.appendChild(a._g.doc.createTextNode(j[n])),h.appendChild(m),k[n]=m}else{k=h.getElementsByTagName("tspan");for(n=0,o=k.length;n<o;n++)n?q(k[n],{dy:i*x,x:g.x}):q(k[0],{dy:0})}q(h,{x:g.x,y:g.y}),d._.dirty=1;var p=d._getBBox(),r=g.y-(p.y+p.height/2);r&&a.is(r,"finite")&&q(k[0],{dy:r})}},z=function(b,c){var d=0,e=0;this[0]=this.node=b,b.raphael=!0,this.id=a._oid++,b.raphaelid=this.id,this.matrix=a.matrix(),this.realPath=null,this.paper=c,this.attrs=this.attrs||{},this._={transform:[],sx:1,sy:1,deg:0,dx:0,dy:0,dirty:1},!c.bottom&&(c.bottom=this),this.prev=c.top,c.top&&(c.top.next=this),c.top=this,this.next=null},A=a.el;z.prototype=A,A.constructor=z,a._engine.path=function(a,b){var c=q("path");b.canvas&&b.canvas.appendChild(c);var d=new z(c,b);d.type="path",w(d,{fill:"none",stroke:"#000",path:a});return d},A.rotate=function(a,b,e){if(this.removed)return this;a=c(a).split(j),a.length-1&&(b=d(a[1]),e=d(a[2])),a=d(a[0]),e==null&&(b=e);if(b==null||e==null){var f=this.getBBox(1);b=f.x+f.width/2,e=f.y+f.height/2}this.transform(this._.transform.concat([["r",a,b,e]]));return this},A.scale=function(a,b,e,f){if(this.removed)return this;a=c(a).split(j),a.length-1&&(b=d(a[1]),e=d(a[2]),f=d(a[3])),a=d(a[0]),b==null&&(b=a),f==null&&(e=f);if(e==null||f==null)var g=this.getBBox(1);e=e==null?g.x+g.width/2:e,f=f==null?g.y+g.height/2:f,this.transform(this._.transform.concat([["s",a,b,e,f]]));return this},A.translate=function(a,b){if(this.removed)return this;a=c(a).split(j),a.length-1&&(b=d(a[1])),a=d(a[0])||0,b=+b||0,this.transform(this._.transform.concat([["t",a,b]]));return this},A.transform=function(c){var d=this._;if(c==null)return d.transform;a._extractTransform(this,c),this.clip&&q(this.clip,{transform:this.matrix.invert()}),this.pattern&&s(this),this.node&&q(this.node,{transform:this.matrix});if(d.sx!=1||d.sy!=1){var e=this.attrs[b]("stroke-width")?this.attrs["stroke-width"]:1;this.attr({"stroke-width":e})}return this},A.hide=function(){!this.removed&&this.paper.safari(this.node.style.display="none");return this},A.show=function(){!this.removed&&this.paper.safari(this.node.style.display="");return this},A.remove=function(){if(!this.removed&&!!this.node.parentNode){var b=this.paper;b.__set__&&b.__set__.exclude(this),k.unbind("raphael.*.*."+this.id),this.gradient&&b.defs.removeChild(this.gradient),a._tear(this,b),this.node.parentNode.tagName.toLowerCase()=="a"?this.node.parentNode.parentNode.removeChild(this.node.parentNode):this.node.parentNode.removeChild(this.node);for(var c in this)this[c]=typeof this[c]=="function"?a._removedFactory(c):null;this.removed=!0}},A._getBBox=function(){if(this.node.style.display=="none"){this.show();var a=!0}var b={};try{b=this.node.getBBox()}catch(c){}finally{b=b||{}}a&&this.hide();return b},A.attr=function(c,d){if(this.removed)return this;if(c==null){var e={};for(var f in this.attrs)this.attrs[b](f)&&(e[f]=this.attrs[f]);e.gradient&&e.fill=="none"&&(e.fill=e.gradient)&&delete e.gradient,e.transform=this._.transform;return e}if(d==null&&a.is(c,"string")){if(c=="fill"&&this.attrs.fill=="none"&&this.attrs.gradient)return this.attrs.gradient;if(c=="transform")return this._.transform;var g=c.split(j),h={};for(var i=0,l=g.length;i<l;i++)c=g[i],c in this.attrs?h[c]=this.attrs[c]:a.is(this.paper.customAttributes[c],"function")?h[c]=this.paper.customAttributes[c].def:h[c]=a._availableAttrs[c];return l-1?h:h[g[0]]}if(d==null&&a.is(c,"array")){h={};for(i=0,l=c.length;i<l;i++)h[c[i]]=this.attr(c[i]);return h}if(d!=null){var m={};m[c]=d}else c!=null&&a.is(c,"object")&&(m=c);for(var n in m)k("raphael.attr."+n+"."+this.id,this,m[n]);for(n in this.paper.customAttributes)if(this.paper.customAttributes[b](n)&&m[b](n)&&a.is(this.paper.customAttributes[n],"function")){var o=this.paper.customAttributes[n].apply(this,[].concat(m[n]));this.attrs[n]=m[n];for(var p in o)o[b](p)&&(m[p]=o[p])}w(this,m);return this},A.toFront=function(){if(this.removed)return this;this.node.parentNode.tagName.toLowerCase()=="a"?this.node.parentNode.parentNode.appendChild(this.node.parentNode):this.node.parentNode.appendChild(this.node);var b=this.paper;b.top!=this&&a._tofront(this,b);return this},A.toBack=function(){if(this.removed)return this;var b=this.node.parentNode;b.tagName.toLowerCase()=="a"?b.parentNode.insertBefore(this.node.parentNode,this.node.parentNode.parentNode.firstChild):b.firstChild!=this.node&&b.insertBefore(this.node,this.node.parentNode.firstChild),a._toback(this,this.paper);var c=this.paper;return this},A.insertAfter=function(b){if(this.removed)return this;var c=b.node||b[b.length-1].node;c.nextSibling?c.parentNode.insertBefore(this.node,c.nextSibling):c.parentNode.appendChild(this.node),a._insertafter(this,b,this.paper);return this},A.insertBefore=function(b){if(this.removed)return this;var c=b.node||b[0].node;c.parentNode.insertBefore(this.node,c),a._insertbefore(this,b,this.paper);return this},A.blur=function(b){var c=this;if(+b!==0){var d=q("filter"),e=q("feGaussianBlur");c.attrs.blur=b,d.id=a.createUUID(),q(e,{stdDeviation:+b||1.5}),d.appendChild(e),c.paper.defs.appendChild(d),c._blur=d,q(c.node,{filter:"url(#"+d.id+")"})}else c._blur&&(c._blur.parentNode.removeChild(c._blur),delete c._blur,delete c.attrs.blur),c.node.removeAttribute("filter")},a._engine.circle=function(a,b,c,d){var e=q("circle");a.canvas&&a.canvas.appendChild(e);var f=new z(e,a);f.attrs={cx:b,cy:c,r:d,fill:"none",stroke:"#000"},f.type="circle",q(e,f.attrs);return f},a._engine.rect=function(a,b,c,d,e,f){var g=q("rect");a.canvas&&a.canvas.appendChild(g);var h=new z(g,a);h.attrs={x:b,y:c,width:d,height:e,r:f||0,rx:f||0,ry:f||0,fill:"none",stroke:"#000"},h.type="rect",q(g,h.attrs);return h},a._engine.ellipse=function(a,b,c,d,e){var f=q("ellipse");a.canvas&&a.canvas.appendChild(f);var g=new z(f,a);g.attrs={cx:b,cy:c,rx:d,ry:e,fill:"none",stroke:"#000"},g.type="ellipse",q(f,g.attrs);return g},a._engine.image=function(a,b,c,d,e,f){var g=q("image");q(g,{x:c,y:d,width:e,height:f,preserveAspectRatio:"none"}),g.setAttributeNS(n,"href",b),a.canvas&&a.canvas.appendChild(g);var h=new z(g,a);h.attrs={x:c,y:d,width:e,height:f,src:b},h.type="image";return h},a._engine.text=function(b,c,d,e){var f=q("text");b.canvas&&b.canvas.appendChild(f);var g=new z(f,b);g.attrs={x:c,y:d,"text-anchor":"middle",text:e,font:a._availableAttrs.font,stroke:"none",fill:"#000"},g.type="text",w(g,g.attrs);return g},a._engine.setSize=function(a,b){this.width=a||this.width,this.height=b||this.height,this.canvas.setAttribute("width",this.width),this.canvas.setAttribute("height",this.height),this._viewBox&&this.setViewBox.apply(this,this._viewBox);return this},a._engine.create=function(){var b=a._getContainer.apply(0,arguments),c=b&&b.container,d=b.x,e=b.y,f=b.width,g=b.height;if(!c)throw new Error("SVG container not found.");var h=q("svg"),i="overflow:hidden;",j;d=d||0,e=e||0,f=f||512,g=g||342,q(h,{height:g,version:1.1,width:f,xmlns:"http://www.w3.org/2000/svg"}),c==1?(h.style.cssText=i+"position:absolute;left:"+d+"px;top:"+e+"px",a._g.doc.body.appendChild(h),j=1):(h.style.cssText=i+"position:relative",c.firstChild?c.insertBefore(h,c.firstChild):c.appendChild(h)),c=new a._Paper,c.width=f,c.height=g,c.canvas=h,c.clear(),c._left=c._top=0,j&&(c.renderfix=function(){}),c.renderfix();return c},a._engine.setViewBox=function(a,b,c,d,e){k("raphael.setViewBox",this,this._viewBox,[a,b,c,d,e]);var f=g(c/this.width,d/this.height),h=this.top,i=e?"meet":"xMinYMin",j,l;a==null?(this._vbSize&&(f=1),delete this._vbSize,j="0 0 "+this.width+m+this.height):(this._vbSize=f,j=a+m+b+m+c+m+d),q(this.canvas,{viewBox:j,preserveAspectRatio:i});while(f&&h)l="stroke-width"in h.attrs?h.attrs["stroke-width"]:1,h.attr({"stroke-width":l}),h._.dirty=1,h._.dirtyT=1,h=h.prev;this._viewBox=[a,b,c,d,!!e];return this},a.prototype.renderfix=function(){var a=this.canvas,b=a.style,c;try{c=a.getScreenCTM()||a.createSVGMatrix()}catch(d){c=a.createSVGMatrix()}var e=-c.e%1,f=-c.f%1;if(e||f)e&&(this._left=(this._left+e)%1,b.left=this._left+"px"),f&&(this._top=(this._top+f)%1,b.top=this._top+"px")},a.prototype.clear=function(){a.eve("raphael.clear",this);var b=this.canvas;while(b.firstChild)b.removeChild(b.firstChild);this.bottom=this.top=null,(this.desc=q("desc")).appendChild(a._g.doc.createTextNode("Created with Raphaël "+a.version)),b.appendChild(this.desc),b.appendChild(this.defs=q("defs"))},a.prototype.remove=function(){k("raphael.remove",this),this.canvas.parentNode&&this.canvas.parentNode.removeChild(this.canvas);for(var b in this)this[b]=typeof this[b]=="function"?a._removedFactory(b):null};var B=a.st;for(var C in A)A[b](C)&&!B[b](C)&&(B[C]=function(a){return function(){var b=arguments;return this.forEach(function(c){c[a].apply(c,b)})}}(C))}(window.Raphael),window.Raphael.vml&&function(a){var b="hasOwnProperty",c=String,d=parseFloat,e=Math,f=e.round,g=e.max,h=e.min,i=e.abs,j="fill",k=/[, ]+/,l=a.eve,m=" progid:DXImageTransform.Microsoft",n=" ",o="",p={M:"m",L:"l",C:"c",Z:"x",m:"t",l:"r",c:"v",z:"x"},q=/([clmz]),?([^clmz]*)/gi,r=/ progid:\S+Blur\([^\)]+\)/g,s=/-?[^,\s-]+/g,t="position:absolute;left:0;top:0;width:1px;height:1px",u=21600,v={path:1,rect:1,image:1},w={circle:1,ellipse:1},x=function(b){var d=/[ahqstv]/ig,e=a._pathToAbsolute;c(b).match(d)&&(e=a._path2curve),d=/[clmz]/g;if(e==a._pathToAbsolute&&!c(b).match(d)){var g=c(b).replace(q,function(a,b,c){var d=[],e=b.toLowerCase()=="m",g=p[b];c.replace(s,function(a){e&&d.length==2&&(g+=d+p[b=="m"?"l":"L"],d=[]),d.push(f(a*u))});return g+d});return g}var h=e(b),i,j;g=[];for(var k=0,l=h.length;k<l;k++){i=h[k],j=h[k][0].toLowerCase(),j=="z"&&(j="x");for(var m=1,r=i.length;m<r;m++)j+=f(i[m]*u)+(m!=r-1?",":o);g.push(j)}return g.join(n)},y=function(b,c,d){var e=a.matrix();e.rotate(-b,.5,.5);return{dx:e.x(c,d),dy:e.y(c,d)}},z=function(a,b,c,d,e,f){var g=a._,h=a.matrix,k=g.fillpos,l=a.node,m=l.style,o=1,p="",q,r=u/b,s=u/c;m.visibility="hidden";if(!!b&&!!c){l.coordsize=i(r)+n+i(s),m.rotation=f*(b*c<0?-1:1);if(f){var t=y(f,d,e);d=t.dx,e=t.dy}b<0&&(p+="x"),c<0&&(p+=" y")&&(o=-1),m.flip=p,l.coordorigin=d*-r+n+e*-s;if(k||g.fillsize){var v=l.getElementsByTagName(j);v=v&&v[0],l.removeChild(v),k&&(t=y(f,h.x(k[0],k[1]),h.y(k[0],k[1])),v.position=t.dx*o+n+t.dy*o),g.fillsize&&(v.size=g.fillsize[0]*i(b)+n+g.fillsize[1]*i(c)),l.appendChild(v)}m.visibility="visible"}};a.toString=function(){return"Your browser doesn’t support SVG. Falling down to VML.\nYou are running Raphaël "+this.version};var A=function(a,b,d){var e=c(b).toLowerCase().split("-"),f=d?"end":"start",g=e.length,h="classic",i="medium",j="medium";while(g--)switch(e[g]){case"block":case"classic":case"oval":case"diamond":case"open":case"none":h=e[g];break;case"wide":case"narrow":j=e[g];break;case"long":case"short":i=e[g]}var k=a.node.getElementsByTagName("stroke")[0];k[f+"arrow"]=h,k[f+"arrowlength"]=i,k[f+"arrowwidth"]=j},B=function(e,i){e.attrs=e.attrs||{};var l=e.node,m=e.attrs,p=l.style,q,r=v[e.type]&&(i.x!=m.x||i.y!=m.y||i.width!=m.width||i.height!=m.height||i.cx!=m.cx||i.cy!=m.cy||i.rx!=m.rx||i.ry!=m.ry||i.r!=m.r),s=w[e.type]&&(m.cx!=i.cx||m.cy!=i.cy||m.r!=i.r||m.rx!=i.rx||m.ry!=i.ry),t=e;for(var y in i)i[b](y)&&(m[y]=i[y]);r&&(m.path=a._getPath[e.type](e),e._.dirty=1),i.href&&(l.href=i.href),i.title&&(l.title=i.title),i.target&&(l.target=i.target),i.cursor&&(p.cursor=i.cursor),"blur"in i&&e.blur(i.blur);if(i.path&&e.type=="path"||r)l.path=x(~c(m.path).toLowerCase().indexOf("r")?a._pathToAbsolute(m.path):m.path),e.type=="image"&&(e._.fillpos=[m.x,m.y],e._.fillsize=[m.width,m.height],z(e,1,1,0,0,0));"transform"in i&&e.transform(i.transform);if(s){var B=+m.cx,D=+m.cy,E=+m.rx||+m.r||0,G=+m.ry||+m.r||0;l.path=a.format("ar{0},{1},{2},{3},{4},{1},{4},{1}x",f((B-E)*u),f((D-G)*u),f((B+E)*u),f((D+G)*u),f(B*u))}if("clip-rect"in i){var H=c(i["clip-rect"]).split(k);if(H.length==4){H[2]=+H[2]+ +H[0],H[3]=+H[3]+ +H[1];var I=l.clipRect||a._g.doc.createElement("div"),J=I.style;J.clip=a.format("rect({1}px {2}px {3}px {0}px)",H),l.clipRect||(J.position="absolute",J.top=0,J.left=0,J.width=e.paper.width+"px",J.height=e.paper.height+"px",l.parentNode.insertBefore(I,l),I.appendChild(l),l.clipRect=I)}i["clip-rect"]||l.clipRect&&(l.clipRect.style.clip="auto")}if(e.textpath){var K=e.textpath.style;i.font&&(K.font=i.font),i["font-family"]&&(K.fontFamily='"'+i["font-family"].split(",")[0].replace(/^['"]+|['"]+$/g,o)+'"'),i["font-size"]&&(K.fontSize=i["font-size"]),i["font-weight"]&&(K.fontWeight=i["font-weight"]),i["font-style"]&&(K.fontStyle=i["font-style"])}"arrow-start"in i&&A(t,i["arrow-start"]),"arrow-end"in i&&A(t,i["arrow-end"],1);if(i.opacity!=null||i["stroke-width"]!=null||i.fill!=null||i.src!=null||i.stroke!=null||i["stroke-width"]!=null||i["stroke-opacity"]!=null||i["fill-opacity"]!=null||i["stroke-dasharray"]!=null||i["stroke-miterlimit"]!=null||i["stroke-linejoin"]!=null||i["stroke-linecap"]!=null){var L=l.getElementsByTagName(j),M=!1;L=L&&L[0],!L&&(M=L=F(j)),e.type=="image"&&i.src&&(L.src=i.src),i.fill&&(L.on=!0);if(L.on==null||i.fill=="none"||i.fill===null)L.on=!1;if(L.on&&i.fill){var N=c(i.fill).match(a._ISURL);if(N){L.parentNode==l&&l.removeChild(L),L.rotate=!0,L.src=N[1],L.type="tile";var O=e.getBBox(1);L.position=O.x+n+O.y,e._.fillpos=[O.x,O.y],a._preload(N[1],function(){e._.fillsize=[this.offsetWidth,this.offsetHeight]})}else L.color=a.getRGB(i.fill).hex,L.src=o,L.type="solid",a.getRGB(i.fill).error&&(t.type in{circle:1,ellipse:1}||c(i.fill).charAt()!="r")&&C(t,i.fill,L)&&(m.fill="none",m.gradient=i.fill,L.rotate=!1)}if("fill-opacity"in i||"opacity"in i){var P=((+m["fill-opacity"]+1||2)-1)*((+m.opacity+1||2)-1)*((+a.getRGB(i.fill).o+1||2)-1);P=h(g(P,0),1),L.opacity=P,L.src&&(L.color="none")}l.appendChild(L);var Q=l.getElementsByTagName("stroke")&&l.getElementsByTagName("stroke")[0],T=!1;!Q&&(T=Q=F("stroke"));if(i.stroke&&i.stroke!="none"||i["stroke-width"]||i["stroke-opacity"]!=null||i["stroke-dasharray"]||i["stroke-miterlimit"]||i["stroke-linejoin"]||i["stroke-linecap"])Q.on=!0;(i.stroke=="none"||i.stroke===null||Q.on==null||i.stroke==0||i["stroke-width"]==0)&&(Q.on=!1);var U=a.getRGB(i.stroke);Q.on&&i.stroke&&(Q.color=U.hex),P=((+m["stroke-opacity"]+1||2)-1)*((+m.opacity+1||2)-1)*((+U.o+1||2)-1);var V=(d(i["stroke-width"])||1)*.75;P=h(g(P,0),1),i["stroke-width"]==null&&(V=m["stroke-width"]),i["stroke-width"]&&(Q.weight=V),V&&V<1&&(P*=V)&&(Q.weight=1),Q.opacity=P,i["stroke-linejoin"]&&(Q.joinstyle=i["stroke-linejoin"]||"miter"),Q.miterlimit=i["stroke-miterlimit"]||8,i["stroke-linecap"]&&(Q.endcap=i["stroke-linecap"]=="butt"?"flat":i["stroke-linecap"]=="square"?"square":"round");if(i["stroke-dasharray"]){var W={"-":"shortdash",".":"shortdot","-.":"shortdashdot","-..":"shortdashdotdot",". ":"dot","- ":"dash","--":"longdash","- .":"dashdot","--.":"longdashdot","--..":"longdashdotdot"};Q.dashstyle=W[b](i["stroke-dasharray"])?W[i["stroke-dasharray"]]:o}T&&l.appendChild(Q)}if(t.type=="text"){t.paper.canvas.style.display=o;var X=t.paper.span,Y=100,Z=m.font&&m.font.match(/\d+(?:\.\d*)?(?=px)/);p=X.style,m.font&&(p.font=m.font),m["font-family"]&&(p.fontFamily=m["font-family"]),m["font-weight"]&&(p.fontWeight=m["font-weight"]),m["font-style"]&&(p.fontStyle=m["font-style"]),Z=d(m["font-size"]||Z&&Z[0])||10,p.fontSize=Z*Y+"px",t.textpath.string&&(X.innerHTML=c(t.textpath.string).replace(/</g,"&#60;").replace(/&/g,"&#38;").replace(/\n/g,"<br>"));var $=X.getBoundingClientRect();t.W=m.w=($.right-$.left)/Y,t.H=m.h=($.bottom-$.top)/Y,t.X=m.x,t.Y=m.y+t.H/2,("x"in i||"y"in i)&&(t.path.v=a.format("m{0},{1}l{2},{1}",f(m.x*u),f(m.y*u),f(m.x*u)+1));var _=["x","y","text","font","font-family","font-weight","font-style","font-size"];for(var ba=0,bb=_.length;ba<bb;ba++)if(_[ba]in i){t._.dirty=1;break}switch(m["text-anchor"]){case"start":t.textpath.style["v-text-align"]="left",t.bbx=t.W/2;break;case"end":t.textpath.style["v-text-align"]="right",t.bbx=-t.W/2;break;default:t.textpath.style["v-text-align"]="center",t.bbx=0}t.textpath.style["v-text-kern"]=!0}},C=function(b,f,g){b.attrs=b.attrs||{};var h=b.attrs,i=Math.pow,j,k,l="linear",m=".5 .5";b.attrs.gradient=f,f=c(f).replace(a._radial_gradient,function(a,b,c){l="radial",b&&c&&(b=d(b),c=d(c),i(b-.5,2)+i(c-.5,2)>.25&&(c=e.sqrt(.25-i(b-.5,2))*((c>.5)*2-1)+.5),m=b+n+c);return o}),f=f.split(/\s*\-\s*/);if(l=="linear"){var p=f.shift();p=-d(p);if(isNaN(p))return null}var q=a._parseDots(f);if(!q)return null;b=b.shape||b.node;if(q.length){b.removeChild(g),g.on=!0,g.method="none",g.color=q[0].color,g.color2=q[q.length-1].color;var r=[];for(var s=0,t=q.length;s<t;s++)q[s].offset&&r.push(q[s].offset+n+q[s].color);g.colors=r.length?r.join():"0% "+g.color,l=="radial"?(g.type="gradientTitle",g.focus="100%",g.focussize="0 0",g.focusposition=m,g.angle=0):(g.type="gradient",g.angle=(270-p)%360),b.appendChild(g)}return 1},D=function(b,c){this[0]=this.node=b,b.raphael=!0,this.id=a._oid++,b.raphaelid=this.id,this.X=0,this.Y=0,this.attrs={},this.paper=c,this.matrix=a.matrix(),this._={transform:[],sx:1,sy:1,dx:0,dy:0,deg:0,dirty:1,dirtyT:1},!c.bottom&&(c.bottom=this),this.prev=c.top,c.top&&(c.top.next=this),c.top=this,this.next=null},E=a.el;D.prototype=E,E.constructor=D,E.transform=function(b){if(b==null)return this._.transform;var d=this.paper._viewBoxShift,e=d?"s"+[d.scale,d.scale]+"-1-1t"+[d.dx,d.dy]:o,f;d&&(f=b=c(b).replace(/\.{3}|\u2026/g,this._.transform||o)),a._extractTransform(this,e+b);var g=this.matrix.clone(),h=this.skew,i=this.node,j,k=~c(this.attrs.fill).indexOf("-"),l=!c(this.attrs.fill).indexOf("url(");g.translate(-0.5,-0.5);if(l||k||this.type=="image"){h.matrix="1 0 0 1",h.offset="0 0",j=g.split();if(k&&j.noRotation||!j.isSimple){i.style.filter=g.toFilter();var m=this.getBBox(),p=this.getBBox(1),q=m.x-p.x,r=m.y-p.y;i.coordorigin=q*-u+n+r*-u,z(this,1,1,q,r,0)}else i.style.filter=o,z(this,j.scalex,j.scaley,j.dx,j.dy,j.rotate)}else i.style.filter=o,h.matrix=c(g),h.offset=g.offset();f&&(this._.transform=f);return this},E.rotate=function(a,b,e){if(this.removed)return this;if(a!=null){a=c(a).split(k),a.length-1&&(b=d(a[1]),e=d(a[2])),a=d(a[0]),e==null&&(b=e);if(b==null||e==null){var f=this.getBBox(1);b=f.x+f.width/2,e=f.y+f.height/2}this._.dirtyT=1,this.transform(this._.transform.concat([["r",a,b,e]]));return this}},E.translate=function(a,b){if(this.removed)return this;a=c(a).split(k),a.length-1&&(b=d(a[1])),a=d(a[0])||0,b=+b||0,this._.bbox&&(this._.bbox.x+=a,this._.bbox.y+=b),this.transform(this._.transform.concat([["t",a,b]]));return this},E.scale=function(a,b,e,f){if(this.removed)return this;a=c(a).split(k),a.length-1&&(b=d(a[1]),e=d(a[2]),f=d(a[3]),isNaN(e)&&(e=null),isNaN(f)&&(f=null)),a=d(a[0]),b==null&&(b=a),f==null&&(e=f);if(e==null||f==null)var g=this.getBBox(1);e=e==null?g.x+g.width/2:e,f=f==null?g.y+g.height/2:f,this.transform(this._.transform.concat([["s",a,b,e,f]])),this._.dirtyT=1;return this},E.hide=function(){!this.removed&&(this.node.style.display="none");return this},E.show=function(){!this.removed&&(this.node.style.display=o);return this},E._getBBox=function(){if(this.removed)return{};return{x:this.X+(this.bbx||0)-this.W/2,y:this.Y-this.H,width:this.W,height:this.H}},E.remove=function(){if(!this.removed&&!!this.node.parentNode){this.paper.__set__&&this.paper.__set__.exclude(this),a.eve.unbind("raphael.*.*."+this.id),a._tear(this,this.paper),this.node.parentNode.removeChild(this.node),this.shape&&this.shape.parentNode.removeChild(this.shape);for(var b in this)this[b]=typeof this[b]=="function"?a._removedFactory(b):null;this.removed=!0}},E.attr=function(c,d){if(this.removed)return this;if(c==null){var e={};for(var f in this.attrs)this.attrs[b](f)&&(e[f]=this.attrs[f]);e.gradient&&e.fill=="none"&&(e.fill=e.gradient)&&delete e.gradient,e.transform=this._.transform;return e}if(d==null&&a.is(c,"string")){if(c==j&&this.attrs.fill=="none"&&this.attrs.gradient)return this.attrs.gradient;var g=c.split(k),h={};for(var i=0,m=g.length;i<m;i++)c=g[i],c in this.attrs?h[c]=this.attrs[c]:a.is(this.paper.customAttributes[c],"function")?h[c]=this.paper.customAttributes[c].def:h[c]=a._availableAttrs[c];return m-1?h:h[g[0]]}if(this.attrs&&d==null&&a.is(c,"array")){h={};for(i=0,m=c.length;i<m;i++)h[c[i]]=this.attr(c[i]);return h}var n;d!=null&&(n={},n[c]=d),d==null&&a.is(c,"object")&&(n=c);for(var o in n)l("raphael.attr."+o+"."+this.id,this,n[o]);if(n){for(o in this.paper.customAttributes)if(this.paper.customAttributes[b](o)&&n[b](o)&&a.is(this.paper.customAttributes[o],"function")){var p=this.paper.customAttributes[o].apply(this,[].concat(n[o]));this.attrs[o]=n[o];for(var q in p)p[b](q)&&(n[q]=p[q])}n.text&&this.type=="text"&&(this.textpath.string=n.text),B(this,n)}return this},E.toFront=function(){!this.removed&&this.node.parentNode.appendChild(this.node),this.paper&&this.paper.top!=this&&a._tofront(this,this.paper);return this},E.toBack=function(){if(this.removed)return this;this.node.parentNode.firstChild!=this.node&&(this.node.parentNode.insertBefore(this.node,this.node.parentNode.firstChild),a._toback(this,this.paper));return this},E.insertAfter=function(b){if(this.removed)return this;b.constructor==a.st.constructor&&(b=b[b.length-1]),b.node.nextSibling?b.node.parentNode.insertBefore(this.node,b.node.nextSibling):b.node.parentNode.appendChild(this.node),a._insertafter(this,b,this.paper);return this},E.insertBefore=function(b){if(this.removed)return this;b.constructor==a.st.constructor&&(b=b[0]),b.node.parentNode.insertBefore(this.node,b.node),a._insertbefore(this,b,this.paper);return this},E.blur=function(b){var c=this.node.runtimeStyle,d=c.filter;d=d.replace(r,o),+b!==0?(this.attrs.blur=b,c.filter=d+n+m+".Blur(pixelradius="+(+b||1.5)+")",c.margin=a.format("-{0}px 0 0 -{0}px",f(+b||1.5))):(c.filter=d,c.margin=0,delete this.attrs.blur)},a._engine.path=function(a,b){var c=F("shape");c.style.cssText=t,c.coordsize=u+n+u,c.coordorigin=b.coordorigin;var d=new D(c,b),e={fill:"none",stroke:"#000"};a&&(e.path=a),d.type="path",d.path=[],d.Path=o,B(d,e),b.canvas.appendChild(c);var f=F("skew");f.on=!0,c.appendChild(f),d.skew=f,d.transform(o);return d},a._engine.rect=function(b,c,d,e,f,g){var h=a._rectPath(c,d,e,f,g),i=b.path(h),j=i.attrs;i.X=j.x=c,i.Y=j.y=d,i.W=j.width=e,i.H=j.height=f,j.r=g,j.path=h,i.type="rect";return i},a._engine.ellipse=function(a,b,c,d,e){var f=a.path(),g=f.attrs;f.X=b-d,f.Y=c-e,f.W=d*2,f.H=e*2,f.type="ellipse",B(f,{cx:b,cy:c,rx:d,ry:e});return f},a._engine.circle=function(a,b,c,d){var e=a.path(),f=e.attrs;e.X=b-d,e.Y=c-d,e.W=e.H=d*2,e.type="circle",B(e,{cx:b,cy:c,r:d});return e},a._engine.image=function(b,c,d,e,f,g){var h=a._rectPath(d,e,f,g),i=b.path(h).attr({stroke:"none"}),k=i.attrs,l=i.node,m=l.getElementsByTagName(j)[0];k.src=c,i.X=k.x=d,i.Y=k.y=e,i.W=k.width=f,i.H=k.height=g,k.path=h,i.type="image",m.parentNode==l&&l.removeChild(m),m.rotate=!0,m.src=c,m.type="tile",i._.fillpos=[d,e],i._.fillsize=[f,g],l.appendChild(m),z(i,1,1,0,0,0);return i},a._engine.text=function(b,d,e,g){var h=F("shape"),i=F("path"),j=F("textpath");d=d||0,e=e||0,g=g||"",i.v=a.format("m{0},{1}l{2},{1}",f(d*u),f(e*u),f(d*u)+1),i.textpathok=!0,j.string=c(g),j.on=!0,h.style.cssText=t,h.coordsize=u+n+u,h.coordorigin="0 0";var k=new D(h,b),l={fill:"#000",stroke:"none",font:a._availableAttrs.font,text:g};k.shape=h,k.path=i,k.textpath=j,k.type="text",k.attrs.text=c(g),k.attrs.x=d,k.attrs.y=e,k.attrs.w=1,k.attrs.h=1,B(k,l),h.appendChild(j),h.appendChild(i),b.canvas.appendChild(h);var m=F("skew");m.on=!0,h.appendChild(m),k.skew=m,k.transform(o);return k},a._engine.setSize=function(b,c){var d=this.canvas.style;this.width=b,this.height=c,b==+b&&(b+="px"),c==+c&&(c+="px"),d.width=b,d.height=c,d.clip="rect(0 "+b+" "+c+" 0)",this._viewBox&&a._engine.setViewBox.apply(this,this._viewBox);return this},a._engine.setViewBox=function(b,c,d,e,f){a.eve("raphael.setViewBox",this,this._viewBox,[b,c,d,e,f]);var h=this.width,i=this.height,j=1/g(d/h,e/i),k,l;f&&(k=i/e,l=h/d,d*k<h&&(b-=(h-d*k)/2/k),e*l<i&&(c-=(i-e*l)/2/l)),this._viewBox=[b,c,d,e,!!f],this._viewBoxShift={dx:-b,dy:-c,scale:j},this.forEach(function(a){a.transform("...")});return this};var F;a._engine.initWin=function(a){var b=a.document;b.createStyleSheet().addRule(".rvml","behavior:url(#default#VML)");try{!b.namespaces.rvml&&b.namespaces.add("rvml","urn:schemas-microsoft-com:vml"),F=function(a){return b.createElement("<rvml:"+a+' class="rvml">')}}catch(c){F=function(a){return b.createElement("<"+a+' xmlns="urn:schemas-microsoft.com:vml" class="rvml">')}}},a._engine.initWin(a._g.win),a._engine.create=function(){var b=a._getContainer.apply(0,arguments),c=b.container,d=b.height,e,f=b.width,g=b.x,h=b.y;if(!c)throw new Error("VML container not found.");var i=new a._Paper,j=i.canvas=a._g.doc.createElement("div"),k=j.style;g=g||0,h=h||0,f=f||512,d=d||342,i.width=f,i.height=d,f==+f&&(f+="px"),d==+d&&(d+="px"),i.coordsize=u*1e3+n+u*1e3,i.coordorigin="0 0",i.span=a._g.doc.createElement("span"),i.span.style.cssText="position:absolute;left:-9999em;top:-9999em;padding:0;margin:0;line-height:1;",j.appendChild(i.span),k.cssText=a.format("top:0;left:0;width:{0};height:{1};display:inline-block;position:relative;clip:rect(0 {0} {1} 0);overflow:hidden",f,d),c==1?(a._g.doc.body.appendChild(j),k.left=g+"px",k.top=h+"px",k.position="absolute"):c.firstChild?c.insertBefore(j,c.firstChild):c.appendChild(j),i.renderfix=function(){};return i},a.prototype.clear=function(){a.eve("raphael.clear",this),this.canvas.innerHTML=o,this.span=a._g.doc.createElement("span"),this.span.style.cssText="position:absolute;left:-9999em;top:-9999em;padding:0;margin:0;line-height:1;display:inline;",this.canvas.appendChild(this.span),this.bottom=this.top=null},a.prototype.remove=function(){a.eve("raphael.remove",this),this.canvas.parentNode.removeChild(this.canvas);for(var b in this)this[b]=typeof this[b]=="function"?a._removedFactory(b):null;return!0};var G=a.st;for(var H in E)E[b](H)&&!G[b](H)&&(G[H]=function(a){return function(){var b=arguments;return this.forEach(function(c){c[a].apply(c,b)})}}(H))}(window.Raphael)
;
window.polyjs=function(X){if(!X){var c={};(function(){var n=[].indexOf||function(c){for(var l=0,d=this.length;l<d;l++)if(l in this&&this[l]===c)return l;return-1};c.groupBy=function(n,l){return _.groupBy(n,c.stringify(l))};c.stringify=function(c){return function(l){return _.reduce(c,function(d,b){return""+d+b+":"+l[b]+";"},"")}};c.cross=function(n,l){var d,b,a,e,h,k,m,t,p,r;null==l&&(l=[]);a=_.difference(_.keys(n),l);if(0===a.length)return[{}];d=[];e=a[0];a=c.cross(n,l.concat(e));r=n[e];k=0;for(t=
r.length;k<t;k++)for(h=r[k],m=0,p=a.length;m<p;m++)b=a[m],b=_.clone(b),b[e]=h,d.push(b);return d};c.filter=function(c,l,d){var b,a,e,h;a=[];e=0;for(h=c.length;e<h;e++)b=c[e],b[l]===d&&a.push(b);return a};c.intersect=function(c,l){var d,b,a,e,h;b=function(a){var b,e,p,r,f;e=[];f=c[a]["in"];p=0;for(r=f.length;p<r;p++)b=f[p],0<=n.call(l[a]["in"],b)&&e.push(b);return{"in":e}};d=function(a){var b,e,p,r,f;e=function(g){return g[a].lt?{type:"lt",val:g[a].lt}:g[a].le?{type:"le",val:g[a].le}:{type:null,val:null}};
b=function(g){return g[a].gt?{type:"gt",val:g[a].gt}:g[a].ge?{type:"ge",val:g[a].ge}:{type:null,val:null}};b=[b(c),b(l)];r=[e(c),e(l)];b.sort(function(g,f){return f.val-g.val});r.sort(function(f,a){return f.val-a.val});e={};b[0].type&&b[0].val&&(f=b[0],p=f.type,f=f.val,b[0].val===b[1].val&&b[0].type!==b[1].type&&(p="lt"),e[p]=f);r[0].type&&r[0].val&&(f=r[0],p=f.type,f=f.val,r[0].val===r[1].val&&r[0].type!==r[1].type&&(p="lt"),e[p]=f);if(b[0].type&&r[0].type&&(b[0].val>r[0].val||b[0].val===r[0].val&&
("lt"===b[0].key||"gt"===r[0].key)))throw"No intersection found!";return e};e={};for(a in c)h=c[a],e[a]=a in l?"in"in c[a]?b(a):d(a):h;for(a in l)h=l[a],a in e||(e[a]=h);return e};c.linear=function(n,l,d,b){if(_.isFinite(n)&&_.isFinite(l)&&_.isFinite(d)&&_.isFinite(b))return function(a){return(b-l)/(d-n)*(a-n)+l};throw c.error.input("Attempting to create linear function from infinity");};c.median=function(c,l){var d;null==l&&(l=!1);l||(c=_.sortBy(c,function(b){return b}));d=c.length/2;return 0!==
d%1?c[Math.floor(d)]:(c[d-1]+c[d])/2};c.counter=function(){var c;c=0;return function(){return c++}};c.sample=function(c,l){return _.pick(c,_.shuffle(_.keys(c)).splice(0,l))};c.compare=function(c,l){var d,b,a,e,h,k,m,t,p;p=_.sortBy(c,function(a){return a});t=_.sortBy(l,function(a){return a});b=[];a=[];d=[];for(m=h=0;m<p.length||h<t.length;)if(k=p[m],e=t[h],m>=p.length)d.push(e),h+=1;else if(h>=t.length)b.push(k),m+=1;else if(k<e)b.push(k),m+=1;else if(k>e)d.push(e),h+=1;else if(k===e)a.push(k),m+=
1,h+=1;else throw DataError("Unknown data encounted");return{deleted:b,kept:a,added:d}};c.flatten=function(n){var l,d,b,a;l=[];if(null!=n)if(_.isObject(n))if("scalefn"===n.t)"novalue"!==n.f&&l.push(n.v);else for(d in n)b=n[d],l=l.concat(c.flatten(b));else if(_.isArray(n))for(d=0,a=n.length;d<a;d++)b=n[d],l=l.concat(c.flatten(b));else l.push(n);return l};c.getLabel=function(c,l){return _.chain(c).map(function(c){return c.mapping[l]}).without(null,void 0).uniq().value().join(" | ")};c.strSize=function(c){c=
(c+"").length;return 10>c?6*c:5*(c-10)+60};c.sortArrays=function(c,l){var d;d=_.zip.apply(_,l);d.sort(function(b,a){return c(b[0],a[0])});return _.zip.apply(_,d)};c.isDefined=function(n){return _.isObject(n)?"scalefn"===n.t&&"novalue"!==n.f?c.isDefined(n.v):!0:void 0!==n&&null!==n&&!(_.isNumber(n)&&_.isNaN(n))};c.isURI=function(c){var l;return _.isString(c)?(l=RegExp("^(https?:\\/\\/)?((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|((\\d{1,3}\\.){3}\\d{1,3}))(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*(\\?[;&a-z\\d%_.~+=-]*)?(\\#[-a-z\\d_]*)?$",
"i"),l.test(c)):!1}}).call(this);(function(){c["const"]={aes:"x y color size opacity shape id text".split(" "),pivot_aes:["row","column","value"],noDomain:["id","text","tooltip"],noLegend:["x","y","id","text","tooltip"],trans:{bin:["key","binwidth"],lag:["key","lag"]},stat:{count:["key"],unique:["key"],sum:["key"],mean:["key"],box:["key"],median:["key"]},timerange:"second minute hour day week month twomonth quarter sixmonth year twoyear fiveyear decade".split(" "),approxTimeInSeconds:{second:1,minute:60,
hour:3600,day:86400,week:604800,month:2592E3,twomonth:5184E3,quarter:10368E3,sixmonth:15552E3,year:31536E3,twoyear:63072E3,fiveyear:157766400},sort:{key:null,sort:null,limit:null,asc:!1},scaleFns:{novalue:function(){return{v:null,f:"novalue",t:"scalefn"}},max:function(c){return{v:c,f:"max",t:"scalefn"}},min:function(c){return{v:c,f:"min",t:"scalefn"}},upper:function(c,s,l){return{v:c,n:s,m:l,f:"upper",t:"scalefn"}},lower:function(c,s,l){return{v:c,n:s,m:l,f:"lower",t:"scalefn"}},middle:function(c){return{v:c,
f:"middle",t:"scalefn"}},jitter:function(c){return{v:c,f:"jitter",t:"scalefn"}},identity:function(c){return{v:c,f:"identity",t:"scalefn"}}},epsilon:Math.pow(10,-7),defaults:{x:{v:null,f:"novalue",t:"scalefn"},y:{v:null,f:"novalue",t:"scalefn"},color:"steelblue",size:2,opacity:0.7}}}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m={}.hasOwnProperty,t=function(a,b){function f(){this.constructor=a}for(var g in b)m.call(b,g)&&(a[g]=b[g]);f.prototype=b.prototype;a.prototype=new f;a.__super__=b.prototype;
return a};s=function(a){function b(f){this.message=f;this.name="DefinitionError"}t(b,a);return b}(Error);l=function(a){function b(f){this.message=f;this.name="DependencyError"}t(b,a);return b}(Error);b=function(a){function b(f){this.message=f;this.name="ModeError"}t(b,a);return b}(Error);n=function(a){function b(f){this.message=f;this.name="DataError"}t(b,a);return b}(Error);k=function(a){function b(f){this.message=f;this.name="UnknownInput"}t(b,a);return b}(Error);a=function(a){function b(f){this.message=
f;this.name="ModeError"}t(b,a);return b}(Error);e=function(a){function b(f){this.message=f;this.name="ScaleError"}t(b,a);return b}(Error);d=function(a){function b(f){this.message=f;this.name="MissingData"}t(b,a);return b}(Error);h=function(a){function b(f){this.message=f;this.name="Type"}t(b,a);return b}(Error);c.error=function(a){return Error(a)};c.error.data=function(a){return new n(a)};c.error.depn=function(a){return new l(a)};c.error.defn=function(a){return new s(a)};c.error.mode=function(a){return new b(a)};
c.error.impl=function(b){return new a(b)};c.error.input=function(a){return new k(a)};c.error.scale=function(a){return new e(a)};c.error.missing=function(a){return new d(a)};c.error.type=function(a){return new h(a)}}).call(this);(function(){var n,s,l,d,b,a,e={}.hasOwnProperty,h=function(a,b){function c(){this.constructor=a}for(var d in b)e.call(b,d)&&(a[d]=b[d]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a},k=function(a,b){return function(){return a.apply(b,arguments)}};
d=function(){function a(){}a.prototype.render=function(){return c.error.impl()};a.prototype.dispose=function(){return c.error.impl()};return a}();s=function(a){function e(){return b=e.__super__.constructor.apply(this,arguments)}h(e,a);e.prototype.getDimension=function(){throw c.error.impl();};return e}(d);l=function(b){function e(){return a=e.__super__.constructor.apply(this,arguments)}h(e,b);e.prototype.getDimension=function(){throw c.error.impl();};e.prototype.make=function(){throw c.error.impl();
};return e}(d);n=function(a){function b(a){this.type=null!=a?a:null;this.dispose=k(this.dispose,this);this.geoms={};this.pts={}}h(b,a);b.prototype.set=function(a){return this.geoms=a};b.prototype.render=function(a){var b,f,g,q,e,v,d;e={};g=c.compare(_.keys(this.pts),_.keys(this.geoms));f=g.deleted;q=g.kept;b=g.added;v=0;for(d=f.length;v<d;v++)g=f[v],this._delete(a,this.pts[g]);f=0;for(v=b.length;f<v;f++)g=b[f],e[g]=this._add(a,this.geoms[g]);b=0;for(f=q.length;b<f;b++)g=q[b],e[g]=this._modify(a,this.pts[g],
this.geoms[g]);return this.pts=e};b.prototype._delete=function(a,b){var f,g,q;q=[];for(f in b)g=b[f],q.push(a.remove(g));return q};b.prototype._modify=function(a,b,f){var g,q,e,c;e={};c=f.marks;for(q in c){g=c[q];try{e[q]=b[q]?b[q].data("m").type===g.type?a.animate(b[q],g,f.evtData,f.tooltip):(a.remove(b[q]),a.add(g,f.evtData,f.tooltip,this.type)):a.add(g,f.evtData,f.tooltip,this.type)}catch(d){if(g=d,"MissingData"===g.name)console.log(g.message);else throw g;}}return e};b.prototype._add=function(a,
b){var f,g,q,e;q={};e=b.marks;for(g in e){f=e[g];try{q[g]=a.add(f,b.evtData,b.tooltip,this.type)}catch(c){if(f=c,"MissingData"===f.name)console.log(f.message);else throw f;}}return q};b.prototype.dispose=function(a){var b,f,g;g=this.pts;for(b in g)f=g[b],this._delete(a,f);return this.pts={}};return b}(d);c.Renderable=d;c.Guide=s;c.GuideSet=l;c.Geometry=n}).call(this);(function(){var n,s,l=[].slice,d=[].indexOf||function(b){for(var a=0,e=this.length;a<e;a++)if(a in this&&this[a]===b)return a;return-1};
n=function(){function b(a,b,c){a.getContext?this.context=a.getContext("2d"):a.polyGeom=this;a.width=b;a.height=c;this.items=[];this._counter=0}b.prototype._makeItem=function(a,b){var c;c=new s(a,this._newId(),this,b);this.items.unshift(c);return c};b.prototype._newId=function(){return this._counter+=1};b.prototype.rect=function(){var a;a=1<=arguments.length?l.call(arguments,0):[];return this._makeItem("rect",a)};b.prototype.circle=function(){var a;a=1<=arguments.length?l.call(arguments,0):[];return this._makeItem("circle",
a)};b.prototype.path=function(){var a;a=1<=arguments.length?l.call(arguments,0):[];return this._makeItem("path",a)};b.prototype.text=function(){var a;a=1<=arguments.length?l.call(arguments,0):[];return this._makeItem("text",a)};b.prototype.remove=function(a){var b,c,d,m,t;t=this.items;b=d=0;for(m=t.length;d<m;b=++d)if(c=t[b],c.id===a)return this.items.splice(b,1)};b.prototype.toBack=function(a){var b;b=this.remove(a)[0];a=this.items.pop();this.items.push(b);return this.items.push(a)};b.prototype.toFront=
function(a){a=this.remove(a)[0];return this.items.unshift(a)};b.prototype._resetContext=function(){this.context.fillStyle="#000000";this.context.strokeStyle="#000000";this.context.globalAlpha=1;return this.context.lineWidth=0.5};b.prototype._stringToHex=function(a){switch(a){case "black":return"#000000";case "white":return"#ffffff";case "steelblue":return"#4692B4";default:return a}};return b}();s=function(){function b(a,b,c,d){this.type=a;this.id=b;this.canvas=c;this._attr={};this._interact={};this.attr(d)}
b.prototype.attr=function(){var a,b,d;a=1<=arguments.length?l.call(arguments,0):[];if(0<a.length&&_.isArray(a[0]))switch(b=a[0],this.type){case "rect":this._attr=_.extend(this._attr,{x:b[0],y:b[1],width:b[2],height:b[3]});break;case "circle":this._attr=_.extend(this._attr,{x:b[0],y:b[1],r:b[2]});break;case "path":this._attr=_.extend(this._attr,{path:b[0]});break;case "text":this._attr=_.extend(this._attr,{x:b[0],y:b[1],text:b[2],"font-size":"12pt","text-anchor":"middle"});break;default:throw c.error.defn("Unknown geometry type!");
}else if(1===a.length&&_.isObject(a[0]))for(b in d=a[0],d)a=d[b],this._attr[b]=a;else 2===a.length&&(null!=a[0]&&null!=a[1])&&(this._attr[a[0]]=a[1]);return this};b.prototype.remove=function(){return this.canvas.remove(this.id)};b.prototype.toBack=function(){return this.canvas.toBack(this.id)};b.prototype.toFront=function(){return this.canvas.toFront(this.id)};b.prototype.getBBox=function(){var a,b,c,k,m,t,p;if("text"===this.type){b=null!=(a=parseInt(this._attr["font-size"].slice(0,-2)))?a:12;k=0;
c=1.04*b;p=this._attr.text;m=0;for(t=p.length;m<t;m++)a=p[m],k=0<=d.call(",.1",a)?k+b/4:k+b;return{height:c,width:k}}if("rect"===this.type)return{height:this._attr.height,width:this._attr.width};if("circle"===this.type)return{height:this._attr.r,width:this._attr.r}};b.prototype.transform=function(a){if("s"===a[0]&&(a=a.slice(1),"font-size"in this._attr&&(this._attr["font-size"]=this._attr["font-size"].slice(0,-2)*a+"pt"),"width"in this._attr&&(this._attr.width*=a),"height"in this._attr))return this._attr.height*=
a};b.prototype.animate=function(){var a;a=1<=arguments.length?l.call(arguments,0):[];this._attr.animate=a;return this};b.prototype.click=function(a){return this._interact.click=a};b.prototype.drag=function(a,b,c){return this._interact.drag={onmove:a,onstart:b,onend:c}};b.prototype.hover=function(a){return this._interact.hover=a};b.prototype.data=function(a,b){var c;null==(c=this._interact).data&&(c.data={});return this._interact.data[a]=b};b.prototype.touchstart=function(a){return this._interact.touchstart=
a};b.prototype.touchend=function(a){return this._interact.touchend=a};b.prototype.touchmove=function(a){return this._interact.touchmove=a};b.prototype.touchcancel=function(a){return this._interact.touchcancel=a};return b}();c.canvas=function(b,a,c){return new n(b,a,c)}}).call(this);(function(){var n,s;c.offset=function(c){var d,b,a;d={top:0,left:0};if(b=c&&c.ownerDocument)return a=b.documentElement,"undefined"!==typeof c.getBoundingClientRect&&(d=c.getBoundingClientRect()),c=null!==b&&b===b.window?
b:9===b.nodeType&&b.defaultView,{top:d.top+c.pageYOffset-a.clientTop,left:d.left+c.pageXOffset-a.clientLeft}};c.getXY=function(c,d){var b,a;-1!==d.type.indexOf("mouse")?(a=d.clientX,b=d.clientY):-1!==d.type.indexOf("touch")&&(b=d.changedTouches[0],a=b.clientX,b=b.clientY);return{x:a+(document.documentElement&&document.documentElement.scrollLeft||document.body.scrollLeft)-c.left,y:b+(document.documentElement&&document.documentElement.scrollTop||document.body.scrollTop)-c.top}};c.touchToMouse=function(c,
d,b){var a,e,h;null==b&&(b=!1);a=d.lastEvent;h=0<a.touches.length&&a.touches[0]||0<a.changedTouches.length&&a.changedTouches[0];e=document.createEvent("MouseEvent");e.initMouseEvent(c,a.bubbles,a.cancelable,a.view,a.detail,h.screenX,h.screenY,h.clientX,h.clientY,a.ctrlKey,a.altKey,a.shiftKey,a.metaKey,1,a.target);return b?(window.clearTimeout(d.pressTimer),d.pressTimer=window.setTimeout(function(){return a.target.dispatchEvent(e)},b)):a.target.dispatchEvent(e)};n={lastStart:0,lastTouch:0,lastEvent:null,
pressTimer:0};s=window.alert;c.touch=function(l,d,b,a){d.tooltip=d.data("t");d.evtData=d.data("e");n.lastEvent=b;b.preventDefault();if("touchstart"===l)return n.lastStart=b.timeStamp,c.touchToMouse("mousedown",n),n.pressTimer=window.setTimeout(function(){return c.touchToMouse("mouseover",n)},800),window.alert=function(){var a;window.clearTimeout(n.pressTimer);a=arguments;return window.setTimeout(function(){s.apply(window,a);return window.alert=s},100)};if("touchmove"===l){l=a.paper.getById(b.target.raphaelid);
a=c.offset(a.dom);a=c.getXY(a,b);if(600<b.timeStamp-n.lastStart&&l.isPointInside(a.x,a.y))return c.touchToMouse("mouseover",n);window.clearTimeout(n.pressTimer);return c.touchToMouse("mouseout",n)}if("touchend"===l){if(window.clearTimeout(n.pressTimer),c.touchToMouse("mouseup",n),c.touchToMouse("mouseout",n,400),800>b.timeStamp-n.lastStart)return c.touchToMouse("click",n)}else if("touchcancel"===l)return window.clearTimeout(n.pressTimer),c.touchToMouse("mouseout",n),c.touchToMouse("mouseup",n,300)}}).call(this);
(function(){var n,s,l;c.format=function(d,b){switch(d){case "cat":return c.format.identity;case "num":return c.format.number(b);case "date":return c.format.date(b);case "none":return c.format.identity}};c.format.identity=function(c){return c};n={0:"",3:"k",6:"m",9:"b",12:"t"};l=function(c,b){return _.isUndefined(n[b])?c+"e"+(0<b?"+":"-")+Math.abs(b):c+n[b]};s=function(c){var b,a,e;if(!isFinite(c))return c;a=""+c;b=Math.abs(c);1E4<=b&&(e=(""+b).split(/\./),b=e[0].length%3||3,e[0]=a.slice(0,b+(0>c))+
e[0].slice(b).replace(/(\d{3})/g,",$1"),a=e.join("."));return a};c.format.getExp=function(c){return Math.floor(Math.log(Math.abs(0===c?1:c))/Math.LN10)};c.format.number=function(d){return function(b){var a,e;e=0;a=null!=d?d:c.format.getExp(b);null==d||2!==a&&5!==a&&8!==a&&11!==a?-1===a?(a=0,e=null!=d?1:2):-2===a?(a=0,e=null!=d?2:3):1===a||2===a?a=0:3<a&&6>a?a=3:6<a&&9>a?a=6:9<a&&12>a?a=9:12<a&&15>a?a=12:e=null!=d?0:1:(a+=1,e=1);b=Math.round(b/Math.pow(10,a-e));b/=Math.pow(10,e);b=b.toFixed(e);return l(s(b),
a)}};c.format.date=function(d){return-1!==_.indexOf(c["const"].timerange,d)?"second"===d?function(b){return moment.unix(b).format("h:mm:ss a")}:"minute"===d?function(b){return moment.unix(b).format("h:mm a")}:"hour"===d?function(b){return moment.unix(b).format("MMM D h a")}:"day"===d||"week"===d?function(b){return moment.unix(b).format("MMM D")}:"month"===d||"twomonth"===d||"quarter"===d||"sixmonth"===d?function(b){return moment.unix(b).format("YYYY/MM")}:function(b){return moment.unix(b).format("YYYY")}:
function(b){return moment.unix(b).format(d)}};c.format._number_instance=c.format.number();c.format.value=function(d){return _.isNumber(d)?c.format._number_instance(d):d}}).call(this);(function(){var n,s;c.type={};c.type.impute=function(c){var d,b,a,e,h,k;h=b=e=d=0;for(k=c.length;h<k;h++)a=c[h],null!=a&&(b++,isNaN(a)&&isNaN(a.replace(/\$|\,/g,""))||e++,a=moment(a),null!=a&&a.isValid()&&d++);return e>0.95*b?"num":d>0.95*b?"date":"cat"};c.type.coerce=function(c,d){if(_.isUndefined(c)||_.isNull(c)||"cat"===
d.type)return c;if("num"===d.type)return isNaN(c)?+(""+c).replace(/\$|\,/g,""):+c;if("date"===d.type)return!_.isNumber(c)&&_.isEmpty(c)?null:d.format?"unix"===d.format?moment.unix(c).unix():moment(c,d.format).unix():isFinite(c)&&c>=Math.pow(10,9)?moment.unix(c).unix():moment(c).unix()};c.type.compare=function(c){switch(c){case "cat":return n;default:return s}};n=function(c,d){var b,a;if(c===d)return 0;_.isString(c)||(c=""+c);_.isString(d)||(d=""+d);b=c.toLowerCase();a=d.toLowerCase();return b===a?
c<d?-1:c>d?1:0:b<a?-1:b>a?1:0};s=function(c,d){return c===d?0:null===c?1:null===d?-1:c<d?-1:c>d?1:0}}).call(this);(function(){var n,s,l,d,b,a,e=function(a,b){return function(){return a.apply(b,arguments)}},h={}.hasOwnProperty,k=function(a,b){function c(){this.constructor=a}for(var e in b)h.call(b,e)&&(a[e]=b[e]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a};c.spec={};c.spec.toStrictMode=function(a){var b,e,d,f,g,q,u,v;a=_.clone(a);null==a.layers&&a.layer&&(a.layers=[a.layer]);
null==a.guides&&a.guide&&(a.guides=a.guide);null==a.guides&&(a.guides={});if(a.layers)for(q=a.layers,b=e=0,f=q.length;e<f;b=++e){d=q[b];v=c["const"].aes;g=0;for(u=v.length;g<u;g++)b=v[g],d[b]&&_.isString(d[b])&&(d[b]={"var":d[b]});null==d.sample&&(d.sample=500)}if(a.facet)for(d=["var","x","y"],q=0,b=d.length;q<b;q++)f=d[q],(e=a.facet[f])&&_.isString(e)&&(a.facet[f]={"var":e});else a.facet={type:"none"};a.coord||(a.coord={type:"cartesian",flip:!1});_.isString(a.dom)&&(a.dom=document.getElementById(a.dom));
return a};c.spec.check=function(a){var b,e,d,f,g;if(null==a.layers||0===a.layers.length)throw c.error.defn("No layers are defined in the specification.");g=a.layers;b=d=0;for(f=g.length;d<f;b=++d){e=g[b];if(null==e.data)throw c.error.defn("Layer "+(b+1)+" does not have data to plot!");if(!e.data.isData)throw c.error.defn("Data must be a Polychart Data object.");}if((null==a.render||!1!==a.render)&&!a.dom)throw c.error.defn("No DOM element specified. Where to make plot?");return a};s=function(){function a(){this["return"]=
e(this["return"],this);this.reset=e(this.reset,this);this.processGrouping=e(this.processGrouping,this);this.processMapping=e(this.processMapping,this);this.addSort=e(this.addSort,this);this.extractFilters=e(this.extractFilters,this);this.translate=e(this.translate,this)}a.prototype.translate=function(a,b){};a.prototype.extractFilters=function(a){var b,e,f,g,q;null==a&&(a={});q=[];for(f in a){e=a[f];g=_.clone(e);b=c.parser.getExpression(f);e=b.exprType;b=b.expr;g.expr=b;if("stat"===e)throw c.error.defn("Aggregate statistics in filters not allowed.");
"trans"===e&&this.trans.push(b);q.push(this.filters.push(g))}return q};a.prototype.addSort=function(a,b){var e,f,g,q,d;q=c.parser.getExpression(a.sort);(f=q.statInfo())?(g=f.fname,f=f.args):(g=null,f=[]);g={key:b,sort:q.expr,stat:g,args:f,limit:a.limit,asc:null!=(e=a.asc)?e:!1};q=0;for(d=f.length;q<d;q++)e=f[q],"ident"!==e.expr[0]&&this.trans.push(e);return this.sort.push(g)};a.prototype.processMapping=function(a){var b,e,f,g,q,d;b=c.parser.getExpression(a["var"]);g=b.exprType;f=b.expr;b=b.statInfo;
a["var"]=f.name;this.select.push(f);"trans"===g&&this.trans.push(f);if("stat"===g){b=b();g=b.fname;e=b.args;q=0;for(d=e.length;q<d;q++)b=e[q],"ident"!==b.expr[0]&&this.trans.push(b);this.stat.push({name:g,args:e,expr:f})}else this.groups.push(f);if("sort"in a)return this.addSort(a,f)};a.prototype.processGrouping=function(a){var b;b=c.parser.getExpression(a["var"]);a=b.exprType;b=b.expr;if("trans"===a)this.trans.push(b);else if("stat"===a)throw c.error.defn("Facet variable should not contain statistics!");
this.select.push(b);return this.groups.push(b)};a.prototype.reset=function(){this.filters=[];this.trans=[];this.stat=[];this.select=[];this.groups=[];return this.sort=[]};a.prototype["return"]=function(){var a;a=function(a,b){var f,g,c,e;null==b&&(b=function(a){return a.name});f={};c=0;for(e=a.length;c<e;c++)g=a[c],f[b(g)]=g;return _.values(f)};return{select:a(this.select),trans:a(this.trans),sort:this.sort,filter:this.filters,stats:{stats:a(this.stat,function(a){return a.expr.name}),groups:a(this.groups)}}};
return a}();n=function(a){function b(){this.pickAesthetics=e(this.pickAesthetics,this);this.translate=e(this.translate,this);return d=b.__super__.constructor.apply(this,arguments)}k(b,a);b.prototype.translate=function(a,b){var f,g,q;null==b&&(b=[]);this.reset();this.extractFilters(null!=(f=a.filter)?f:{});f=this.pickAesthetics(a,c["const"].aes);for(q in f)g=f[q],this.processMapping(g);f=0;for(g=b.length;f<g;f++)q=b[f],this.processGrouping(q);return this["return"]()};b.prototype.pickAesthetics=function(a,
b){var f,g;f=_.pick(a,b);for(g in f)"var"in f[g]||delete f[g];return f};return b}(s);l=function(a){function c(){this.pickAesthetics=e(this.pickAesthetics,this);this.translate=e(this.translate,this);return b=c.__super__.constructor.apply(this,arguments)}k(c,a);c.prototype.translate=function(a){var b,f,g;this.reset();this.extractFilters(null!=(b=a.filter)?b:{});a=this.pickAesthetics(a);f=0;for(g=a.length;f<g;f++)b=a[f],this.processMapping(b);return this["return"]()};c.prototype.pickAesthetics=function(a){var b,
f,g,c,e,d;a=_.pick(a,["columns","rows","values"]);b=[];for(g in a)for(c=a[g],e=0,d=c.length;e<d;e++)f=c[e],"var"in f&&b.push(f);return b};return c}(s);s=function(b){function c(){this.pickAesthetics=e(this.pickAesthetics,this);this.translate=e(this.translate,this);return a=c.__super__.constructor.apply(this,arguments)}k(c,b);c.prototype.translate=function(a){var b,f;this.reset();this.extractFilters(null!=(b=a.filter)?b:{});a=this.pickAesthetics(a);for(f in a)b=a[f],this.processMapping(b);return this["return"]()};
c.prototype.pickAesthetics=function(a){var b;a=_.pick(a,["value"]);for(b in a)"var"in a[b]||delete a[b];return a};return c}(s);n=new n;l=new l;s=new s;c.spec.layerToData=n.translate;c.spec.pivotToData=l.translate;c.spec.numeralToData=s.translate}).call(this);(function(){c.xhr=function(c,s,l){var d;d=new XMLHttpRequest;3>arguments.length?(l=s,s=null):s&&d.overrideMimeType&&d.overrideMimeType(s);d.open("GET",c,!0);s&&d.setRequestHeader("Accept",s);d.onreadystatechange=function(){var b;if(4===d.readyState)return b=
d.status,b=!b&&d.response||200<=b&&300>b||304===b?d:null,l(b)};return d.send(null)};c.text=function(n,s,l){3>arguments.length&&(l=s,s=null);return c.xhr(n,s,function(c){return l(c&&c.responseText)})};c.json=function(n,s){return c.text(n,"application/json",function(c){return s(c?JSON.parse(c):null)})};c.dsv=function(n,s){var l,d,b,a,e,h,k;k=RegExp("\r\n|["+n+"\r\n]","g");h=RegExp('["'+n+"\n]");l=n.charCodeAt(0);b=function(b){return b.map(a).join(n)};a=function(a){var b;return null!=(b=h.test(a))?b:
'"'+a.replace(/\"/g,'""')+{'"':a}};e=null;d=function(a,b){return c.text(a,s,function(a){return b(a&&d.parse(a))})};d.parse=function(a){return d.parseRows(a,function(a,b){var c,f,g;if(b){g={};c=-1;for(f=e.length;++c<f;)g[e[c]]=a[c];return g}e=a;return null})};d.parseRows=function(a,b){var c,e,f,g,q,d,v,h;e={};c={};d=[];q=0;g=v=null;k.lastIndex=0;for(h=function(){var b,f,q;if(k.lastIndex>=a.length)return c;if(g)return g=!1,e;q=k.lastIndex;if(34===a.charCodeAt(q)){for(f=q;f++<a.length;)if(34===a.charCodeAt(f)){if(34!==
a.charCodeAt(f+1))break;f++}k.lastIndex=f+2;b=a.charCodeAt(f+1);13===b?(g=!0,10===a.charCodeAt(f+2)&&k.lastIndex++):10===b&&(g=!0);return a.substring(q+1,f).replace(/""/g,'"')}if(b=k.exec(a))return g=b[0].charCodeAt(0)!==l,a.substring(q,b.index);k.lastIndex=a.length;return a.substring(q)};(v=h())!==c;){for(f=[];v!==e&&v!==c;)f.push(v),v=h();b&&!(f=b(f,q++))||d.push(f)}return d};d.format=function(a){return a.map(b).join("\n")};return d};c.csv=c.dsv(",","text/csv")}).call(this);(function(){var n,s,
l,d,b,a,e,h,k,m,t,p,r,f,g,q,u,v,D,C,z,J,G,B,F,x,H,I,P,R,S,A,da,ea,Y,K,Q,fa,ga,U,Z,ha,V,E,L,ia,T,y,aa,ba,ja,W,ka,M,N,X,ca,w=function(a,b){return function(){return a.apply(b,arguments)}},ma={}.hasOwnProperty,O=function(a,b){function f(){this.constructor=a}for(var g in b)ma.call(b,g)&&(a[g]=b[g]);f.prototype=b.prototype;a.prototype=new f;a.__super__=b.prototype;return a},na=[].slice,la=[].indexOf||function(a){for(var b=0,f=this.length;b<f;b++)if(b in this&&this[b]===a)return b;return-1};x=function(a){return a.replace(/[\[\]\\]/g,
function(a){return"\\"+a})};W=function(a){return a.replace(/\\./g,function(a){return a.slice(1)})};F=function(a){return"["+x(a)+"]"};ja=function(a){var b;b=a.length;"["===a[0]&&"]"===a[b-1]&&(a=a.slice(1,+(b-2)+1||9E9),a=W(a));return a};fa=function(a){return'"'+a.replace(/["\\]/g,function(a){return"\\"+a})+'"'};ka=function(a){var b,f,g,c,q;b=a.length;q=['"',"'"];g=0;for(c=q.length;g<c;g++)if(f=q[g],a[0]===f&&a[b-1]===f){a=a.slice(1,+(b-2)+1||9E9);a=W(a);break}return a};U=function(a,b){return""+a+
"("+b+")"};Z=function(a){return"["+a+"]"};e=function(){return function(a){this.message=a}}();a=function(){function a(b){this.name=b;this._unify=w(this._unify,this);this._runify=w(this._runify,this);this._known_unify=w(this._known_unify,this);this.unify=w(this.unify,this);this.mismatch=w(this.mismatch,this);this.error=w(this.error,this)}a.prototype.error=function(a,b){var f,g,c,q,d;d=[];c=0;for(q=a.length;c<q;c++)g=a[c],f=g[0],g=g[1],d.push("("+f+" vs. "+g+")");d.reverse();f=d.join(" in ");throw new e(b+
": "+f);};a.prototype.mismatch=function(a){return this.error(a,"Type mismatch")};a.prototype.unify=function(a){return a._known_unify(this)};a.prototype._known_unify=function(a){this._runify([],a);return this};a.prototype._runify=function(a,b){return this._unify(a.concat([[this.toString(),b.toString()]]),b)};a.prototype._unify=function(a,b){if(this.name!==b.name)return this.mismatch(a)};return a}();J=function(a){function b(){this._unify=w(this._unify,this);this.unify=w(this.unify,this);this.toString=
w(this.toString,this);b.__super__.constructor.call(this,"?");this.found=null}O(b,a);b.prototype.toString=function(){return null===this.found?"?":this.found.toString()};b.prototype.unify=function(a){return this._known_unify(a)};b.prototype._unify=function(a,b){return null===this.found?this.found=b:this.found._unify(a,b)};return b}(a);n=function(a){function b(){this.toString=w(this.toString,this);return X=b.__super__.constructor.apply(this,arguments)}O(b,a);b.prototype.toString=function(){return""+
this.name};return b}(a);k=function(a){function b(a,f){this.domains=a;this.range=f;this._unify=w(this._unify,this);this.toString=w(this.toString,this);b.__super__.constructor.call(this,"->")}O(b,a);b.prototype.toString=function(){var a,b,f,g,c;g=this.domains;c=[];b=0;for(f=g.length;b<f;b++)a=g[b],c.push(a.toString());return"(["+c.join(", ")+"] -> "+this.range+")"};b.prototype._unify=function(a,f){var g,c,q,e,d;b.__super__._unify.call(this,a,f);this.domains.length!==f.domains.length&&this.error(a,"function domains differ in length");
d=_.zip(this.domains,f.domains);q=0;for(e=d.length;q<e;q++)c=d[q],g=c[0],c=c[1],g._runify(a,c);return this.range._runify(a,f.range)};return b}(a);a.Base=_.object(function(){var a,b;a={cat:"cat",num:"num",date:"date",stat:"stat"};b=[];for(Y in a)ga=a[Y],b.push([Y,new n(ga)]);return b}());D=function(){function a(b){this.toString=w(this.toString,this);this.get=w(this.get,this);this.peek=w(this.peek,this);this.empty=w(this.empty,this);var f,g,c,q;q=[];g=0;for(c=b.length;g<c;g++)f=b[g],q.push(f);this.buffer=
q.reverse()}a.prototype.empty=function(){return 0===this.buffer.length};a.prototype.peek=function(){return this.empty()?null:this.buffer[this.buffer.length-1]};a.prototype.get=function(){return this.empty()?null:this.buffer.pop()};a.prototype.toString=function(){return U("Stream",Z(na.call(this.buffer).reverse()))};return a}();z=function(){function a(b){this.tag=b;this.contents=w(this.contents,this);this.toString=w(this.toString,this)}a.Tag={symbol:"symbol",literal:"literal",infixsymbol:"infixsymbol",
keyword:"keyword",lparen:"(",rparen:")",comma:","};a.prototype.toString=function(){return"<"+this.contents().toString()+">"};a.prototype.contents=function(){return[this.tag]};return a}();C=function(a){function b(a){this.name=a;this.contents=w(this.contents,this);this.name=ja(this.name);b.__super__.constructor.call(this,z.Tag.symbol)}O(b,a);b.prototype.contents=function(){return b.__super__.contents.call(this).concat([this.name])};return b}(z);g=function(b){function f(b,g){this.val=b;this.type=g;this.contents=
w(this.contents,this);f.__super__.constructor.call(this,z.Tag.literal);this.type===a.Base.cat&&(this.val=ka(this.val))}O(f,b);f.prototype.contents=function(){return f.__super__.contents.call(this).concat([this.val])};return f}(z);p=function(a){function b(a){this.op=a;this.contents=w(this.contents,this);b.__super__.constructor.call(this,z.Tag.infixsymbol)}O(b,a);b.prototype.contents=function(){return b.__super__.contents.call(this).concat([this.op])};return b}(z);r=function(a){function b(a){this.name=
a;this.contents=w(this.contents,this);b.__super__.constructor.call(this,z.Tag.keyword)}O(b,a);b.prototype.contents=function(){return b.__super__.contents.call(this).concat([this.name])};return b}(z);h=function(){var a,b,f,g;f=[z.Tag.lparen,z.Tag.rparen,z.Tag.comma];g=[];a=0;for(b=f.length;a<b;a++)V=f[a],g.push(new z(V));return g}();f=h[0];v=h[1];l=h[2];S="++ * / % + - >= > <= < != ==".split(" ");R=function(a,b){return S.indexOf(a)<=S.indexOf(b)};h=function(){var a,b,f;f=[];a=0;for(b=S.length;a<b;a++)ha=
S[a],f.push(ha.replace(/[+*]/g,function(a){return"(\\"+a+")"}));return f}();h=RegExp("^("+h.join("|")+")");da=["if","then","else"];ba=[[/^\(/,function(){return f}],[/^\)/,function(){return v}],[/^,/,function(){return l}],[/^[+-]?(0x[0-9a-fA-F]+|0?\.\d+|[1-9]\d*(\.\d+)?|0)([eE][+-]?\d+)?/,function(b){return new g(b,a.Base.num)}],[/^(([\w|\.]|[^\u0000-\u0080])+|\[((\\.)|[^\\\[\]])+\])/,function(a){return 0<=la.call(da,a)?new r(a):new C(a)}],[/^('((\\.)|[^\\'])*'|"((\\.)|[^\\"])+")/,function(b){return new g(b,
a.Base.cat)}],[h,function(a){return new p(a)}]];ea=function(a){var b,f,g,q;g=0;for(q=ba.length;g<q;g++)if(f=ba[g],b=f[0],f=f[1],b=b.exec(a))return g=b[0],[a.slice(g.length),f(g)];throw c.error.defn("There is an error in your specification at "+a);};aa=function(a){var b,f;for(f=[];;){a=a.replace(/^\s+/,"");if(!a)break;b=ea(a);a=b[0];b=b[1];f.push(b)}return f};h=function(){function a(){}a.prototype.toString=function(){return U(this.constructor.name,this.contents())};return a}();m=function(a){function b(a){this.name=
a;this.visit=w(this.visit,this);this.pretty=w(this.pretty,this);this.contents=w(this.contents,this)}O(b,a);b.prototype.contents=function(){return[this.name]};b.prototype.pretty=function(){return F(this.name)};b.prototype.visit=function(a){return a.ident(this,this.name)};return b}(h);b=function(b){function f(a,b){this.val=a;this.vtype=b;this.visit=w(this.visit,this);this.pretty=w(this.pretty,this);this.contents=w(this.contents,this)}O(f,b);f.prototype.contents=function(){return[this.val]};f.prototype.pretty=
function(){return this.vtype===a.Base.cat?fa(this.val):this.val};f.prototype.visit=function(a){return a["const"](this,this.val,this.vtype)};return f}(h);s=function(a){function b(a,f){this.fname=a;this.args=f;this.visit=w(this.visit,this);this.pretty=w(this.pretty,this);this.contents=w(this.contents,this)}O(b,a);b.prototype.contents=function(){return[this.fname,Z(this.args)]};b.prototype.pretty=function(){var a,b=this.fname,f,g,c,q;c=this.args;q=[];f=0;for(g=c.length;f<g;f++)a=c[f],q.push(a.pretty());
return U(b,q)};b.prototype.visit=function(a){var b;return a.call(this,this.fname,function(){var f,g,c,q;c=this.args;q=[];f=0;for(g=c.length;f<g;f++)b=c[f],q.push(b.visit(a));return q}.call(this))};return b}(h);t=function(a){function b(a,f,g){this.opsym=a;this.lhs=f;this.rhs=g;this.visit=w(this.visit,this);this.pretty=w(this.pretty,this);this.contents=w(this.contents,this)}O(b,a);b.prototype.contents=function(){return[this.lhs,this.opsym,this.rhs]};b.prototype.pretty=function(){return"("+[this.lhs.pretty(),
this.opsym,this.rhs.pretty()].join(" ")+")"};b.prototype.visit=function(a){return a.infixop(this,this.opsym,this.lhs.visit(a),this.rhs.visit(a))};return b}(h);d=function(a){function b(a,f,g){this.condition=a;this.consequent=f;this.alternative=g;this.visit=w(this.visit,this);this.pretty=w(this.pretty,this);this.contents=w(this.contents,this)}O(b,a);b.prototype.contents=function(){return[this.condition,this.consequent,this.alternative]};b.prototype.pretty=function(){return"(if "+this.condition.pretty()+
" "+("then "+this.consequent.pretty()+" else "+this.alternative.pretty()+")")};b.prototype.visit=function(a){return a.conditional(this,this.condition.visit(a),this.consequent.visit(a),this.alternative.visit(a))};return b}(h);q=function(){function a(){this.finish=w(this.finish,this);this.push=w(this.push,this);this._reduce=w(this._reduce,this);this.ops=[]}a.prototype._reduce=function(a,b){for(var f,g;0!==this.ops.length;)if(g=this.ops.pop(),f=g[0],g=g[1],b(g))a=new t(g,f,a);else{this.ops.push([f,g]);
break}return a};a.prototype.push=function(a,b){a=this._reduce(a,function(a){return R(a,b)});return this.ops.push([a,b])};a.prototype.finish=function(a){return this._reduce(a,function(a){return!0})};return a}();G=function(a,b){if(a!==b)throw c.error.defn("Expected "+b+" but received "+a);};B=function(a,b){return G(a.tag,b)};u=function(){function a(b){this.stream=b;this.parseFinish=w(this.parseFinish,this);this.parseInfix=w(this.parseInfix,this);this.parseCallArgs=w(this.parseCallArgs,this);this.parseCall=
w(this.parseCall,this);this.parseAtomCall=w(this.parseAtomCall,this);this.parseParenExpr=w(this.parseParenExpr,this);this.parseConditional=w(this.parseConditional,this);this.parseKeyword=w(this.parseKeyword,this);this.parseKeywordExpr=w(this.parseKeywordExpr,this);this.parseExpr=w(this.parseExpr,this);this.parseSubExpr=w(this.parseSubExpr,this);this.parseTopExpr=w(this.parseTopExpr,this);this.parseFail=w(this.parseFail,this);this.expect=w(this.expect,this);this.ops=new q}a.prototype.expect=function(a,
b){var f,g,c,q,e;g=this.stream.peek();if(null!==g)for(c=0,q=b.length;c<q;c++)if(f=b[c],V=f[0],f=f[1],e=g.tag,0<=la.call(V,e))return f();return a()};a.prototype.parseFail=function(){throw c.error.defn("There is an error in your specification at "+this.stream.toString());};a.prototype.parseTopExpr=function(){var a;a=this.parseExpr();null!==this.stream.peek()&&this.parseFail();return a};a.prototype.parseSubExpr=function(){return(new a(this.stream)).parseExpr()};a.prototype.parseExpr=function(){var a;
a=this.expect(this.parseFail,[[[z.Tag.lparen],this.parseParenExpr],[[z.Tag.keyword],this.parseKeywordExpr],[[z.Tag.literal,z.Tag.symbol],this.parseAtomCall]]);return this.expect(this.parseFinish(a),[[[z.Tag.infixsymbol],this.parseInfix(a)]])};a.prototype.parseKeywordExpr=function(){var a;a=this.stream.peek();B(a,z.Tag.keyword);switch(a.name){case "if":return this.parseConditional();default:return this.parseFail()}};a.prototype.parseKeyword=function(a){var b;b=this.stream.get();B(b,z.Tag.keyword);
return G(b.name,a)};a.prototype.parseConditional=function(){var a,b,f;this.parseKeyword("if");b=this.parseSubExpr();this.parseKeyword("then");f=this.parseSubExpr();this.parseKeyword("else");a=this.parseSubExpr();return new d(b,f,a)};a.prototype.parseParenExpr=function(){var a;G(this.stream.get(),f);a=this.parseSubExpr();G(this.stream.get(),v);return a};a.prototype.parseAtomCall=function(){var a,f;f=this.stream.get();a=f.tag===z.Tag.literal?new b(f.val,f.type):f.tag===z.Tag.symbol?new m(f.name):G(!1,
!0);return this.expect(function(){return a},[[[z.Tag.lparen],this.parseCall(f)]])};a.prototype.parseCall=function(a){var b=this;return function(g){var c;B(a,z.Tag.symbol);G(b.stream.get(),f);c=a.name;g=b.expect(b.parseCallArgs([]),[[[z.Tag.rparen],function(){b.stream.get();return[]}]]);return new s(c,g)}};a.prototype.parseCallArgs=function(a){var b=this;return function(){var f,g;f=b.parseSubExpr();g=a.concat([f]);return b.expect(b.parseFail,[[[z.Tag.rparen],function(){b.stream.get();return g}],[[z.Tag.comma],
function(){b.stream.get();return b.parseCallArgs(g)()}]])}};a.prototype.parseInfix=function(a){var b=this;return function(){var f;f=b.stream.get();B(f,z.Tag.infixsymbol);b.ops.push(a,f.op);return b.parseExpr()}};a.prototype.parseFinish=function(a){var b=this;return function(){return b.ops.finish(a)}};return a}();Q=function(a){a=new D(aa(a));return(new u(a)).parseTopExpr()};I=function(b,f,g){var q;q=function(a,f){var g,q;if(!(a in b))throw c.error.defn("Unknown function name: "+a);"++"===a&&2===f.length&&
(f[1]===y&&f[0]===E&&(a="++_num1"),f[0]===y&&f[1]===E&&(a="++_num2"));"bin"===a&&(2===f.length&&f[0]===L)&&(a="bin_date");"min"!==a&&"max"!==a||(1!==f.length||f[0]!==L)||(a+="_date");"count"!==a&&"unique"!==a&&"lag"!==a||1!==f.length||(f[0]===E?a+="_cat":f[0]===L&&(a+="_date"));"parseDate"===a&&1===f.length&&(a="parseDateDefault");g=b[a];q=new J;g.unify(new k(f,q));return q.found};return g.visit({ident:function(a,b){if(b in f)return f[b];throw c.error.defn("Unknown column name: "+b);},"const":function(a,
b,f){return f},call:function(a,b,f){return q(b,f)},infixop:function(a,b,f,g){return q(b,[f,g])},conditional:function(b,f,g,c){f.unify(a.Base.num);g.unify(c);return g}})};E=a.Base.cat;y=a.Base.num;L=a.Base.date;K=new k([y,y],y);A={"++":new k([E,E],E),"++_num1":new k([E,y],E),"++_num2":new k([y,E],E)};ca="* / % + - >= > <= < != == =".split(" ");M=0;for(N=ca.length;M<N;M++)h=ca[M],A[h]=K;N=["sum","mean","box","median"];K=0;for(M=N.length;K<M;K++)h=N[K],A[h]=new k([y],a.Base.stat);N=["min","max"];K=0;
for(M=N.length;K<M;K++)h=N[K],A[h]=new k([y],a.Base.stat),A[h+"_date"]=new k([L],a.Base.stat);N=["count","unique"];K=0;for(M=N.length;K<M;K++)h=N[K],A[h]=new k([y],a.Base.stat),A[h+"_cat"]=new k([E],a.Base.stat),A[h+"_date"]=new k([L],a.Base.stat);N=["lag"];M=0;for(K=N.length;M<K;M++)h=N[M],A[h]=new k([y,y],y),A[h+"_cat"]=new k([E,y],E),A[h+"_date"]=new k([L,y],L);A.log=new k([y],y);A.substr=new k([E,y,y],E);A.length=new k([E],y);A.upper=new k([E],E);A.lower=new k([E],E);A.indexOf=new k([E,E],y);
A.parseNum=new k([E],y);A.parseDate=new k([E,E],L);A.parseDateDefault=new k([E],L);A.year=new k([L],y);A.month=new k([L],y);A.dayOfMonth=new k([L],y);A.dayOfYear=new k([L],y);A.dayOfWeek=new k([L],y);A.hour=new k([L],y);A.minute=new k([L],y);A.second=new k([L],y);A.bin=new k([y,y],y);A.bin_date=new k([L,E],L);H=function(a){return a.visit({ident:function(a,b){return["ident",{name:b}]},"const":function(a,b,f){return["const",{value:b,type:f.name}]},call:function(a,b,f){return["call",{fname:b,args:f}]},
infixop:function(a,b,f,g){return["infixop",{opname:b,lhs:f,rhs:g}]},conditional:function(a,b,f,g){return["conditional",{cond:b,conseq:f,altern:g}]}})};T=_.clone(A);T.sum=new k([y],a.Base.stat);T.log=new k([y],y);T.nameCollision=new k([E],y);ia={x:y,nameCollision:E};P=function(a){var b;try{if(b=Q(a),"name"in b)return b.name}catch(f){}return a};c.parser={tj:function(a){a=Q(a);return H(a)},tc:function(a){a=Q(a);return I(T,ia,a)},ttc:function(){var b,f,g,c;f=a.Base.cat;g=a.Base.num;c=new J;b=new k([f,
g,c,g],g);f=new k([f,g,f,c],g);return b.unify(f)},createColTypeEnv:function(b){var f,g,c;f={};for(g in b)c=b[g],f[g]=a.Base[c.type];return f},getExpression:function(a){var b,f,g,c;"count(*)"===a&&(a="count(1)");b=Q(a);f=function(a){return{name:a.pretty(),expr:H(a)}};g=function(){};a=f(b);return{exprType:"ident"===a.expr[0]?"ident":!_.has(b,"fname")||"sum"!==(c=b.fname)&&"count"!==c&&"unique"!==c&&"mean"!==c&&"box"!==c&&"median"!==c&&"min"!==c&&"max"!==c?"trans":(g=function(){var a,g=b.fname,c,q,e,
d;e=b.args;d=[];q=0;for(c=e.length;q<c;q++)a=e[q],d.push(f(a));return{fname:g,args:d}},"stat"),expr:a,statInfo:g}},getType:function(a,b,f){null==f&&(f=!0);a=I(A,b,Q(a));return f&&"stat"===a.name?"num":a.name},tokenize:aa,parse:Q,bracket:F,unbracket:P,normalize:function(a){return P(Q(a).pretty())},escape:x,unescape:W}}).call(this);(function(){var n,s,l,d,b,a={}.hasOwnProperty,e=function(b,c){function e(){this.constructor=b}for(var d in c)a.call(c,d)&&(b[d]=c[d]);e.prototype=c.prototype;b.prototype=
new e;b.__super__=c.prototype;return b},h=function(a,b){return function(){return a.apply(b,arguments)}};s=function(){function a(b){var c;this.spec=b;null==this.spec&&(this.spec={});this.flip=null!=(c=this.spec.flip)?c:!1;this.scales=null;b=this.flip?["y","x"]:["x","y"];this.x=b[0];this.y=b[1]}a.prototype.make=function(a){return this.dims=a};a.prototype.setScales=function(a){return this.scales={x:a.x.f,y:a.y.f}};a.prototype.clipping=function(a){return[a.x,a.y,this.dims.eachWidth,this.dims.eachHeight]};
a.prototype.getScale=function(a){};a.prototype.ranges=function(){};return a}();n=function(a){function b(){return d=b.__super__.constructor.apply(this,arguments)}e(b,a);b.prototype.type="cartesian";b.prototype.getScale=function(a){if("x"===a||"y"===a)return this.scales[this[a]];throw c.error.input("Coordinates only keep x & y scales");};b.prototype.ranges=function(){var a;a={};a[this.x]={min:0,max:this.dims.eachWidth};a[this.y]={min:this.dims.eachHeight,max:0};return a};b.prototype.axisType=function(a){return this[a]};
b.prototype.getXY=function(a,b){var c,f;if(a)return c={x:_.isArray(b.x)?_.map(b.x,this.scales.x):this.scales.x(b.x),y:_.isArray(b.y)?_.map(b.y,this.scales.y):this.scales.y(b.y)},{x:c[this.x],y:c[this.y]};c=this.scales[this.x];f=this.scales[this.y];return{x:_.isArray(b.x)?_.map(b.x,c):c(b.x),y:_.isArray(b.y)?_.map(b.y,f):f(b.y)}};b.prototype.getAes=function(a,b,c){return{x:c.x(a[this.x],b[this.x]),y:c.y(a[this.y],b[this.y])}};return b}(s);l=function(a){function d(){this.getXY=h(this.getXY,this);return b=
d.__super__.constructor.apply(this,arguments)}e(d,a);d.prototype.type="polar";d.prototype.make=function(a){this.dims=a;this.cx=this.dims.eachWidth/2;return this.cy=this.dims.eachHeight/2};d.prototype.getScale=function(a){if("r"===a)return this.scales[this.x];if("t"===a)return this.scales[this.y];throw c.error.input("Coordinates only keep r & t scales");};d.prototype.ranges=function(){var a,b,c;b=[this.x,this.y];a=b[0];c=b[1];b={};b[c]={min:0,max:2*Math.PI};b[a]={min:0,max:Math.min(this.dims.eachWidth,
this.dims.eachHeight)/2-10};return b};d.prototype.axisType=function(a){return"x"===this[a]?"r":"t"};d.prototype.getXY=function(a,b){var c,f,g,q,e,d,h,k,m,l,G,B,F,x,H=this;l=function(a,b){return H.cx+a*Math.cos(b-Math.PI/2)};G=function(a,b){return H.cy+a*Math.sin(b-Math.PI/2)};q=[this.x,this.y];e=q[0];h=q[1];if(a){if(_.isArray(b[e])){q={x:[],y:[],r:[],t:[]};F=b[e];f=c=0;for(B=F.length;c<B;f=++c)d=F[f],d=this.scales[e](d),k=this.scales[h](b[h][f]),q.x.push(l(d,k)),q.y.push(G(d,k)),q.r.push(d),q.t.push(k);
return q}d=this.scales[e](b[e]);k=this.scales[h](b[h]);return{x:l(d,k),y:G(d,k),r:d,t:k}}g=function(a){return _.isObject(a)&&"scalefn"===a.t&&"identity"===a.f};c=function(a,b){var f,c;f=g(a);c=g(b);if(f&&!c)return{x:a.v,y:G(H.scales[e](b),0)};if(f&&c)return{x:a.v,y:b.v};if(!f&&c)return{y:b.v,x:G(H.scales[h](a),0)};d=H.scales[e](b);k=H.scales[h](a);return{x:l(d,k),y:G(d,k)}};if(_.isArray(b.x)){q={x:[],y:[]};x=b.x;f=B=0;for(F=x.length;B<F;f=++B)m=x[f],f=b.y[f],m=c(m,f),f=m.x,m=m.y,q.x.push(f),q.y.push(m);
return q}return c(b.x,b.y)};return d}(s);c.coord={cartesian:function(a){return new n(a)},polar:function(a){return new l(a)}};c.coord.make=function(a){if(null==a||null==a.type)return c.coord.cartesian();switch(a.type){case "cartesian":return c.coord.cartesian(a);case "polar":return c.coord.polar(a);default:throw c.error.defn("No such coordinate type "+a.type+".");}}}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m=[].indexOf||function(a){for(var b=0,c=this.length;b<c;b++)if(b in this&&this[b]===a)return b;
return-1};d=c["const"].aes;c.domain={};c.domain.make=function(a,b,e,f){var g,q,d;g=[];for(d in a)q=a[d],g.push(h(q.geoms,b[d],e,f));return c.domain.merge(g)};c.domain.compare=function(a){return a?"cat"===a.type?function(b,c){b=_.indexOf(a.levels,b);c=_.indexOf(a.levels,c);return-1===b?1:-1===c?-1:b<c?-1:b>c?1:0}:c.type.compare(a.type):function(a){return a}};l=function(){return function(a){this.type=a.type;this.min=a.min;this.max=a.max;this.bw=a.bw}}();s=function(){return function(a){this.type=a.type;
this.min=a.min;this.max=a.max;this.bw=a.bw}}();n=function(){return function(a){this.type=a.type;this.levels=a.levels;this.sorted=a.sorted}}();e=function(a){"cat"!==a.type&&a.max===a.min&&(a.bw?(a.max+=a.bw,a.min-=a.bw):0===a.max?a.max+=1:(a.max*=1.1,a.min/=1.1));switch(a.type){case "num":return new l(a);case "date":return new s(a);case "cat":return new n(a)}};c.domain.single=function(a,b,d){var f,g,q,u,v,h,k,m,l,G,B,F,x,H,I,P,R,n,A;if(0===a.length)throw c.error.input("Dataset is none?");g=function(a){return null!=
d?d[a]:null};switch(b.type){case "num":return f=null!=(u=g("bw"))?u:b.bw,1<a.length?(b=null!=(v=g("min"))?v:_.min(a),q=null!=(F=g("max"))?F:_.max(a)+(null!=f?f:0)):1===a.length?f?(b=null!=(x=g("min"))?x:a[0],q=null!=(H=g("max"))?H:a[0]+f):(b=null!=(I=g("min"))?I:a[0]-1,q=null!=(P=g("max"))?P:a[0]+1):(b=null!=(R=g("min"))?R:0,q=null!=(n=null!=(A=g("max"))?A:f)?n:1),e({type:"num",min:b,max:q,bw:f});case "date":return f=null!=(h=g("bw"))?h:b.bw,b=null!=(k=g("min"))?k:_.min(a),q=g("max"),null==q&&(q=
_.max(a),q=function(){switch(f){case "week":return moment.unix(q).add("days",7).unix();case "twomonth":return moment.unix(q).add("months",2).unix();case "quarter":return moment.unix(q).add("months",4).unix();case "sixmonth":return moment.unix(q).add("months",6).unix();case "twoyear":return moment.unix(q).add("years",2).unix();case "fiveyear":return moment.unix(q).add("years",5).unix();case "decade":return moment.unix(q).add("years",10).unix();default:return moment.unix(q).add(f+"s",1).unix()}}()),
e({type:"date",min:b,max:q,bw:f});case "cat":return e({type:"cat",levels:null!=(m=null!=(l=g("levels"))?l:b.levels)?m:_.uniq(a),sorted:null!=(G=null!=(B=g("levels"))?B:b.sorted)?G:!1})}};h=function(b,d,h,f){var g,q,u,v,k;q={};for(g in d)v=d[g],u=h[g],0<=m.call(c["const"].noDomain,g)||(f?q[g]=e(h[g]):(k=a(b,g),q[g]=c.domain.single(k,v,u)));return q};a=function(a,b){var e,f,g,q,d;q=[];for(f in a)for(g in e=a[f],d=e.marks,d)e=d[g],q=q.concat(c.flatten(e[b]));d=[];g=0;for(e=q.length;g<e;g++)f=q[g],c.isDefined(f)&&
d.push(f);return d};c.domain.merge=function(a){var b,c,f,g,q;f={};g=0;for(q=d.length;g<q;g++)b=d[g],c=_.without(_.pluck(a,b),void 0),0<c.length&&(f[b]=k(c));return f};b={num:function(a){var b,d;b=_.compact(_.uniq(_.map(a,function(a){return a.bw})));if(1<b.length)throw c.error.data("Not all layers have the same binwidth.");b=null!=(d=b[0])?d:void 0;d=_.min(_.map(a,function(a){return a.min}));a=_.max(_.map(a,function(a){return a.max}));return e({type:"num",min:d,max:a,bw:b})},date:function(a){var b,
d;b=_.compact(_.uniq(_.map(a,function(a){return a.bw})));if(1<b.length)throw c.error.data("Not all layers have the same binwidth.");b=null!=(d=b[0])?d:void 0;d=_.min(_.map(a,function(a){return a.min}));a=_.max(_.map(a,function(a){return a.max}));return e({type:"date",min:d,max:a,bw:b})},cat:function(a){var b,d,f,g,q,u,v,h;g=[];q=0;for(v=a.length;q<v;q++)if(d=a[q],d.sorted){b=!0;u=0;for(h=g.length;u<h;u++)f=g[u],_.isEqual(f,d.levels)&&(b=!1);b&&g.push(d.levels)}a=_.chain(a).filter(function(a){return!a.sorted}).map(function(a){return a.levels}).value();
if(1<g.length&&_.intersection.apply(this,g))throw c.error.data("You are trying to combine incompatible sorted domains in the same axis.");g=[_.flatten(g,!0)];a=_.union.apply(this,g.concat(a));0===g[0].length&&(a=a.sort());return e({type:"cat",levels:a,sorted:0!==g[0].length})}};k=function(a){var e;e=_.uniq(_.map(a,function(a){return a.type}));if(1<e.length)throw c.error.data("You are trying to merge data of different types in the same axis or legend.");return b[e[0]](a)}}).call(this);(function(){var n,
s,l,d;c.tick={};c.tick.make=function(b,a,e){var h,k,m,n,p,r,f,g;p=null;h=function(a){return a};null!=a.ticks?r="num"===e?_.filter(a.ticks,function(a){return a>=b.min&&a<=b.max}):a.ticks:(h=null!=(r=a.numticks)?r:5,h=d[e](b,h),r=h.ticks,p=h.step);h=a.labels?function(b){var f;return null!=(f=a.labels[b])?f:b}:a.formatter?a.formatter:c.format(e.split("-")[0],p);p={};e=l(e,h);if(r)for(k=f=0,g=r.length-1;0<=g?f<=g:f>=g;k=0<=g?++f:--f)n=0===k?null:r[k-1],m=k===r.length-1?null:r[k+1],k=r[k],m=e(k,n,m),p[m.value]=
m;return{ticks:p,ticksFormatter:h}};n=function(){return function(b){this.location=b.location;this.value=b.value;this.index=b.index;this.evtData=b.evtData}}();l=function(b,a){var c;c=0;return function(d,k,m){var l;"cat"===b?l={"in":[d]}:(l={},null!=k&&(l.ge=k),null!=m&&(l.le=m));return new n({location:d,value:a(d),index:c++,evtData:l})}};s=function(b,a){var c,d;d=Math.pow(10,Math.floor(Math.log(b/a)/Math.LN10));c=a/b*d;0.15>c?d*=10:0.35>=c?d*=5:0.75>=c&&(d*=2);return d};d={none:function(){return{}},
cat:function(b,a){var c,d,k,m,l,p,r;k=Math.max(1,Math.round(b.levels.length/a));m=[];r=b.levels;c=l=0;for(p=r.length;l<p;c=++l)d=r[c],0===c%k&&m.push(d);return{ticks:m}},num:function(b,a){var c,d,k,m;k=b.min;d=b.max;if(c=b.bw){for(;(d-k)/c>1.4*a;)c*=2;m=k}else c=s(d-k,a),m=Math.ceil(k/c)*c;for(k=[];m<=d;)k.push(m),m+=c;return{ticks:k,step:Math.floor(Math.log(c)/Math.LN10)}},"num-log":function(b,a){var d,h,k,m,l,p,r,f,g;f=[];p=b.min;l=b.max;h=function(a){return Math.log(a)/Math.LN10};d=function(a){return Math.exp(a*
Math.LN10)};m=Math.max(h(p),0);k=h(l);r=s(k-m,a);for(g=Math.ceil(m/r)*r;g<k+c["const"].epsilon;){if(!(0!==g%1&&0.1>=g%1)){if(g%1>c["const"].epsilon){if(m=Math.floor(g)+h(10*(g%1)),0===m%1){g+=r;continue}}else m=g;m=d(m);m<p||m>l||f.push(m)}g+=r}return{ticks:f}},date:function(b,a){var d,h,k,m,l,p,r;m=b.min;k=b.max;if(d=b.bw)for(l=d;"decade"!==l&&(k-m)/c["const"].approxTimeInSeconds[l]>1.4*a;)l=c["const"].timerange[_.indexOf(c["const"].timerange,l)+1];else for(h in d=(k-m)/a,l="decade",r=c["const"].approxTimeInSeconds,
r)if(p=r[h],d<1.4*p){l=h;break}p=[];h=moment.unix(m).startOf(l);d=function(){switch(l){case "twomonth":return["months",2];case "quarter":return["months",4];case "sixmonth":return["months",6];case "twoyear":return["years",2];case "fiveyear":return["years",5];case "decade":return["years",10];default:return[l+"s",1]}}();for(h.unix()<m&&h.add(d[0],d[1]);h.unix()<=k;)p.push(h.unix()),h.add(d[0],d[1]);return{ticks:p,step:l}}}}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m,t=function(a,b){return function(){return a.apply(b,
arguments)}},p={}.hasOwnProperty,r=function(a,b){function c(){this.constructor=a}for(var d in b)p.call(b,d)&&(a[d]=b[d]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a};a=c["const"].scaleFns;n=function(a){function b(){this.render=t(this.render,this);this.make=t(this.make,this);this.position="none";this.title=this.titletext=null}r(b,a);b.prototype.make=function(a){var b,f,g,c;b=a.guideSpec;g=a.title;f=a.position;this.size=a.size;this.color=a.color;a=function(a,f){var g;
return null!=(g=b[a])?g:f};this.titletext=a("title",g);this.position=null!=(c=a("position",f))?c:this.defaultPosition;if("out"===this.position)return this.position="bottom"};b.prototype.render=function(a,b,f){if("none"!==this.position)return null!=this.title&&a.remove(this.title),this.title=a.add(this._makeTitle(b,f),null,null,"guide-"+this.titleType);if(null!=this.title)return a.remove(this.title)};b.prototype.dispose=function(a){a.remove(this.title);return this.title=null};b.prototype._makeTitle=
function(){throw c.error.impl();};b.prototype.getDimension=function(){var a;a={};"none"!==this.position&&(a[this.position]=10);return a};return b}(c.Guide);l=function(b){function g(){return e=g.__super__.constructor.apply(this,arguments)}r(g,b);g.prototype.defaultPosition="bottom";g.prototype.titleType="titleH";g.prototype._makeTitle=function(b,f){var g,c,d,e,h;g="top"===this.position?b.paddingTop+b.guideTop-(null!=(c=f.top)?c:0)-2:b.height-b.paddingBottom-b.guideBottom+(null!=(d=f.bottom)?d:0);return{type:"text",
x:a.identity(b.paddingLeft+b.guideLeft+(b.width-b.paddingLeft-b.guideLeft-b.paddingRight-b.guideRight)/2),y:a.identity(g),color:a.identity(null!=(e=this.color)?e:"black"),size:a.identity(null!=(h=this.size)?h:12),text:this.titletext,"text-anchor":"middle"}};return g}(n);b=function(b){function g(){return h=g.__super__.constructor.apply(this,arguments)}r(g,b);g.prototype.defaultPosition="left";g.prototype.titleType="titleV";g.prototype._makeTitle=function(b,f){var g,c,d,e,h;g="left"===this.position?
b.paddingLeft+b.guideLeft-(null!=(c=f.left)?c:0)-7:b.width-b.paddingRight-b.guideRight+(null!=(d=f.right)?d:0);c=b.paddingTop+b.guideTop+(b.height-b.paddingTop-b.guideTop-b.paddingBottom-b.guideBottom)/2;return{type:"text",x:a.identity(g),y:a.identity(c),color:a.identity(null!=(e=this.color)?e:"black"),size:a.identity(null!=(h=this.size)?h:12),text:this.titletext,"text-anchor":"middle",transform:"r270"}};return g}(n);d=function(b){function g(){return k=g.__super__.constructor.apply(this,arguments)}
r(g,b);g.prototype.titleType="title";g.prototype._makeTitle=function(b,f){var g,c;return{type:"text",x:a.identity(b.width/2),y:a.identity(20),color:a.identity(null!=(g=this.color)?g:"black"),size:a.identity(null!=(c=this.size)?c:12),text:this.titletext,"font-size":"13px","font-weight":"bold","text-anchor":"middle"}};return g}(n);s=function(b){function g(){this.render=t(this.render,this);this.make=t(this.make,this);return m=g.__super__.constructor.apply(this,arguments)}r(g,b);g.prototype.make=function(a){var b;
b=a.title;this.size=a.size;this.color=a.color;return this.titletext=b};g.prototype.render=function(a,b,f){return null!=this.title?this.title=a.animate(this.title,this._makeTitle(b,f)):this.title=a.add(this._makeTitle(b,f),null,null,"guide-facet-title")};g.prototype._makeTitle=function(b,f){var g,c;return{type:"text",x:a.identity(f.x+b.eachWidth/2),y:a.identity(f.y-7),color:a.identity(null!=(g=this.color)?g:"black"),size:a.identity(null!=(c=this.size)?c:12),text:this.titletext,"text-anchor":"middle"}};
return g}(n);null==c.guide&&(c.guide={});c.guide.title=function(a){return"y"===a||"r"===a?new b:"main"===a?new d:"facet"===a?new s:new l}}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m,t,p={}.hasOwnProperty,r=function(a,b){function f(){this.constructor=a}for(var g in b)p.call(b,g)&&(a[g]=b[g]);f.prototype=b.prototype;a.prototype=new f;a.__super__=b.prototype;return a},f=function(a,b){return function(){return a.apply(b,arguments)}},g=[].indexOf||function(a){for(var b=0,f=this.length;b<f;b++)if(b in
this&&this[b]===a)return b;return-1};e=c["const"].scaleFns;n=function(a){function b(){this.axesGeoms={}}r(b,a);b.prototype.make=function(a){var b,f,g,d;this.domains=a.domains;this.coord=a.coord;this.scales=a.scales;this.specs=a.specs;this.labels=a.labels;return this.axes={x:c.guide.axis(this.coord.axisType("x"),{domain:this.domains.x,type:this.scales.x.tickType(),guideSpec:null!=(b=this.specs.x)?b:{},key:null!=(f=this.labels.x)?f:"x"}),y:c.guide.axis(this.coord.axisType("y"),{domain:this.domains.y,
type:this.scales.y.tickType(),guideSpec:null!=(g=this.specs.y)?g:{},key:null!=(d=this.labels.y)?d:"y"})}};b.prototype.getDimension=function(a){var b,f,g;a={};g=this.axes;for(f in g)b=g[f],b=b.getDimension(),"left"===b.position?a.left=b.width:"right"===b.position?a.right=b.width:"bottom"===b.position?a.bottom=b.height:"top"===b.position&&(a.top=b.height);return a};b.prototype.render=function(a,b,f){var g,d,e,q,u,h,k,I,m,r,l,p,n,t,s,K;h=_.keys(f.indices);e=c.compare(_.keys(this.axesGeoms),h).deleted;
u=0;for(r=e.length;u<r;u++)for(q in d=e[u],l=this.axesGeoms[d],l)d=l[q],d.dispose(b());e={top:0,left:0,right:a.eachWidth,bottom:a.eachHeight,width:a.eachWidth,height:a.eachHeight};q=f.edge(this.axes.x.position);u=f.edge(this.axes.y.position);r={renderLabel:!1,renderTick:!1};l={renderLabel:!1,renderTick:!1};"r"===this.axes.x.type&&(r.renderLine=!1);"r"===this.axes.y.type&&(l.renderLine=!1);n=0;for(t=h.length;n<t;n++)for(d=h[n],I=f.getOffset(a,d),null==(p=this.axesGeoms)[d]&&(p[d]={x:new c.Geometry("guide"),
y:new c.Geometry("guide")}),m=b(I,!1,!1),I=q(d)?{}:r,this.axesGeoms[d].x.set(this.axes.x.calculate(e,this.coord,I)),this.axesGeoms[d].x.render(m),I=u(d)?{}:l,this.axesGeoms[d].y.set(this.axes.y.calculate(e,this.coord,I)),this.axesGeoms[d].y.render(m),s=["x","y"],I=0,m=s.length;I<m;I++)for(k in g=s[I],K=this.axesGeoms[d][g].pts,K)g=K[k],g.grid&&g.grid.toBack()};b.prototype.dispose=function(a){var b,f,g;g=this.axesGeoms;for(f in g)b=g[f],b.x.dispose(a),b.y.dispose(a);return this.axesGeoms={}};return b}(c.GuideSet);
s=function(a){function b(a){this.calculate=f(this.calculate,this);var d,e,q,u,h;d=a.domain;u=a.type;e=a.guideSpec;a=a.key;q=function(a,b){var f;return null!=(f=e[a])?f:b};this.position=q("position",this.defaultPosition);if(h=this.position,0>g.call(this.validPositions,h))throw c.error.defn("X-axis position can't be "+this.position+".");this.titletext=q("title",a);this.renderTick=q("renderTick",this.renderTickDefault);this.renderGrid=q("renderGrid",this.renderGridDefault);this.renderLabel=q("renderLabel",
this.renderLabelDefault);this.renderLine=q("renderLine",this.renderLineDefault);this.gridColor=q("gridColor",this.gridColor);d=c.tick.make(d,e,u);this.ticks=d.ticks;this.ticksFormatter=d.ticksFormatter;this.maxwidth=_.max(_.map(this.ticks,function(a){return c.strSize(a.value)}));this.maxwidth=Math.max(this.maxwidth,0)}r(b,a);b.prototype.renderTickDefault=!0;b.prototype.renderGridDefault=!0;b.prototype.renderLabelDefault=!0;b.prototype.renderLineDefault=!0;b.prototype.calculate=function(a,b,f){var g,
c,d,e,q,u,h;this.coord=b;if("none"===this.position)return{};null==f&&(f={});a.centerx=a.left+a.width/2;a.centery=a.top+a.height/2;a.radius=Math.min(a.width,a.height)/2-10;b={};this.renderLine&&(b.line={marks:{0:this._renderline(a)}});e=this.ticks;for(g in e)d=e[g],c={},this.renderTick&&(null!=(q=f.renderTick)?q:1)&&(c.tick=this._makeTick(a,d)),this.renderLabel&&(null!=(u=f.renderLabel)?u:1)&&(c.text=this._makeLabel(a,d)),this.renderGrid&&(null!=(h=f.renderGrid)?h:1)&&(c.grid=this._makeGrid(a,d)),
b[g]={marks:c};return b};b.prototype._makeTick=function(a){if(!a)throw c.error.impl();a.type="path";a.stroke=e.identity("#666");a.color=e.identity("#666");return a};b.prototype._makeLabel=function(a){if(!a)throw c.error.impl();a.type="text";a.stroke=e.identity("#666");a.color=e.identity("#666");return a};b.prototype._makeGrid=function(a){if(!a)throw c.error.impl();a.stroke=null!=this.gridColor?this.gridColor:"#EFEFEF";return a};return b}(c.Guide);b=function(a){function b(){return h=b.__super__.constructor.apply(this,
arguments)}r(b,a);b.prototype.type="x";b.prototype.renderGridDefault=!1;b.prototype.defaultPosition="bottom";b.prototype.validPositions=["top","bottom","none"];b.prototype._renderline=function(a){var b,f;f="top"===this.position?e.identity(a.top):e.identity(a.bottom);b=e.identity(a.left);a=e.identity(a.left+a.width);return{type:"path",y:[f,f],x:[b,a],stroke:e.identity("#666")}};b.prototype._makeTick=function(a,f){var g,c;"top"===this.position?(g=e.identity(a.top),c=e.identity(a.top-5)):(g=e.identity(a.bottom),
c=e.identity(a.bottom+5));return b.__super__._makeTick.call(this,{x:[f.location,f.location],y:[g,c]})};b.prototype._makeLabel=function(a,f){var g;g="top"===this.position?e.identity(a.top-15):e.identity(a.bottom+15);return b.__super__._makeLabel.call(this,{x:f.location,y:g,text:f.value,"text-anchor":"middle"})};b.prototype._makeGrid=function(a,f){var g,c;g=e.identity(a.top);c=e.identity(a.bottom);return b.__super__._makeGrid.call(this,{type:"path",x:[f.location,f.location],y:[g,c]})};b.prototype.getDimension=
function(){var a;return{position:null!=(a=this.position)?a:"bottom",height:30,width:"all"}};return b}(s);a=function(a){function b(){return k=b.__super__.constructor.apply(this,arguments)}r(b,a);b.prototype.type="y";b.prototype.renderLineDefault=!1;b.prototype.renderTickDefault=!1;b.prototype.defaultPosition="left";b.prototype.validPositions=["left","right","none"];b.prototype._renderline=function(a){var b,f;b="left"===this.position?e.identity(a.left):e.identity(a.right);f=e.identity(a.top);a=e.identity(a.top+
a.height);return{type:"path",x:[b,b],y:[f,a],stroke:e.identity("#666")}};b.prototype._makeTick=function(a,f){var g,c;"left"===this.position?(g=e.identity(a.left),c=e.identity(a.left-5)):(g=e.identity(a.right),c=e.identity(a.right+5));return b.__super__._makeTick.call(this,{x:[g,c],y:[f.location,f.location]})};b.prototype._makeLabel=function(a,f){var g;g="left"===this.position?e.identity(a.left-7):e.identity(a.right+7);return b.__super__._makeLabel.call(this,{x:g,y:f.location,text:f.value,"text-anchor":"left"===
this.position?"end":"start"})};b.prototype._makeGrid=function(a,f){var g,c;g=e.identity(a.left);c=e.identity(a.right);return b.__super__._makeGrid.call(this,{type:"path",y:[f.location,f.location],x:[g,c]})};b.prototype.getDimension=function(){var a;return{position:null!=(a=this.position)?a:"right",height:"all",width:5+this.maxwidth}};return b}(s);l=function(a){function b(){return m=b.__super__.constructor.apply(this,arguments)}r(b,a);b.prototype.type="r";b.prototype.defaultPosition="left";b.prototype.validPositions=
["left","right","none"];b.prototype._renderline=function(a){var b,f;b=e.identity(a.left);f=e.identity(a.top);a=e.identity(a.top+a.height/2);return{type:"path",x:[b,b],y:[f,a],stroke:e.identity("#666")}};b.prototype._makeTick=function(a,f){return b.__super__._makeTick.call(this,{x:[e.identity(a.left),e.identity(a.left-5)],y:[f.location,f.location]})};b.prototype._makeLabel=function(a,f){return b.__super__._makeLabel.call(this,{x:e.identity(a.left-7),y:f.location,text:f.value,"text-anchor":"end"})};
b.prototype._makeGrid=function(a,f){return b.__super__._makeGrid.call(this,{type:"circle",x:e.identity(a.centerx),y:e.identity(a.centery),size:e.identity(this.coord.getScale("r")(f.location)),color:e.identity("none"),"fill-opacity":0,"stroke-width":1})};b.prototype.getDimension=function(){return{position:"left",height:"all",width:5+this.maxwidth}};return b}(s);d=function(a){function b(){return t=b.__super__.constructor.apply(this,arguments)}r(b,a);b.prototype.type="t";b.prototype.defaultPosition=
"out";b.prototype.validPositions=["out","none"];b.prototype._renderline=function(a){return{type:"circle",x:e.identity(a.centerx),y:e.identity(a.centery),size:e.identity(a.radius),color:e.identity("none"),stroke:e.identity("#666"),"stroke-width":1}};b.prototype._makeTick=function(a,f){return b.__super__._makeTick.call(this,{x:[f.location,f.location],y:[e.max(0),e.max(3)]})};b.prototype._makeLabel=function(a,f){return b.__super__._makeLabel.call(this,{x:f.location,y:e.max(12),text:f.value,"text-anchor":"middle"})};
b.prototype._makeGrid=function(a,f){var g,c,d,q;c=e.identity(a.centerx);q=e.identity(a.centery);g=this.coord.getScale("t")(f.location)-Math.PI/2;d=e.identity(a.centerx+a.radius*Math.cos(g));g=e.identity(a.centery+a.radius*Math.sin(g));return b.__super__._makeGrid.call(this,{type:"path",y:[q,g],x:[c,d]})};b.prototype.getDimension=function(){return{}};return b}(s);null==c.guide&&(c.guide={});c.guide.axis=function(f,g){if("x"===f)return new b(g);if("y"===f)return new a(g);if("r"===f)return new l(g);
if("t"===f)return new d(g)};c.guide.axes=function(a){return new n(a)}}).call(this);(function(){var n,s,l,d,b,a,e,h={}.hasOwnProperty,k=function(a,b){function f(){this.constructor=a}for(var g in b)h.call(b,g)&&(a[g]=b[g]);f.prototype=b.prototype;a.prototype=new f;a.__super__=b.prototype;return a},m=[].indexOf||function(a){for(var b=0,f=this.length;b<f;b++)if(b in this&&this[b]===a)return b;return-1},t=function(a,b){return function(){return a.apply(b,arguments)}};b=c["const"].scaleFns;c.guide.legends=
function(){return new l};c.guide.legend=function(a,b){return"left"===b||"right"===b?new d(a):new n(a)};l=function(a){function b(){this.legends=[];this.deletedLegends=[]}k(b,a);b.prototype.make=function(a){var b,d,e,h,k,m,l,p,r,B,n,x;e=a.domains;p=a.layers;h=a.guideSpec;n=a.scales;l=a.layerMapping;this.position=a.position;d=a.dims;null==this.postion&&(this.postion="right");if("none"!==this.position){b=this._mergeAes(e,p);for(m=0;m<this.legends.length;){r=this.legends[m];B=!0;for(k=0;k<b.length;){a=
b[k];if(_.isEqual(a,r.aes)){b.splice(k,1);B=!1;break}k++}B?(this.deletedLegends.push(r),this.legends.splice(m,1)):m++}r=0;for(k=b.length;r<k;r++)a=b[r],this.legends.push(c.guide.legend(a,this.position));m=this.legends;B=[];b=0;for(k=m.length;b<k;b++)r=m[b],a=r.aes[0],B.push(r.make({domain:e[a],position:this.position,guideSpec:null!=(x=h[a])?x:{},type:n[a].tickType(),mapping:l,keys:c.getLabel(p,a),dims:d}));return B}};b.prototype._mergeAes=function(a,b){var d,e,h,k,l,r,p;l=[];for(d in a)if(!(0<=m.call(c["const"].noLegend,
d)||(h=_.map(b,function(a){return a.mapping[d]}),_.all(h,_.isUndefined)))){k=!1;r=0;for(p=l.length;r<p;r++)if(e=l[r],_.isEqual(e.mapped,h)){e.aes.push(d);k=!0;break}k||l.push({aes:[d],mapped:h})}return _.pluck(l,"aes")};b.prototype.getDimension=function(a){var b,c,d;b={};if("left"===(c=this.position)||"right"===c)b[this.position]=this._leftrightWidth(a);else if("top"===(d=this.position)||"bottom"===d)b[this.position]=this._topbottomHeight(a);return b};b.prototype._leftrightWidth=function(a){var b,
c,d,e,h,k,m,l;e=a.chartHeight;h=0;b=10;c=0;l=this.legends;k=0;for(m=l.length;k<m;k++)d=l[k],d=d.getDimension(a),d.height+c>e&&(b+=h+5,h=c=0),d.width>h&&(h=d.width),c+=d.height;return b+h};b.prototype._topbottomHeight=function(a){var b,c,d,e,h;c=10;h=this.legends;d=0;for(e=h.length;d<e;d++)b=h[d],b=b.getDimension(a),c+=b.height+10;return c};b.prototype.render=function(a,b,c){var d,e,h,k,m;e=b();m=this.deletedLegends;h=0;for(k=m.length;h<k;h++)d=m[h],d.dispose(e);this.deletedLegends=[];if("left"===
this.position||"right"===this.position)return this._renderV(a,b,c);if("top"===this.position||"bottom"===this.position)return this._renderH(a,b,c)};b.prototype._renderV=function(a,b,c){var d,e,h,k,m,l,r,p,n,x,H,I,P;d=a.paddingTop+a.guideTop;e="left"===this.position?a.paddingLeft:a.width-a.guideRight-a.paddingRight;m=0;k=a.height-a.guideTop-a.paddingTop;p=10;r="right"===this.position?c.right:0;I=this.legends;P=[];x=0;for(H=I.length;x<H;x++)h=I[x],l=h.getDimension(a),l.height+c.y>k&&(r+=m+5,m=p=0),l.width>
m&&(m=l.width),n={x:r+e,y:p+d},h.render(b(n,!1,!1),m),P.push(p+=l.height);return P};b.prototype._renderH=function(a,b,c){var d,e,h,k,m,l;d=a.paddingLeft;e="top"===this.position?a.paddingTop:a.height-a.guideBottom-a.paddingBottom;e={x:d,y:"top"===this.position?c.top+e:c.bottom+e+10};m=this.legends;l=[];h=0;for(k=m.length;h<k;h++)c=m[h],d=c.getDimension(a),c.render(b(e,!1,!1)),l.push(e.y+=d.height+10);return l};b.prototype.dispose=function(a){var b,c,d,e,h;e=this.legends;h=[];c=0;for(d=e.length;c<d;c++)b=
e[c],h.push(b.dispose(a));return h};return b}(c.GuideSet);s=function(a){function d(a){this.aes=a;this._makeEvtData=t(this._makeEvtData,this);this._makeTick=t(this._makeTick,this);this.geometry=new c.Geometry("guide")}k(d,a);d.prototype.TITLEHEIGHT=15;d.prototype.TICKHEIGHT=12;d.prototype.SPACING=10;d.prototype.make=function(a){var b,d,e,h,k;b=a.domain;e=a.type;d=a.guideSpec;this.mapping=a.mapping;this.position=a.position;a=a.keys;this.titletext=null!=(h=d.title)?h:a;return k=c.tick.make(b,d,e),this.ticks=
k.ticks,k};d.prototype.calculate=function(){var a,b,c,d,e;b={};b.title={marks:{0:this._makeTitle(this.titletext)},evtData:{aes:this.aes[0],value:"legendTitle"}};e=this.ticks;for(c in e)a=e[c],d={},d.tick=this._makeTick(a),d.text=this._makeLabel(a),a=this._makeEvtData(a),b[c]={marks:d,evtData:a};return b};d.prototype.render=function(a){this.geometry.set(this.calculate());return this.geometry.render(a)};d.prototype.dispose=function(a){return this.geometry.dispose(a)};d.prototype._makeTitle=function(a,
c){null==c&&(c={x:0,y:0});return{type:"text",x:b.identity(c.x+5),y:b.identity(c.y),color:b.identity("black"),text:a,"text-anchor":"start"}};d.prototype._makeLabel=function(a,c){c||(c={x:0,y:15+12*a.index});return{type:"text",x:b.identity(c.x+20),y:b.identity(c.y+1),color:b.identity("black"),text:a.value,"text-anchor":"start"}};d.prototype._makeTick=function(a,g){var d,e,h,k;g||(g={x:0,y:15+12*a.index});e={type:"circle",x:b.identity(g.x+10),y:b.identity(g.y),color:b.identity("steelblue")};k=this.mapping;
for(d in k)h=k[d],0<=m.call(c["const"].noLegend,d)||(h=h[0],0<=m.call(this.aes,d)?e[d]=a.location:null!=h.type&&"const"===h.type?e[d]=b.identity(h.value):_.isObject(h)?e[d]=b.identity(c["const"].defaults[d]):e[d]=b.identity(h));_.isObject(e.size)&&(e.size=b.identity(5));return e};d.prototype._makeEvtData=function(a){var b,c,d,e,h,k,l;c={};l=this.mapping;for(b in l)for(e=l[b],h=0,k=e.length;h<k;h++)d=e[h],0<=m.call(this.aes,b)&&"map"===d.type&&(c[d.value]=_.extend(a.evtData,{value:a.location,aes:b}));
return c};return d}(c.Guide);d=function(b){function d(){return a=d.__super__.constructor.apply(this,arguments)}k(d,b);d.prototype.make=function(a){var b;d.__super__.make.call(this,a);this.height=this.TITLEHEIGHT+this.SPACING+this.TICKHEIGHT*_.size(this.ticks);b=c.strSize(this.titletext);a=_.max(_.map(this.ticks,function(a){return c.strSize(a.value)}));return this.maxwidth=Math.max(b,a)};d.prototype.getDimension=function(){return{position:this.position,height:this.height,width:15+this.maxwidth}};return d}(s);
n=function(a){function b(){return e=b.__super__.constructor.apply(this,arguments)}k(b,a);b.prototype.TICKSPACING=25;b.prototype.make=function(a){var g,d,e,h;b.__super__.make.call(this,a);this.maxwidth=a.dims.width;this.height=this.TITLEHEIGHT+this.SPACING;a=0;this.height+=this.TICKHEIGHT;h=this.ticks;d=0;for(e=h.length;d<e;d++)g=h[d],g=c.strSize(g.value)+this.TICKSPACING,a+g<this.maxwidth?a+=g:(this.height+=this.TICKHEIGHT,a=g);return null};b.prototype.calculate=function(){var a,b,d,e,h,k,m;b={};
b.title={marks:{0:this._makeTitle(this.titletext)}};h={x:0,y:this.TITLEHEIGHT};m=this.ticks;for(d in m)k=m[d],e={},e.tick=this._makeTick(k,h),e.text=this._makeLabel(k,h),a=this._makeEvtData(k,h),b[d]={marks:e,evtData:a},a=c.strSize(k.value)+this.TICKSPACING,h.x+a<this.maxwidth?h.x+=a:(h.x=0,h.y+=this.TICKHEIGHT);return b};b.prototype.getDimension=function(){return{position:this.position,height:this.height,width:"all"}};return b}(s)}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m,t,p,r,f,g,q,u,v=
function(a,b){return function(){return a.apply(b,arguments)}},D={}.hasOwnProperty,C=function(a,b){function c(){this.constructor=a}for(var f in b)D.call(b,f)&&(a[f]=b[f]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a};m=function(){function a(b){this.f=null}a.prototype.make=function(a){this.domain=a;this.compare=c.domain.compare(a);if(!a)return this._makeNone();switch(a.type){case "num":return this._makeNum();case "date":return this._makeDate();case "cat":return this._makeCat()}};
a.prototype._makeNone=function(){throw c.error.impl("You are using a scale that does not support null values");};a.prototype._makeNum=function(){throw c.error.impl("You are using a scale that does not support numbers");};a.prototype._makeDate=function(){throw c.error.impl("You are using a scale that does not support dates");};a.prototype._makeCat=function(){throw c.error.impl("You are using a scale that does not support categories");};a.prototype.tickType=function(){if(!this.domain)return this._tickNone();
switch(this.domain.type){case "num":return this._tickNum();case "date":return this._tickDate();case "cat":return this._tickCat()}};a.prototype._tickNone=function(){return"none"};a.prototype._tickNum=function(){return"num"};a.prototype._tickDate=function(){return"date"};a.prototype._tickCat=function(){return"cat"};a.prototype._identityWrapper=function(a){return function(b){return _.isObject(b)&&"scalefn"===b.t&&"identity"===b.f?b.v:a(b)}};return a}();n=function(a){function b(a){this._catWrapper=v(this._catWrapper,
this);this._dateWrapper=v(this._dateWrapper,this);this._numWrapper=v(this._numWrapper,this);this.finv=this.f=null}C(b,a);b.prototype.make=function(a,c,f){this.range=c;this.space=f;_.isNumber(this.space)||(this.space=0.05);return b.__super__.make.call(this,a)};b.prototype._makeNone=function(){var a,b=this;a=(this.range.max-this.range.min)*this.space;this.f=this._NaNCheckWrap(function(c){var f;if(_.isObject(c))switch(f=function(b){return(this.range.max-this.range.min-2*a)/b},c.f){case "identity":return c.v;
case "middle":return b.range.max/2+b.range.min/2;case "max":return b.range.max;case "min":return b.range.min;case "novalue":return b.range.max/2+b.range.min/2;case "upper":return c.m?b.range.min+a+(c.n+1)*f(c.m):b.range.max-a;case "lower":return c.m?b.range.min+a+c.n*f(c.m):b.range.min+a}else return b.range.max/2+b.range.min/2});return this.finv=function(){return{}}};b.prototype._NaNCheckWrap=function(a){return function(b){if(c.isDefined(b)){b=a(b);if(isNaN(b)||Infinity===b||-Infinity===b)throw c.error.scale("Scale outputed a value that is not finite.");
return b}}};b.prototype._numWrapper=function(a,b){var f=this;return this._NaNCheckWrap(function(g){var d,e,q;if(_.isObject(g)){if("scalefn"===g.t)switch(g.f){case "identity":return g.v;case "middle":return b(g.v+a.bw/2);case "max":return f.range.max+g.v;case "min":return f.range.min+g.v;case "upper":case "lower":q=b(g.v+a.bw);d=b(g.v);e=(q-d)*f.space;if("upper"===g.f&&!g.m)return q-e;if("lower"===g.f&&!g.m)return d+e;q=(q-d-2*e)/g.m;if("upper"===g.f)return d+e+(g.n+1)*q;if("lower"===g.f)return d+
e+g.n*q}throw c.error.input("Unknown object "+g+" is passed to a scale");}return b(g)})};b.prototype._dateWrapper=function(a,b){var f=this;return this._NaNCheckWrap(function(g){var d,e,q,h;if(_.isObject(g)){if("scalefn"===g.t)switch(g.f){case "identity":return g.v;case "max":return f.range.max+g.v;case "min":return f.range.min+g.v;case "upper":case "middle":case "lower":h=function(a,b,c){var f;null==c&&(c=0);f=moment.unix(g.v).startOf(b);f[b](a*Math.floor(f[b]()/a)+a*c);return f.unix()};q=b(function(){switch(a.bw){case "week":return moment.unix(g.v).day(7).unix();
case "twomonth":return h(2,"month");case "quarter":return h(4,"month");case "sixmonth":return h(6,"month");case "twoyear":return h(2,"year");case "fiveyear":return h(5,"year");case "decade":return h(10,"year");default:return moment.unix(g.v).endOf(a.bw).unix()}}());d=b(function(){switch(a.bw){case "week":return moment.unix(g.v).day(0).unix();case "twomonth":return h(2,"month",1);case "quarter":return h(4,"month",1);case "sixmonth":return h(6,"month",1);case "twoyear":return h(2,"year",1);case "fiveyear":return h(5,
"year",1);case "decade":return h(10,"year",1);default:return moment.unix(g.v).startOf(a.bw).unix()}}());e=(q-d)*f.space;if("middle"===g.f)return q/2+d/2;if("upper"===g.f&&!g.m)return q-e;if("lower"===g.f&&!g.m)return d+e;q=(q-d-2*e)/g.m;if("upper"===g.f)return d+e+(g.n+1)*q;if("lower"===g.f)return d+e+g.n*q}throw c.error.input("Unknown object "+g+" is passed to a scale");}return b(g)})};b.prototype._catWrapper=function(a,b){var f=this;return this._NaNCheckWrap(function(g){var d,e,q;e=a*f.space;if(_.isObject(g)){if("scalefn"===
g.t)switch(g.f){case "identity":return g.v;case "max":return f.range.max+g.v;case "min":return f.range.min+g.v;case "upper":case "middle":case "lower":q=b(g.v)+a;d=b(g.v);if("middle"===g.f)return q/2+d/2;if("upper"===g.f&&!g.m)return q-e;if("lower"===g.f&&!g.m)return d+e;q=(q-d-2*e)/g.m;if("upper"===g.f)return d+e+(g.n+1)*q;if("lower"===g.f)return d+e+g.n*q}throw c.error.input("Unknown object "+g+" is passed to a scale");}return b(g)+a/2})};return b}(m);a=function(a){function b(){return t=b.__super__.constructor.apply(this,
arguments)}C(b,a);b.prototype._makeNum=function(){var a,b;b=c.linear(this.domain.min,this.range.min,this.domain.max,this.range.max);a=c.linear(this.range.min,this.domain.min,this.range.max,this.domain.max);this.f=this._numWrapper(this.domain,b);return this.finv=function(b,c){var f;f=[a(b),a(c)];return{ge:_.min(f),le:_.max(f)}}};b.prototype._makeDate=function(){var a,b;b=c.linear(this.domain.min,this.range.min,this.domain.max,this.range.max);a=c.linear(this.range.min,this.domain.min,this.range.max,
this.domain.max);this.f=this._dateWrapper(this.domain,b);return this.finv=function(b,c){var f;f=[a(b),a(c)];return{ge:_.min(f),le:_.max(f)}}};b.prototype._makeCat=function(){var a,b=this;a=(this.range.max-this.range.min)/this.domain.levels.length;this.f=this._catWrapper(a,function(c){c=_.indexOf(b.domain.levels,c);return-1===c?null:b.range.min+c*a});return this.finv=function(c,f){var g;f<c&&(g=[f,c],c=g[0],f=g[1]);return{"in":b.domain.levels.slice(Math.floor(c/a),+Math.floor(f/a)+1||9E9)}}};return b}(n);
e=function(a){function b(){return p=b.__super__.constructor.apply(this,arguments)}C(b,a);b.prototype._makeNum=function(){var a,b,f,g;if(0>this.domain.min)throw c.error.input("Log scale cannot handle zero or negative input.");a=Math.log;f=c.linear(a(this.domain.min),this.range.min,a(this.domain.max),this.range.max);this.f=this._numWrapper(this.domain,function(b){return f(a(b))});g=c.linear(this.range.min,a(this.domain.min),this.range.max,a(this.domain.max));b=function(a){return Math.exp(g(a))};return this.finv=
function(a,c){var f;f=[b(a),b(c)];return{ge:_.min(f),le:_.max(f)}}};b.prototype._tickNum=function(){return"num-log"};return b}(n);n=function(a){function b(){this._makeDate=v(this._makeDate,this);this._makeNum=v(this._makeNum,this);return r=b.__super__.constructor.apply(this,arguments)}C(b,a);b.prototype._makeNum=function(){var a,b,f;a=0===this.domain.min?0:1;b=Math.sqrt;f=c.linear(b(this.domain.min),a,b(this.domain.max),10);return this.f=this._identityWrapper(function(a){return f(b(a))})};b.prototype._makeDate=
function(){return this._makeNum()};return b}(m);h=function(a){function b(){this._makeDate=v(this._makeDate,this);this._makeNum=v(this._makeNum,this);return f=b.__super__.constructor.apply(this,arguments)}C(b,a);b.prototype._makeNum=function(){return this.f=this._identityWrapper(c.linear(this.domain.min,0===this.domain.min?0:0.1,this.domain.max,1))};b.prototype._makeDate=function(){return this._makeNum()};return b}(m);k=function(a){function b(){this._makeCat=v(this._makeCat,this);return g=b.__super__.constructor.apply(this,
arguments)}C(b,a);b.prototype._makeCat=function(){var a,b,c,f=this;c=this.domain.levels.length;if(9>=c)return a="#E41A1C #377EB8 #4DAF4A #984EA3 #FF7F00 #FFFF33 #A65628 #F781BF #999999".split(" "),this.f=function(b){b=_.indexOf(f.domain.levels,b);return a[b]};b=function(a){return _.indexOf(f.domain.levels,a)/c+1/(2*c)};return this.f=function(a){return"undefined"!==typeof Raphael&&null!==Raphael?Raphael.hsl(b(a),0.5,0.5):"hsl("+b(a)+",0.5,0.5)"}};return b}(m);l=function(a){function b(a){this._makeDate=
v(this._makeDate,this);this._makeNum=v(this._makeNum,this);this.lower=a.lower;this.upper=a.upper}C(b,a);b.prototype._makeNum=function(){var a,b,f,g,d;f="undefined"!==typeof Raphael&&null!==Raphael?Raphael.color(this.lower):this.lower;d="undefined"!==typeof Raphael&&null!==Raphael?Raphael.color(this.upper):this.upper;g=c.linear(this.domain.min,f.r,this.domain.max,d.r);b=c.linear(this.domain.min,f.g,this.domain.max,d.g);a=c.linear(this.domain.min,f.b,this.domain.max,d.b);return this.f=this._identityWrapper(function(c){return"undefined"!==
typeof Raphael&&null!==Raphael?Raphael.rgb(g(c),b(c),a(c)):"rgb("+g(c)+","+b(c)+","+a(c)+")"})};b.prototype._makeDate=function(){return this._makeNum()};return b}(m);d=function(a){function b(a){this._makeDate=v(this._makeDate,this);this._makeCat=v(this._makeCat,this);this._makeNum=v(this._makeNum,this);this.lower=a.lower;this.middle=a.middle;this.upper=a.upper;this.midpoint=a.midpoint;null==this.midpoint&&(this.midpoint=0)}C(b,a);b.prototype._makeNum=function(){var a,b,f,g,d,e,q,h,k,m=this;d="undefined"!==
typeof Raphael&&null!==Raphael?Raphael.color(this.lower):this.lower;e="undefined"!==typeof Raphael&&null!==Raphael?Raphael.color(this.middle):this.middle;k="undefined"!==typeof Raphael&&null!==Raphael?Raphael.color(this.upper):this.upper;q=c.linear(this.domain.min,d.r,this.midpoint,e.r);f=c.linear(this.domain.min,d.g,this.midpoint,e.g);a=c.linear(this.domain.min,d.b,this.midpoint,e.b);h=c.linear(this.midpoint,e.r,this.domain.max,k.r);g=c.linear(this.midpoint,e.g,this.domain.max,k.g);b=c.linear(this.midpoint,
e.b,this.domain.max,k.b);return this.f=this._identityWrapper(function(c){return c<m.midpoint?"undefined"!==typeof Raphael&&null!==Raphael?Raphael.rgb(q(c),f(c),a(c)):"rgb("+q(c)+","+f(c)+","+a(c)+")":"undefined"!==typeof Raphael&&null!==Raphael?Raphael.rgb(h(c),g(c),b(c)):"rgb("+h(c)+","+g(c)+","+b(c)+")"})};b.prototype._makeCat=function(){};b.prototype._makeDate=function(){return this._makeNum()};return b}(m);s=function(a){function b(a){this["function"]=a["function"]}C(b,a);b.prototype.make=function(a){this.domain=
a;this.compare=c.domain.compare(a);return this.f=this._identityWrapper(this["function"])};return b}(m);(function(a){function b(){return q=b.__super__.constructor.apply(this,arguments)}C(b,a);b.prototype._makeCat=function(){};return b})(m);b=function(a){function b(){return u=b.__super__.constructor.apply(this,arguments)}C(b,a);b.prototype.make=function(a){this.domain=a;this.compare=function(a,b){return 0};return this.f=this._identityWrapper(function(a){return a})};return b}(m);c.scale={};c.scale.Base=
m;c.scale.classes={linear:a,log:e,area:n,palette:k,gradient:l,gradient2:d,identity:b,opacity:h,custom:s};c.scale.make=function(a){if(a.type in c.scale.classes)return new c.scale.classes[a.type](a);throw c.error.defn("No such scale "+a.type+".");}}).call(this);(function(){var n,s=[].indexOf||function(c){for(var d=0,b=this.length;d<b;d++)if(d in this&&this[d]===c)return d;return-1};c.scaleset=function(c,d,b){return new n(c,d,b)};n=function(){function l(d,b){this.coord=b;this.ranges=d;this.axes=c.guide.axes();
this.legends=c.guide.legends()}l.prototype.make=function(c,b,a){this.guideSpec=c;this.layers=a;this.domains=b;this.scales=this._makeScales(c,b,this.ranges);this.reverse={x:this.scales.x.finv,y:this.scales.y.finv};return this.layerMapping=this._mapLayers(a)};l.prototype.setRanges=function(c){var b,a,e,h;this.ranges=c;e=["x","y"];h=[];b=0;for(a=e.length;b<a;b++)c=e[b],h.push(this.scales[c].make(this.domains[c],this.ranges[c],this.getSpec(c).padding));return h};l.prototype._makeScales=function(d,b,a){var e,
h,k,m,l,p,n,f;h=function(a){var b,f;if(d&&null!=d[a]&&null!=d[a].scale){if(_.isFunction(d[a].scale))return{type:"custom","function":d[a].scale};b=function(){switch(a){case "x":return["linear","log"];case "y":return["linear","log"];case "color":return["palette","gradient","gradient2"];case "size":return["linear","log"];case "opacity":return["opacity"];case "shape":return["linear","log","area"];case "id":return["identity"];case "text":return["identity"];default:return[]}}();if(f=d[a].scale.type,0<=
s.call(b,f))return d[a].scale;throw c.error.scale("Aesthetic "+a+" cannot have scale "+d[a].scale.type);}return null};e={};e.x=c.scale.make(null!=(k=h("x"))?k:{type:"linear"});e.x.make(b.x,a.x,this.getSpec("x").padding);e.y=c.scale.make(null!=(m=h("y"))?m:{type:"linear"});e.y.make(b.y,a.y,this.getSpec("y").padding);null!=b.color&&("cat"===b.color.type?e.color=c.scale.make(null!=(l=h("color"))?l:{type:"palette"}):(a={type:"gradient",upper:"steelblue",lower:"red"},e.color=c.scale.make(null!=(p=h("color"))?
p:a)),e.color.make(b.color));null!=b.size&&(e.size=c.scale.make(null!=(n=h("size"))?n:{type:"area"}),e.size.make(b.size));null!=b.opacity&&(e.opacity=c.scale.make(null!=(f=h("opacity"))?f:{type:"opacity"}),e.opacity.make(b.opacity));e.text=c.scale.make({type:"identity"});e.text.make();return e};l.prototype.fromPixels=function(c,b){var a,e,h,k,m,l,p;null!=c&&null!=b&&(a=this.coord.getAes(c,b,this.reverse),h=a.x,k=a.y);e={};p=this.layerMapping.x;m=0;for(l=p.length;m<l;m++)a=p[m],null!=a.type&&"map"===
a.type&&(e[a.value]=null!=h?h:null);l=this.layerMapping.y;h=0;for(m=l.length;h<m;h++)a=l[h],null!=a.type&&"map"===a.type&&(e[a.value]=null!=k?k:null);return e};l.prototype.getSpec=function(c){return null!=this.guideSpec&&null!=this.guideSpec[c]?this.guideSpec[c]:{}};l.prototype.makeGuides=function(c,b){var a,e;this.makeAxes();this.makeTitles(null!=(a=c.title)?a:"");this.makeLegends(null!=(e=c.legendPosition)?e:"right",b);return{axes:this.axes,legends:this.legends,title:this.title}};l.prototype.renderGuides=
function(c,b,a){this.axes.render(c,b,a);this.renderTitles(c,b);return this.renderLegends(c,b)};l.prototype.disposeGuides=function(c){this.axes.dispose(c);this.legends.dispose(c);this.titles.x.dispose(c);this.titles.y.dispose(c);this.titles.main.dispose(c);return this.titles={}};l.prototype.makeTitles=function(d){null==this.titles&&(this.titles={x:c.guide.title(this.coord.axisType("x")),y:c.guide.title(this.coord.axisType("y")),main:c.guide.title("main")});this.titles.main.make({title:d,guideSpec:{},
position:"top"});this.titles.x.make({guideSpec:this.getSpec("x"),title:c.getLabel(this.layers,"x")});this.titles.y.make({guideSpec:this.getSpec("y"),title:c.getLabel(this.layers,"y")})};l.prototype.titleOffset=function(c){var b,a,e,h,k,m,l;c={};m=this.titles;for(a in m)for(b=m[a],e=b.getDimension(),l=["left","right","top"," bottom"],h=0,k=l.length;h<k;h++)b=l[h],e[b]&&(null==c[b]&&(c[b]=0),c[b]+=e[b]);return c};l.prototype.renderTitles=function(c,b){var a;b=b({},!1,!1);a=this.axesOffset(c);this.titles.x.render(b,
c,a);this.titles.y.render(b,c,a);this.titles.main.render(b,c,a)};l.prototype.makeAxes=function(){var d;return this.axes.make({domains:{x:this.domains.x,y:this.domains.y},coord:this.coord,scales:this.scales,specs:null!=(d=this.guideSpec)?d:{},labels:{x:c.getLabel(this.layers,"x"),y:c.getLabel(this.layers,"y")}})};l.prototype.axesOffset=function(c){return this.axes.getDimension(c)};l.prototype._mapLayers=function(d){var b,a,e,h,k;a={};k=c["const"].aes;e=0;for(h=k.length;e<h;e++)b=k[e],a[b]=_.map(d,
function(a){return null!=a.mapping[b]?{type:"map",value:a.mapping[b]}:null!=a.consts[b]?{type:"const",value:a.consts[b]}:a.defaults[b]});return a};l.prototype.makeLegends=function(c,b){null==c&&(c="right");return this.legends.make({domains:this.domains,layers:this.layers,guideSpec:this.guideSpec,scales:this.scales,layerMapping:this.layerMapping,position:c,dims:b})};l.prototype.legendOffset=function(c){return this.legends.getDimension(c)};l.prototype.renderLegends=function(c,b){var a,e,h,k,m,l,p,n,
f;h={left:0,right:0,top:0,bottom:0};a=this.axesOffset(c);k=this.titleOffset(c);p=["left","right","top","bottom"];m=0;for(l=p.length;m<l;m++)e=p[m],h[e]+=null!=(n=a[e])?n:0,h[e]+=null!=(f=k[e])?f:0;this.legends.render(c,b,h)};return l}()}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m={}.hasOwnProperty,t=function(a,b){function c(){this.constructor=a}for(var d in b)m.call(b,d)&&(a[d]=b[d]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a},p=[].indexOf||function(a){for(var b=
0,c=this.length;b<c;b++)if(b in this&&this[b]===a)return b;return-1},r=function(a,b){return function(){return a.apply(b,arguments)}};c.data=function(a){var b,d;d=void 0;_.isObject(a)&&"data"in a&&(7>(b=_.keys(a).length)&&"meta"in a||5>b)?(b=a.data,d=a.meta):b=a;switch(h(b)){case "json-object":case "json-grid":case "json-array":return c.data.json(b,d,void 0);case "url":return c.data.url(b,d,void 0);case "csv":return c.data.csv(b,d);case "api":return c.data.api(b);default:throw c.error.data("Unknown data format.");
}};c.data.json=function(a,b,c){return new d({data:a,meta:b,type:c})};c.data.csv=function(a,b){return new d({data:a,meta:b,csv:"csv"})};c.data.url=function(a,b,c){return new l({url:a,computeBackend:b,limit:c})};c.data.api=function(a){return new s({apiFun:a})};h=function(a){if(_.isArray(a))return _.isArray(a[0])?"json-grid":"json-array";if(_.isObject(a))return"json-object";if(_.isString(a))return c.isURI(a)?"url":"csv";if(_.isFunction(a))return"api";throw c.error.data("Unknown data format.");};b=function(a,
b){var d,e,h,k,m,l,p;if(0<a.length){h=_.union(_.keys(b),_.keys(a[0]));d=a.slice(0,100);k=0;for(m=h.length;k<m;k++)e=h[k],null==b[e]&&(b[e]={}),b[e].type||(b[e].type=c.type.impute(_.pluck(d,e)));k=0;for(l=a.length;k<l;k++)for(d=a[k],m=0,p=h.length;m<p;m++)e=h[m],d[e]=c.type.coerce(d[e],b[e]);e=h;h=a}else e=_.keys(b),h=[];return{key:e,raw:h,meta:b}};a=function(a,b){var d,e,h,k,m,l,p,n,r,t,x;l=[];if(0<a.length){k=b&&_.isArray(b)?b:b&&_.isObject(b)?_.keys(b):_.keys(a[0]);if(_.isArray(b)||!_.isObject(b))b=
{};d=a.slice(0,100);e=m=0;for(p=k.length;m<p;e=++m)h=k[e],null==b[h]&&(b[h]={}),b[h].type||(b[h].type=c.type.impute(_.pluck(d,e)));n=0;for(t=a.length;n<t;n++){d=a[n];m={};e=r=0;for(x=d.length;r<x;e=++r)p=d[e],h=k[e],m[h]=c.type.coerce(p,b[h]);l.push(m)}h=k;e=l}else h=_.keys(b),e=[];return{key:h,raw:e,meta:b}};k=function(a,b){var d,e,h,k,m,l,p,n,r;h=_.keys(a);m=[];l=0;for(e=h.length;l<e;l++)d=h[l],null==b[d]&&(b[d]={}),b[d].type||(b[d].type=c.type.impute(a[d].slice(0,100)));if(0<h.length&&(e=a[h[0]].length,
0<e))for(d=l=0,r=e-1;0<=r?l<=r:l>=r;d=0<=r?++l:--l){k={};p=0;for(n=h.length;p<n;p++)e=h[p],k[e]=c.type.coerce(a[e][d],b[e]);m.push(k)}return{key:h,raw:m,meta:b}};e=function(a,g){return b(c.csv.parse(a),g)};n=function(){function a(){this.raw=null;this.meta={};this.key=[];this.subscribed=[];this.computeBackend=!1}a.prototype.isData=!0;a.prototype.update=function(){var a,b,c,f,d;f=this.subscribed;d=[];b=0;for(c=f.length;b<c;b++)a=f[b],d.push(a());return d};a.prototype.subscribe=function(a){if(-1===_.indexOf(this.subscribed,
a))return this.subscribed.push(a)};a.prototype.unsubscribe=function(a){return this.subscribed.splice(_.indexOf(this.subscribed,a),1)};a.prototype.keys=function(){return this.key};a.prototype.rename=function(){return!1};a.prototype.renameMany=function(){return!1};a.prototype.remove=function(){return!1};a.prototype.filter=function(){return!1};a.prototype.sort=function(){return!1};a.prototype.derive=function(){return!1};a.prototype.get=function(a){if(this.raw)return _.pluck(this.raw,a);throw c.error.data("Data has not been fetched or is undefined.");
};a.prototype.len=function(){if(this.raw)return this.raw.length;throw c.error.data("Data has not been fetched or is undefined.");};a.prototype.getObject=function(a){if(this.raw)return this.raw[a];throw c.error.data("Data has not been fetched or is undefined.");};a.prototype.max=function(a){return _.max(this.get(a))};a.prototype.min=function(a){return _.min(this.get(a))};a.prototype.getMeta=function(a){if(this.meta)return this.meta[a]};a.prototype.type=function(a){if(a in this.meta)return a=this.meta[a].type,
"num"===a?"number":a;throw c.error.defn("Data does not have column "+a+".");};return a}();d=function(f){function g(a){g.__super__.constructor.call(this);this._setData(a)}t(g,f);g.prototype.getData=function(a,b){if(null==b)a(null,this);else return c.data.frontendProcess(b,this,function(b,c){c.raw=c.data;return a(b,c)})};g.prototype.update=function(a){this._setData(a);return g.__super__.update.call(this)};g.prototype._setData=function(f){var g,d,m;_.isObject(f)&&4>_.keys(f).length&&"data"in f?(g=f.data,
d=null!=(m=f.meta)?m:{}):(g=f,d={});m=function(){var m;switch(null!=(m=f.type)?m:h(g)){case "json-object":return k(g,d);case "json-grid":return a(g,d);case "json-array":return b(g,d);case "csv":return e(g,d);default:throw c.error.data("Unknown data format.");}}();this.key=m.key;this.raw=m.raw;this.meta=m.meta;return this.data=this.raw};g.prototype._checkRename=function(a,b){if(""===b)throw c.error.defn("Column names cannot be an empty string");if(-1===_.indexOf(this.key,a))throw c.error.defn("The key "+
a+" doesn't exist!");if(-1!==_.indexOf(this.key,b))throw c.error.defn("The key "+b+" already exists!");};g.prototype.rename=function(a,b,c){var f,g,d;null==c&&(c=!1);a=a.toString();b=b.toString();if(a===b)return!0;c||this._checkRename(a,b);d=this.raw;f=0;for(g=d.length;f<g;f++)c=d[f],c[b]=c[a],delete c[a];c=_.indexOf(this.key,a);this.key[c]=b;this.meta[b]=this.meta[a];delete this.meta[a];return!0};g.prototype.renameMany=function(a){var b,c;for(b in a)c=a[b],b!==c&&this._checkRename(b,c);for(b in a)c=
a[b],b!==c&&this.rename(b,c,!0);return!0};g.prototype.remove=function(a){var b,c,f,g;b=_.indexOf(this.key,a);if("-1"===b)return!1;this.key.splice(b,1);delete this.meta[a];g=this.raw;c=0;for(f=g.length;c<f;c++)b=g[c],delete b[a];return!0};g.prototype.filter=function(a){var b,f,g,d,e;a=_.isFunction(a)?a:_.isString(a)?new Function("d","with(d) { return "+a+";}"):function(){return!0};f=[];e=this.raw;g=0;for(d=e.length;g<d;g++)b=e[g],a(b)&&f.push(b);return c.data.json(f,this.meta)};g.prototype.sort=function(a,
b){var f,g,d;d=this.type(a);f=_.clone(this.raw);g=c.type.compare(d);f.sort(function(b,c){return g(b[a],c[a])});b&&f.reverse();return c.data.json(f,this.meta)};g.prototype.derive=function(a,b,f){var g,d,e,h,k,m,l,n;null==f&&(f={});d=f.dryrun;g=f.context;null==b&&(b=_uniqueId("var_"));null==g&&(g={});_.isFunction(a)?(f=a,e=!1):(e=!0,f=new Function("d","with(this) { with(d) { return "+(a||'""')+";}}"));n=this.raw;m=0;for(l=n.length;m<l;m++){h=n[m];k=f.call(g,h);if(_.isFunction(k))throw c.error.defn("Derivation function returned another function.");
h[b]=k}if(d)return{success:!0,values:_.pluck(this.raw.slice(0,11),b)};0<=p.call(this.key,b)||this.key.push(b);this.meta[b]={type:c.type.impute(_.pluck(this.raw.slice(0,101),b)),derived:!0};e&&(this.meta[b].formula=a);return b};return g}(n);l=function(f){function g(a){this.getData=r(this.getData,this);g.__super__.constructor.call(this);this.url=a.url;this.computeBackend=a.computeBackend;this.limit=a.limit;null==this.computeBackend&&(this.computeBackend=!1)}t(g,f);g.prototype.getData=function(f,g){var d,
m,l=this;if(null==this.raw||this.computeBackend)return d=-1===_.indexOf(this.url,"?")?"?":"&",m=this.url,this.limit&&(m+=""+d+"limit="+this.limit),g&&(m+="&spec="+encodeURIComponent(JSON.stringify(g))),c.text(m,function(g){var d,m,p;try{g=JSON.parse(g)}catch(n){}_.isObject(g)&&4>_.keys(g).length&&"data"in g?(d=g.data,m=null!=(p=g.meta)?p:{}):(d=g,m={});g=function(){switch(h(d)){case "json-object":return k(d,m);case "json-grid":return a(d,m);case "json-array":return b(d,m);case "csv":return e(d,m);
default:throw c.error.data("Unknown data format.");}}();l.key=g.key;l.raw=g.raw;l.meta=g.meta;l.data=l.raw;return f(null,l)});if(null==g)return f(null,this);c.data.frontendProcess(g,this,function(a,b){b.raw=b.data;return f(a,b)})};g.prototype.update=function(a){this.raw=null;return g.__super__.update.call(this)};g.prototype.renameMany=function(a){return 0===_.keys(a).length};return g}(n);s=function(f){function g(a){this.getData=r(this.getData,this);g.__super__.constructor.call(this);this.apiFun=a.apiFun;
this.computeBackend=!0}t(g,f);g.prototype.getData=function(f,g){var d=this;return this.apiFun(g,function(g,m){var l,p,n,r,t;if(null!=g)return f(g,null);if(_.isString(m))try{m=JSON.parse(m)}catch(x){p=x}p=null;try{l=m.data,n=null!=(r=m.meta)?r:{},t=function(){switch(h(l)){case "json-object":return k(l,n);case "json-grid":return a(l,n);case "json-array":return b(l,n);case "csv":return e(l,n);default:throw c.error.data("Unknown data format.");}}(),d.key=t.key,d.raw=t.raw,d.meta=t.meta,d.data=d.raw}catch(H){p=
H}return f(p,d)})};g.prototype.update=function(a){this.raw=null;return g.__super__.update.call(this)};g.prototype.renameMany=function(a){return 0===_.keys(a).length};return g}(n)}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m,t,p=function(a,b){return function(){return a.apply(b,arguments)}},r=[].indexOf||function(a){for(var b=0,c=this.length;b<c;b++)if(b in this&&this[b]===a)return b;return-1};n=function(){function a(b,f,d,e){this.parseMethod=null!=e?e:c.spec.layerToData;this._wrap=p(this._wrap,
this);this.make=p(this.make,this);this.layerMeta=_.extend({},b.meta,{_additionalInfo:b.additionalInfo});this.dataObj=b.data;this.prevSpec=null;this.strictmode=d;this.statData=null;this.metaData={}}a.prototype.make=function(a,b,c){var f,d;d=this._wrap(c);this.strictmode&&d({data:this.dataObj.raw,meta:this.dataObj.meta});if(this.dataObj.computeBackend)return f=this.parseMethod(a,b),this.layerMeta&&(f.meta=this.layerMeta),s(f,this.dataObj,d);f=this.parseMethod(a,b);return this.dataObj.getData(function(a,
b){var c,g,e,h;if(null!=a)return d(a,null);if(0<=r.call(f.select,"count(*)")){h=b.data;g=0;for(e=h.length;g<e;g++)c=h[g],c["count(*)"]=1;b.meta["count(*)"]={};b.meta["count(*)"].type="num";f.stats.stats.push({key:"count(*)",name:"count(*)",stat:"count"})}return k(f,b,d)})};a.prototype._wrap=function(a){var b=this;return function(c,f){var d,e;if(null!=c)return a(c,null,null);d=f.data;e=f.meta;b.statData=d;b.metaData=e;return a(null,b.statData,b.metaData)}};return a}();c.DataProcess=n;c.data.process=
function(a,b,c,d){a=new n(b,c);a.process(d);return a};a={ident:function(a){return function(b){if(a in b)return b[a];throw c.error.defn("Referencing unknown column: "+a);}},"const":function(a){return function(){return a}},conditional:function(a,b,c){return function(d){return a(d)?b(d):c(d)}},infixop:{"+":function(a,b){return function(c){return a(c)+b(c)}},"-":function(a,b){return function(c){return a(c)-b(c)}},"*":function(a,b){return function(c){return a(c)*b(c)}},"/":function(a,b){return function(c){return a(c)/
b(c)}},"%":function(a,b){return function(c){return a(c)%b(c)}},">":function(a,b){return function(c){return a(c)>b(c)}},">=":function(a,b){return function(c){return a(c)>=b(c)}},"<":function(a,b){return function(c){return a(c)<b(c)}},"<=":function(a,b){return function(c){return a(c)<=b(c)}},"!=":function(a,b){return function(c){return a(c)!==b(c)}},"==":function(a,b){return function(c){return a(c)===b(c)}},"=":function(a,b){return function(c){return a(c)===b(c)}},"++":function(a,b){return function(c){return a(c)+
b(c)}}},trans:{substr:function(a){return function(b){var c,d;d=a[0](b).toString();c=a[1](b);b=a[2](b);return d.substr(c,b)}},length:function(a){return function(b){b=a[0](b).toString();return _.size(b)}},upper:function(a){return function(b){return a[0](b).toString().toUpperCase()}},lower:function(a){return function(b){return a[0](b).toString().toLowerCase()}},indexOf:function(a){return function(b){var c;c=a[0](b).toString();b=a[1](b).toString();return c.indexOf(b)}},parseNum:function(a){return function(b){return+a[0](b).toString()}},
parseDateDefault:function(a){return function(b){b=a[0](b);return moment(b).unix()}},parseDate:function(a){return function(b){var c;c=a[0](b);b=a[1](b);return moment(c,b).unix()}},year:function(a){return function(b){b=a[0](b);return moment.unix(b).year()}},month:function(a){return function(b){b=a[0](b);return moment.unix(b).month()+1}},dayOfMonth:function(a){return function(b){b=a[0](b);return moment.unix(b).date()}},dayOfYear:function(a){return function(b){b=a[0](b);return moment.unix(b).dayOfYear()}},
dayOfWeek:function(a){return function(b){b=a[0](b);return moment.unix(b).day()}},hour:function(a){return function(b){b=a[0](b);return moment.unix(b).hour()}},minute:function(a){return function(b){b=a[0](b);return moment.unix(b).minute()}},second:function(a){return function(b){b=a[0](b);return moment.unix(b).second()}},log:function(a){return function(b){return Math.log(a[0](b))}},lag:function(a){var b;b=[];return function(d){var e,h;h=a[0](d);d=a[1](d);e=_.size(b);if(0===e){var k;k=[];for(e=1;1<=d?
e<=d:e>=d;1<=d?++e:--e)k.push(void 0);b=k}else if(e!==d)throw c.error.defn("Lag period needs to be constant, but isn't!");b.push(h);return b.shift()}},bin:function(a){return function(b){var c,d;c=a[0](b);b=a[1](b);if(_.isNumber(b))return Math.floor(c/b)*b;d=function(a,b){var d;d=moment.unix(c).startOf(b);d[b](a*Math.floor(d[b]()/a));return d.unix()};switch(b){case "week":return moment.unix(c).day(0).unix();case "twomonth":return d(2,"month");case "quarter":return d(4,"month");case "sixmonth":return d(6,
"month");case "twoyear":return d(2,"year");case "fiveyear":return d(5,"year");case "decade":return d(10,"year");default:return moment.unix(c).startOf(b).unix()}}}}};b=function(d){var e,h,k,m,l,p,n;l=d[0];d=d[1];if("ident"===l)d=a.ident(d.name);else if("const"===l)d=(n=c.type.coerce(d.value,{type:d.type}),a["const"](n));else if("infixop"===l)d=(m=b(d.lhs),p=b(d.rhs),a.infixop[d.opname](m,p));else if("conditional"===l)d=(h=b(d.cond),k=b(d.conseq),e=b(d.altern),a.conditional(h,k,e));else if("call"===
l){m=d.args;p=[];h=0;for(k=m.length;h<k;h++)e=m[h],p.push(b(e));d=a.trans[d.fname](p)}else d=void 0;if(d)return d;throw c.error.defn("Unknown operation of type: "+l);};h={lt:function(a,b){return a<b},le:function(a,b){return a<=b},gt:function(a,b){return a>b},ge:function(a,b){return a>=b},"in":function(a,b){return 0<=r.call(b,a)}};e=function(a){var b;b=[];_.each(a,function(a){var d,f;d=c.parser.unbracket(a.expr.name);f=_.pick(a,"lt","gt","le","ge","in");return _.each(f,function(c,f){if(f in h)return a=
function(a){return h[f](a[d],c)},b.push(a)})});return function(a){var c,d,f;d=0;for(f=b.length;d<f;d++)if(c=b[d],!c(a))return!1;return!0}};t={sum:function(a){return _.reduce(_.without(a,void 0,null),function(a,b){return a+b},0)},mean:function(a){a=_.without(a,void 0,null);return _.reduce(a,function(a,b){return a+b},0)/a.length},count:function(a){return _.without(a,void 0,null).length},unique:function(a){return _.uniq(_.without(a,void 0,null)).length},min:function(a){return _.min(a)},max:function(a){return _.max(a)},
median:function(a){return c.median(a)},box:function(a){var b,d,e,h,k,m;d=a.length;return 5<d?(h=d/2,a=_.sortBy(a,function(a){return a}),b=Math.ceil(h)/2,0!==b%1?(b=Math.floor(b),h=a[b],d=a[d-1-b]):(h=(a[b]+a[b-1])/2,d=(a[d-b]+a[d-b-1])/2),b=d-h,e=h-1.5*b,k=d+1.5*b,b=_.groupBy(a,function(a){return a>=e&&a<=k}),{q1:_.min(b["true"]),q2:h,q3:c.median(a,!0),q4:d,q5:_.max(b["true"]),outliers:null!=(m=b["false"])?m:[]}):{outliers:a}}};d=function(a,b){var d,e,h;h={};_.each(b.stats,function(a){var b,d,f,e;
e=a.name;b=a.expr;a=a.args;d=t[e];f=c.parser.unbracket(a[0].name);return h[b.name]=function(a){return d(_.pluck(a,f))}});e=c.groupBy(a,function(){var a,f,e,h;e=b.groups;h=[];a=0;for(f=e.length;a<f;a++)d=e[a],h.push(c.parser.unbracket(d.name));return h}());return _.map(e,function(a){var d,e,f,k,m;e={};m=b.groups;f=0;for(k=m.length;f<k;f++)d=m[f].name,d=c.parser.unbracket(d),e[d]=a[0][d];for(d in h)f=h[d],e[d]=f(a);return e})};l=function(a,b){var e,h,k,m,l,p,n,r;k=a.key;p=a.sort;r=a.stat;e=a.args;m=
a.limit;h=a.asc;r&&(e={stats:[{name:r,expr:p,args:e}],groups:[k]},b=d(b,e));l=h?1:-1;n=c.parser.unbracket(p.name);b.sort(function(a,b){return a[n]===b[n]?0:a[n]>=b[n]?1*l:-1*l});m&&(b=b.slice(0,+(m-1)+1||9E9));h=_.uniq(_.pluck(b,c.parser.unbracket(k.name)));return{meta:{levels:h,sorted:!0},filter:{expr:k,"in":h}}};m=function(a){var b;b=c.parser.createColTypeEnv(a);return function(a){var d,e,f;d=a.expr;f=d[0];e=d[1];d=null;"call"===f&&"bin"===e.fname&&(e=e.args[1],f=e[0],e=e[1],"const"===f&&(d=c.type.coerce(e.value,
{type:e.type})));return{type:c.parser.getType(a.name,b),bw:d}}};k=function(a,g,h){var k,p,n,r,t,s,G,B,F,x,H;G=null!=(p=_.clone(g.meta))?p:{};t=m(G);p=function(a,b){var d,e;null==b&&(b={});d=c.parser.unbracket(a.name);return G[d]=_.extend(null!=(e=G[d])?e:{},t(a),b)};g=_.clone(g.raw);k=function(a,b){var c,d,e,f;f=[];d=0;for(e=g.length;d<e;d++)c=g[d],f.push(c[a]=b(c));return f};if(a.trans)for(H=a.trans,B=0,x=H.length;B<x;B++)n=H[B],k(n.name,b(n.expr)),p(n);a.filter&&(g=_.filter(g,e(a.filter)));if(a.sort){k=
[];H=a.sort;B=0;for(x=H.length;B<x;B++)s=H[B],n=s.key,r=l(s,g),s=r.meta,r=r.filter,k.push(r),p(n,s);g=_.filter(g,e(k))}if(a.stats&&a.stats.stats&&0<a.stats.stats.length)for(g=d(g,a.stats),x=a.stats.stats,k=0,B=x.length;k<B;k++)n=x[k],n=n.expr,p(n);a=null!=(F=a.select)?F:[];F=0;for(p=a.length;F<p;F++)if(n=a[F],n=c.parser.unbracket(n.name),null==G[n]&&"count(*)"!==n)throw c.error.defn("You referenced a data column "+n+" that doesn't exist.");return h(null,{data:g,meta:G})};s=function(a,b,c){return b.getData(c,
a)};c.data.frontendProcess=k;c.data.createFunction=b}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m,t,p,r,f,g,q,u,v,D,C,z,J,G=[].indexOf||function(a){for(var b=0,c=this.length;b<c;b++)if(b in this&&this[b]===a)return b;return-1},B={}.hasOwnProperty,F=function(a,b){function c(){this.constructor=a}for(var d in b)B.call(b,d)&&(a[d]=b[d]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a};t=c["const"].aes;r=c["const"].scaleFns;p={x:r.novalue(),y:r.novalue(),color:"steelblue",
size:5,opacity:0.9,shape:1};d=function(){function a(b,d,e){var f;this.spec=b;this.guideSpec=e;this.mapping={};this.consts={};e=0;for(f=t.length;e<f;e++)d=t[e],b[d]&&(b[d]["var"]&&(this.mapping[d]=c.parser.unbracket(b[d]["var"])),b[d]["const"]&&(this.consts[d]=b[d]["const"]))}a.prototype.defaults=p;a.prototype.calculate=function(a,b){var c,d,e;this.statData=a;this.meta=b;this._calcGeoms();this.geoms=this._sample(this.geoms);b={};e=this.mapping;for(c in e)d=e[c],b[c]=this.meta[d];return{geoms:this.geoms,
meta:b}};a.prototype._calcGeoms=function(){throw c.error.impl();};a.prototype._tooltip=function(a){var b=this;return"function"===typeof this.spec.tooltip?function(c){return b.spec.tooltip(a)}:null!=this.spec.tooltip?function(a){return b.spec.tooltip}:function(d){var e,f,g,h,k,m;k="";h=[];m=b.mapping;for(e in m)g=m[e],-1===h.indexOf(g)&&(h.push(g),f=null!=d&&null!=d[e]?c.format(d[e].domain.type,d[e].domain.bw):function(a){return a},k+="\n"+g+": "+f(a[g]));return k.substr(1)}};a.prototype._sample=function(a){if(!1===
this.spec.sample)return a;if(_.isNumber(this.spec.sample))return c.sample(a,this.spec.sample);throw c.error.defn("A layer's 'sample' definition should be an integer, not "+this.spec.sample);};a.prototype._getValue=function(a,b){return this.mapping[b]?a[this.mapping[b]]:this.consts[b]?r.identity(this.consts[b]):"x"===b||"y"===b?this.defaults[b]:r.identity(this.defaults[b])};a.prototype._getIdFunc=function(){var a=this;return null!=this.mapping.id?function(b){return a._getValue(b,"id")}:c.counter()};
a.prototype._fillZeros=function(a,b){var c,d,e;c=function(){var b,c,e;e=[];b=0;for(c=a.length;b<c;b++)d=a[b],e.push(this._getValue(d,"x"));return e}.call(this);e=_.difference(b,c);return{x:c.concat(e),y:function(){var b,c,e;e=[];b=0;for(c=a.length;b<c;b++)d=a[b],e.push(this._getValue(d,"y"));return e}.call(this).concat(function(){var a,b,c;c=[];a=0;for(b=e.length;a<b;a++)c.push(void 0);return c}())}};a.prototype._stack=function(a){var b,d,e,f,g,h,k,m,l,n=this;a=c.groupBy(this.statData,a);l=[];for(f in a)d=
a[f],this.mapping.color&&(g=this.meta[this.mapping.color].levels,h=null!=g?function(a,b){a=_.indexOf(g,a[n.mapping.color]);b=_.indexOf(g,b[n.mapping.color]);return a<b?-1:a>b?1:0}:(b=c.type.compare(this.meta[this.mapping.color].type),function(a,c){a=a[n.mapping.color];c=c[n.mapping.color];return b(a,c)}),d.sort(h)),k=0,m=null!=this.mapping.y?function(a){return a[n.mapping.y]}:function(a){return 0},l.push(function(){var a,b,c;c=[];a=0;for(b=d.length;a<b;a++)e=d[a],e.$lower=k,k+=parseFloat(m(e)),c.push(e.$upper=
k);return c}());return l};a.prototype._dodge=function(a){var b,d,e,f,g,h,k,m,l,n,p,q,r=this;e=_.without(_.keys(this.mapping),"x","y","id");_.toArray(_.pick(this.mapping,e));p=c.groupBy(this.statData,a);q=[];for(g in p){d=p[g];k={};h=1;l=0;for(n=e.length;l<n;l++)b=e[l],a=_.uniq(function(){var a,c,e;e=[];a=0;for(c=d.length;a<c;a++)f=d[a],e.push(this._getValue(f,b));return e}.call(this)),h*=a.length,a.sort(c.type.compare(this.meta[this.mapping[b]].type)),k[b]=a;m=function(a){var c,d,f,g;c=h;f=d=0;for(g=
e.length;f<g;f++)b=e[f],c/=k[b].length,d+=c*_.indexOf(k[b],r._getValue(a,b));return d};q.push(function(){var a,b,c;c=[];a=0;for(b=d.length;a<b;a++)f=d[a],f.$n=m(f),c.push(f.$m=h);return c}())}return q};a.prototype._inLevels=function(a){var b,c,d,e,f,g;e=["x","y"];c=0;for(d=e.length;c<d;c++)if(b=e[c],null!=(null!=(f=this.guideSpec[b])?f.levels:void 0)&&(g=a[this.spec[b]["var"]],0>G.call(this.guideSpec[b].levels,g)))return!1;return!0};return a}();e=function(a){function b(){return f=b.__super__.constructor.apply(this,
arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b,c,d,e,f,g,h,k;b=this._getIdFunc();this.geoms={};h=this.statData;k=[];f=0;for(g=h.length;f<g;f++){c=h[f];a={};for(d in c)e=c[d],a[d]={"in":[e]};k.push(this.geoms[b(c)]={marks:{0:{type:"circle",x:this._getValue(c,"x"),y:this._getValue(c,"y"),color:this._getValue(c,"color"),size:this._getValue(c,"size"),opacity:this._inLevels(c)?this._getValue(c,"opacity"):0}},evtData:a,tooltip:this._tooltip(c)})}return k};return b}(d);a=function(a){function b(){return g=
b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b,d,e,f,g,h,k,m,l,n,p=this;e=function(){var a,b,c,d;c=_.without(_.keys(this.mapping),"x","y");d=[];a=0;for(b=c.length;a<b;a++)g=c[a],d.push(this.mapping[g]);return d}.call(this);b=c.groupBy(this.statData,e);f=this._getIdFunc();this.geoms={};n=[];for(g in b){a=b[g];k=a[0];d={};m=0;for(l=e.length;m<l;m++)h=e[m],d[h]={"in":[k[h]]};n.push(this.geoms[f(k)]={marks:{0:{type:"path",x:_.map(a,function(a){return p._getValue(a,
"x")}),y:_.map(a,function(a){return p._getValue(a,"y")}),color:this._getValue(k,"color"),opacity:this._getValue(k,"opacity"),size:this._getValue(k,"size")}},evtData:d})}return n};return b}(d);b=function(a){function b(){return q=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype.defaults={x:r.novalue(),y:r.novalue(),color:"steelblue",size:1,opacity:0.9,shape:1};b.prototype._calcGeoms=function(){var a,b,d,e,f,g,h,k,m,l,n,p,q,r,x,t;a=_.uniq(function(){var a,b,c,d;c=this.statData;d=[];a=
0;for(b=c.length;a<b;a++)h=c[a],d.push(this._getValue(h,"x"));return d}.call(this));f=function(){var a,b,c,d;c=_.without(_.keys(this.mapping),"x","y");d=[];a=0;for(b=c.length;a<b;a++)k=c[a],d.push(this.mapping[k]);return d}.call(this);d=_.pairs(c.groupBy(this.statData,f));g=this._getIdFunc();this.geoms={};n=1===_.max(d,function(a){return a[1].length})[1].length;t=[];e=p=0;for(r=d.length;p<r;e=++p){l=d[e];m=l[0];b=l[1];n&&e+1<d.length&&b.push(d[e+1][1][0]);l=b[0];e={};q=0;for(x=f.length;q<x;q++)m=
f[q],e[m]={"in":[l[m]]};b=this._fillZeros(b,a);m=b.x;b=b.y;t.push(this.geoms[g(l)]={marks:{0:{type:"line",x:m,y:b,color:this._getValue(l,"color"),opacity:this._getValue(l,"opacity"),size:this._getValue(l,"size")}},evtData:e})}return t};return b}(d);h=function(a){function b(){return u=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,c,d,e,f,g;b.__super__._calcGeoms.call(this);f=this.geoms;g=[];for(c in f)a=f[c],g.push(function(){var b,c;b=a.marks;c=[];for(d in b)e=
b[d],c.push(e.type="spline");return c}());return g};return b}(b);s=function(a){function b(){return v=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b;if(this.mapping.y&&"cat"===this.meta[this.mapping.y].type)throw c.error.defn("The dependent variable of a bar chart cannot be categorical!");if(this.mapping.x&&(a=this.meta[this.mapping.x],"cat"!==a.type&&!a.bw&&!a.binned&&"num"===a.type&&null==this.guideSpec.x.bw))throw c.error.type("Bar chart x-values need to be binned. Set binwidth or use the bin() transform!");
this.position=null!=(b=this.spec.position)?b:"stack";if("stack"===this.position)return this._calcGeomsStack();if("dodge"===this.position)return this._calcGeomsDodge();throw c.error.defn("Bar chart position "+this.position+" is unknown.");};b.prototype._calcGeomsDodge=function(){var a,b,c,d,e,f,g,h,k,m;a=null!=this.mapping.x?[this.mapping.x]:[];this._dodge(a);this._stack(a.concat("$n"));this.geoms={};b=this._getIdFunc();k=this.statData;m=[];g=0;for(h=k.length;g<h;g++){c=k[g];a={};for(d in c)e=c[d],
"y"!==d&&(a[d]={"in":[e]});e=r.lower(this._getValue(c,"x"),c.$n,c.$m);f=r.upper(this._getValue(c,"x"),c.$n,c.$m);m.push(this.geoms[b(c)]={marks:{0:{type:"rect",x:[e,f],y:[c.$lower,c.$upper],color:this._getValue(c,"color"),opacity:this._inLevels(c)?this._getValue(c,"opacity"):0}},evtData:a,tooltip:this._tooltip(c)})}return m};b.prototype._calcGeomsStack=function(){var a,b,c,d,e,f,g,h,k;this._stack(null!=this.mapping.x?[this.mapping.x]:[]);b=this._getIdFunc();this.geoms={};h=this.statData;k=[];f=0;
for(g=h.length;f<g;f++){c=h[f];a={};for(d in c)e=c[d],"y"!==d&&(a[d]={"in":[e]});k.push(this.geoms[b(c)]={marks:{0:{type:"rect",x:[r.lower(this._getValue(c,"x")),r.upper(this._getValue(c,"x"))],y:[c.$lower,c.$upper],color:this._getValue(c,"color"),opacity:this._inLevels(c)?this._getValue(c,"opacity"):0}},evtData:a,tooltip:this._tooltip(c)})}return k};return b}(d);n=function(a){function b(){return D=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b,d,e,
f,g,h,k,m,l,n,p,q,r,t,x;a=function(){var a,b,d,e;d=this.statData;e=[];a=0;for(b=d.length;a<b;a++)k=d[a],c.isDefined(this._getValue(k,"y"))&&c.isDefined(p=this._getValue(k,"x"))&&e.push(p);return e}.call(this);a=_.uniq(a);b={};e=0;for(f=a.length;e<f;e++)l=a[e],b[l]=0;g=function(){var a,b,c,d;c=_.without(_.keys(this.mapping),"x","y");d=[];a=0;for(b=c.length;a<b;a++)m=c[a],d.push(this.mapping[m]);return d}.call(this);e=c.groupBy(this.statData,g);h=this._getIdFunc();this.geoms={};x=[];for(m in e){d=e[m];
n=d[0];f={};q=0;for(r=g.length;q<r;q++)l=g[q],f[l]={"in":[n[l]]};l=function(){var c,d,e;e=[];c=0;for(d=a.length;c<d;c++)p=a[c],e.push(b[p]);return e}();r=0;for(t=d.length;r<t;r++)k=d[r],p=this._getValue(k,"x"),q=this._getValue(k,"y"),b[p]+=q;d=function(){var c,d,e;e=[];c=0;for(d=a.length;c<d;c++)p=a[c],e.push(b[p]);return e}();x.push(this.geoms[h(n)]={marks:{0:{type:"area",x:a,y:{bottom:l,top:d},color:this._getValue(n,"color"),opacity:this._getValue(n,"opacity")}},evtData:f})}return x};return b}(d);
k=function(a){function b(){return C=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b,c,d,e,f,g,h,k;b=this._getIdFunc();this.geoms={};h=this.statData;k=[];f=0;for(g=h.length;f<g;f++){c=h[f];a={};for(d in c)e=c[d],a[d]={"in":[e]};k.push(this.geoms[b(c)]={marks:{0:{type:"text",x:this._getValue(c,"x"),y:this._getValue(c,"y"),text:this._getValue(c,"text"),color:this._getValue(c,"color"),size:this._getValue(c,"size"),opacity:this._getValue(c,"opacity"),"text-anchor":"center"}},
evtData:a})}return k};return b}(d);m=function(a){function b(){return z=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b,c,d,e,f,g,h,k;b=this._getIdFunc();this.geoms={};h=this.statData;k=[];f=0;for(g=h.length;f<g;f++){c=h[f];a={};this._getValue(c,"x");this._getValue(c,"y");for(d in c)e=c[d],"y"!==d&&"x"!==d&&(a[d]={"in":[e]});k.push(this.geoms[b(c)]={marks:{0:{type:"rect",x:[r.lower(this._getValue(c,"x")),r.upper(this._getValue(c,"x"))],y:[r.lower(this._getValue(c,
"y")),r.upper(this._getValue(c,"y"))],color:this._getValue(c,"color"),size:this._getValue(c,"size"),opacity:this._getValue(c,"opacity")}},evtData:a,tooltip:this._tooltip(c)})}return k};return b}(d);l=function(a){function b(){return J=b.__super__.constructor.apply(this,arguments)}F(b,a);b.prototype._calcGeoms=function(){var a,b,c,d,e,f,g,h,k,m,l,n,p,q,t,x;c=this._getIdFunc();this.geoms={};t=this.statData;x=[];n=0;for(p=t.length;n<p;n++){e=t[n];b={};for(f in e)a=e[f],"y"!==f&&(b[f]={"in":[a]});k=this._getValue(e,
"x");l=this._getValue(e,"y");a=this._getValue(e,"color");d=this._getValue(e,"size");g=this._inLevels(e)?this._getValue(e,"opacity"):0;h=r.lower(k);m=r.upper(k);k=r.middle(k);b={marks:{},evtData:b};l.q1&&(b.marks={iqr:{type:"rect",x:[h,m],y:[l.q2,l.q4],stroke:a,color:r.identity("white"),size:d,opacity:g,"stroke-width":"1px"},q1:{type:"pline",x:[h,m],y:[l.q1,l.q1],color:a,size:d,opacity:g},lower:{type:"pline",x:[k,k],y:[l.q1,l.q2],color:a,size:d,opacity:g},q5:{type:"pline",x:[h,m],y:[l.q5,l.q5],color:a,
size:d,opacity:g},upper:{type:"pline",x:[k,k],y:[l.q4,l.q5],color:a,size:d,opacity:g},middle:{type:"pline",x:[h,m],y:[l.q3,l.q3],color:a,size:d,opacity:g}});q=l.outliers;d=m=0;for(l=q.length;m<l;d=++m)h=q[d],b.marks[d]={type:"circle",x:k,y:h,color:a,size:r.identity(3),opacity:g};x.push(this.geoms[c(e)]=b)}return x};return b}(d);c.layer={};c.layer.Base=d;c.layer.classes={point:e,text:k,line:b,path:a,area:n,bar:s,tile:m,box:l,spline:h};c.layer.make=function(a,b,d){var e;e=a.type;if(e in c.layer.classes)return new c.layer.classes[e](a,
b,d);throw c.error.defn("No such layer "+a.type+".");}}).call(this);(function(){var n,s={}.hasOwnProperty,l=function(c,b){function a(){this.constructor=c}for(var e in b)s.call(b,e)&&(c[e]=b[e]);a.prototype=b.prototype;c.prototype=new a;c.__super__=b.prototype;return c};c.pane={};c.pane.make=function(c,b){return new n(c,b)};n=function(d){function b(a,b){this.titleObj=b;this.index=a;this.title=this.layers=null}l(b,d);b.prototype.make=function(a,b,d){var k,m,l,n,r;this.layers=d;if(!this.geoms)for(this.geoms=
{},n=this.layers,d=l=0,n=n.length;l<n;d=++l)this.geoms[d]=new c.Geometry;this.metas={};r=this.layers;d=l=0;for(n=r.length;l<n;d=++l)k=r[d],m=k.calculate(b[d].statData,b[d].metaData),k=m.geoms,m=m.meta,this.geoms[d].set(k),this.metas[d]=m;null==this.title&&(this.title=this._makeTitle(a));this.title.make(this.titleObj);return this.domains=this._makeDomains(a,this.geoms,this.metas)};b.prototype._makeTitle=function(){return c.guide.title("facet")};b.prototype._makeDomains=function(a,b,d){return c.domain.make(b,
d,a.guides,a.strict)};b.prototype.render=function(a,b,c,d){var m;this.title.render(a({},!1,!1),d,b);b=a(b,c,!0);c=this.geoms;d=[];for(m in c)a=c[m],d.push(a.render(b));return d};b.prototype.dispose=function(a){var b,c,d;d=this.geoms;for(c in d)b=d[c],b.dispose(a);this.geoms={};return this.title.dispose(a)};return b}(c.Renderable)}).call(this);(function(){c.dim={};c.dim.make=function(c,s,l){var d,b,a,e,h,k,m,t;c={width:null!=(b=c.width)?b:400,height:null!=(a=c.height)?a:400,paddingLeft:null!=(e=c.paddingLeft)?
e:10,paddingRight:null!=(d=c.paddingRight)?d:10,paddingTop:null!=(h=c.paddingTop)?h:10,paddingBottom:null!=(k=c.paddingBottom)?k:10,horizontalSpacing:null!=(m=c.horizontalSpacing)?m:10,verticalSpacing:null!=(t=c.verticalSpacing)?t:20,guideTop:10,guideRight:0,guideLeft:5,guideBottom:5};d=s.axesOffset(c);b=d.left;a=d.right;e=d.top;d=d.bottom;c.guideLeft+=null!=b?b:0;c.guideRight+=null!=a?a:0;c.guideBottom+=null!=d?d:0;c.guideTop+=null!=e?e:0;d=s.titleOffset(c);b=d.left;a=d.right;e=d.top;d=d.bottom;
c.guideLeft+=null!=b?b:0;c.guideRight+=null!=a?a:0;c.guideBottom+=null!=d?d:0;c.guideTop+=null!=e?e:0;s=s.legendOffset(c);b=s.left;a=s.right;e=s.top;d=s.bottom;c.guideLeft+=null!=b?b:0;c.guideRight+=null!=a?a:0;c.guideBottom+=null!=d?d:0;c.guideTop+=null!=e?e:0;s=0.4*c.width;b=0.4*c.height;c.guideLeft>s&&(c.guideLeft=s);c.guideRight>s&&(c.guideRight=s);c.guideTop>b&&(c.guideTop=b);c.guideBottom>b&&(c.guideBottom=b);c.chartHeight=c.height-c.paddingTop-c.paddingBottom-c.guideTop-c.guideBottom;c.chartWidth=
c.width-c.paddingLeft-c.paddingRight-c.guideLeft-c.guideRight;null!=l.cols&&1<l.cols?(c.eachWidth=c.chartWidth-c.horizontalSpacing*l.cols,c.eachWidth/=l.cols):c.eachWidth=c.chartWidth;null!=l.rows&&1<l.rows?(c.eachHeight=c.chartHeight-c.verticalSpacing*(l.rows+1),c.eachHeight/=l.rows):c.eachHeight=c.chartHeight-c.verticalSpacing;return c};c.dim.guess=function(c,s){var l,d,b,a,e,h,k,m,t;l={width:null!=(d=c.width)?d:400,height:null!=(b=c.height)?b:400,paddingLeft:null!=(a=c.paddingLeft)?a:10,paddingRight:null!=
(e=c.paddingRight)?e:10,paddingTop:null!=(h=c.paddingTop)?h:10,paddingBottom:null!=(k=c.paddingBottom)?k:10,guideLeft:30,guideRight:40,guideTop:10,guideBottom:30,horizontalSpacing:null!=(m=c.horizontalSpacing)?m:10,verticalSpacing:null!=(t=c.verticalSpacing)?t:10};l.chartHeight=l.height-l.paddingTop-l.paddingBottom-l.guideTop-l.guideBottom;l.chartWidth=l.width-l.paddingLeft-l.paddingRight-l.guideLeft-l.guideRight;l.eachWidth=null!=s.cols&&1<s.cols?l.chartWidth-l.horizontalSpacing*(s.cols-1):l.chartWidth;
l.eachHeight=null!=s.rows&&1<s.rows?l.chartHeight-l.verticalSpacing*(s.rows-1):l.chartHeight;return l}}).call(this);(function(){var n,s,l,d,b,a,e,h,k,m,t,p,r,f,g,q,u,v,D,C,z={}.hasOwnProperty,J=function(a,b){function c(){this.constructor=a}for(var d in b)z.call(b,d)&&(a[d]=b[d]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a};c.paper=function(a,b,d,e,f){var g;null==f&&(f=!0);g="undefined"!==typeof Raphael&&null!==Raphael?Raphael(a,b,d):c.canvas(a,b,d);a=e.graph;e=e.numeral;
b=g.rect(0,0,b,d).attr({fill:"white",opacity:0,"stroke-width":0});null!=a?(b.click(a.handleEvent("reset")),c.mouseEvents(a,b,f),c.touchEvents(a.handleEvent,b,!0)):null!=e&&b.click(e.handleEvent("reset"));return g};c.mouseEvents=function(a,b,d){var e,f,g,h,k,m;g=a.handleEvent("select");d&&(h=null);m=f=k=e=null;return b.drag(function(b,g,l,p){if(null!=m&&null!=k){if(e={x:k.x+b,y:k.y+g},f=a.facet.getFacetInfo(a.dims,e.x,e.y),null!=h&&null!=f&&f.col===m.col&&f.row===m.row&&d)return l={x:Math.min(k.x,
e.x),y:Math.min(k.y,e.y),width:Math.abs(k.x-e.x),height:Math.abs(k.y-e.y)},h=h.attr(l)}else if(b=c.offset(a.dom),k={x:l-b.left,y:p-b.top},m=a.facet.getFacetInfo(a.dims,k.x,k.y),null!=m&&d)return h=a.paper.rect(k.x,k.y,0,0,2),h=h.attr({fill:"black",opacity:0.2})},function(){return e=k=null},function(){if(null!=k&&null!=e)return null!=h&&d&&(h=h.hide(),h.remove()),g({start:k,end:e})})};c.touchEvents=function(a,b,c){null==c&&(c=!0);if(c)return b.touchstart(a("touchstart")),b.touchend(a("touchend")),
b.touchmove(a("touchmove")),b.touchcancel(a("touchcancel"))};c.render=function(a,b,d,e){return function(f,g,h){null==f&&(f={});null==g&&(g=!1);null==h&&(h=!0);if(null==e.type)throw c.error.unknown("Coordinate don't have at type?");if(null==m[e.type])throw c.error.input("Unknown coordinate type "+e.type);return{add:function(k,l,p,q){var r;if(null==m[e.type][k.type])throw c.error.input("Coord "+e.type+" has no mark "+k.type);r=m[e.type][k.type].render(b,d,e,f,k,h);r.data("m",k);l&&0<_.keys(l).length&&
r.data("e",l);p&&r.data("t",p);null!=g&&r.attr("clip-rect",g);"guide"===q?(r.click(a("guide-click")),r.hover(a("gover"),a("gout"))):"guide-title"===q||"guide-titleH"===q||"guide-titleV"===q?(r.click(a(q)),r.hover(a("tover"),a("tout"))):(r.click(a("click")),r.hover(a("mover"),a("mout")));c.touchEvents(a,r,!0);return r},remove:function(a){return a.remove()},animate:function(a,b,c,k){m[e.type][b.type].animate(a,d,e,f,b,h);null!=g&&a.attr("clip-rect",g);c&&0<_.keys(c).length&&a.data("e",c);k&&a.data("t",
k);a.data("m",b);return a}}}};h=function(){function a(){}a.prototype.render=function(a,b,c,d,e,f){var g;a=this._make(a);c=this.attr(b,c,d,e,f);for(g in c)b=c[g],a.attr(g,b);return a};a.prototype._make=function(){throw c.error.impl();};a.prototype.animate=function(a,b,c,d,e,f){return a.animate(this.attr(b,c,d,e,f),300)};a.prototype.attr=function(a,b,d,e,f){throw c.error.impl();};a.prototype._cantRender=function(a){throw c.error.missingdata();};a.prototype._makePath=function(a,b,c){null==c&&(c="L ");
return("spline"===c?_.map(a,function(a,c){return(0===c?"M "+a+" "+b[c]+" R ":"")+(""+a+" "+b[c])}):_.map(a,function(a,d){return(0===d?"M ":c)+a+" "+b[d]})).join(" ")};a.prototype._maybeApply=function(a,b,c){b=b[c];return _.isObject(b)&&"identity"===b.f?b.v:null!=a[c]?a[c].f(b):b};a.prototype._applyOffset=function(a,b,c){var d;if(!c)return{x:a,y:b};null==c.x&&(c.x=0);null==c.y&&(c.y=0);return{x:_.isArray(a)?function(){var b,e,f;f=[];b=0;for(e=a.length;b<e;b++)d=a[b],f.push(d+c.x);return f}():a+c.x,
y:_.isArray(b)?function(){var a,e,f;f=[];a=0;for(e=b.length;a<e;a++)d=b[a],f.push(d+c.y);return f}():b+c.y}};a.prototype._shared=function(a,b,c){var d,e=this;d=function(d){if(null!=b[d]&&null==c[d])return c[d]=e._maybeApply(a,b,d)};d("opacity");d("stroke-width");d("stroke-dasharray");d("stroke-dashoffset");d("transform");d("font-size");d("font-weight");d("font-family");return c};a.prototype._checkPointUndefined=function(a,b,d){null==d&&(d="Point");if(void 0===a||void 0===b)throw c.error.missing(""+
d+" cannot be plotted due to undefined data.");};a.prototype._checkArrayUndefined=function(a,b,d){var e;null==d&&(d="Line");if(_.all(function(){var c,d,f;f=[];e=c=0;for(d=a.length-1;0<=d?c<=d:c>=d;e=0<=d?++c:--c)f.push(void 0===a[e]||void 0===b[e]);return f}()))throw c.error.missing(""+d+" cannot be plotted due to too many missing points.");};a.prototype._checkArrayNaN=function(a,b){var c,d;d=_.map(_.zip(a,b),function(a,b){return isNaN(a[0])||isNaN(a[1])?void 0:a});return{x:function(){var a,b,e;e=
[];a=0;for(b=d.length;a<b;a++)c=d[a],null!=c&&e.push(c[0]);return e}(),y:function(){var a,b,e;e=[];a=0;for(b=d.length;a<b;a++)c=d[a],null!=c&&e.push(c[1]);return e}()}};return a}();n=function(a){function b(){return t=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype.animate=function(a,b,c,d,e,f){var g,h;h=a.data("m");g=this.attr(b,c,d,e,f);if(_.isEqual(h.x,e.x))return a.animate(g,300);b=this.attr(b,c,d,h,f);return a.animate(b,300,function(){return a.attr(g)})};return b}(h);s=function(a){function b(){return p=
b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype._make=function(a){return a.circle()};b.prototype.attr=function(a,b,c,d,e){e=b.getXY(e,d);b=e.x;e=e.y;this._checkPointUndefined(b,e,"Circle");c=this._applyOffset(b,e,c);b=c.x;e=c.y;c=this._maybeApply(a,d,d.stroke?"stroke":"color");c={cx:b,cy:e,r:this._maybeApply(a,d,"size"),stroke:c};(b=this._maybeApply(a,d,"color"))&&"none"!==b&&(c.fill=b);return this._shared(a,d,c)};return b}(h);b=function(a){function b(){return r=b.__super__.constructor.apply(this,
arguments)}J(b,a);b.prototype._make=function(a){return a.path()};b.prototype.attr=function(a,b,c,d,e){var f;e=b.getXY(e,d);b=e.x;e=e.y;this._checkArrayUndefined(b,e,"Path");c=this._applyOffset(b,e,c);b=c.x;e=c.y;f=this._maybeApply(a,d,d.stroke?"stroke":"color");c=this._maybeApply(a,d,d.size?"size":"stroke-width");return this._shared(a,d,{path:this._makePath(b,e),stroke:f,"stroke-width":c})};return b}(h);d=function(a){function b(){return f=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype._make=
function(a){return a.path()};b.prototype.attr=function(a,b,d,e,f){var g,h;g=c.sortArrays(a.x.compare,[e.x,e.y]);e.x=g[0];e.y=g[1];f=b.getXY(f,e);b=f.x;f=f.y;this._checkArrayUndefined(b,f,"Line");g=0;for(h=b.length;g<h;++g);d=this._applyOffset(b,f,d);b=d.x;f=d.y;d=this._checkArrayNaN(b,f);b=d.x;f=d.y;g=this._maybeApply(a,e,e.stroke?"stroke":"color");d=this._maybeApply(a,e,e.size?"size":"stroke-width");return this._shared(a,e,{path:this._makePath(b,f),stroke:g,"stroke-width":d})};return b}(n);k=function(a){function b(){return g=
b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype.attr=function(a,b,d,e,f){var g,h;g=c.sortArrays(a.x.compare,[e.x,e.y]);e.x=g[0];e.y=g[1];f=b.getXY(f,e);b=f.x;f=f.y;this._checkArrayUndefined(b,f,"Spline");g=0;for(h=b.length;g<h;++g);d=this._applyOffset(b,f,d);b=d.x;f=d.y;d=this._checkArrayNaN(b,f);b=d.x;f=d.y;g=this._maybeApply(a,e,e.stroke?"stroke":"color");d=this._maybeApply(a,e,e.size?"size":"stroke-width");return this._shared(a,e,{path:this._makePath(b,f,"spline"),stroke:g,"stroke-width":d})};
return b}(d);a=function(a){function b(){return q=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype.attr=function(a,b,d,e,f){var g,h,k,m,l;m=b.getXY(f,e);f=m.x;l=m.y;b=m.r;m=m.t;this._checkArrayUndefined(f,l,"Line");l=this._applyOffset(f,l,d);f=l.x;l=l.y;var p,q;if(_.max(b)-_.min(b)<c["const"].epsilon)for(b=b[0],d="M "+f[0]+" "+l[0],h=p=1,q=f.length-1;1<=q?p<=q:p>=q;h=1<=q?++p:--p)k=Math.abs(m[h]-m[h-1])>Math.PI?1:0,g=0<m[h]-m[h-1]?1:0,d+="A "+b+" "+b+" 0 "+k+" "+g+" "+f[h]+" "+l[h];
else d=this._makePath(f,l);b=this._maybeApply(a,e,e.stroke?"stroke":"color");return this._shared(a,e,{path:d,stroke:b})};return b}(d);n=function(a){function b(){return u=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype._make=function(a){return a.path()};b.prototype.attr=function(a,b,d,e,f){var g,h,k;g=c.sortArrays(a.x.compare,[e.x,e.y.top]);h=g[0];k=g[1];g=b.getXY(f,{x:h,y:k});g=this._applyOffset(g.x,g.y,d);k=c.sortArrays(function(b,c){return-a.x.compare(b,c)},[e.x,e.y.bottom]);h=
k[0];k=k[1];b=b.getXY(f,{x:h,y:k});b=this._applyOffset(b.x,b.y,d);h=g.x.concat(b.x);k=g.y.concat(b.y);return this._shared(a,e,{path:this._makePath(h,k),stroke:this._maybeApply(a,e,"color"),fill:this._maybeApply(a,e,"color"),"stroke-width":"0px"})};return b}(n);e=function(a){function b(){return v=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype._make=function(a){return a.rect()};b.prototype.attr=function(a,b,c,d,e){e=b.getXY(e,d);b=e.x;e=e.y;this._checkPointUndefined(b[0],e[0],"Bar");
this._checkPointUndefined(b[1],e[1],"Bar");c=this._applyOffset(b,e,c);b=c.x;e=c.y;c=this._maybeApply(a,d,d.stroke?"stroke":"color");return this._shared(a,d,{x:_.min(b),y:_.min(e),width:Math.abs(b[1]-b[0]),height:Math.abs(e[1]-e[0]),fill:this._maybeApply(a,d,"color"),stroke:c,"stroke-width":this._maybeApply(a,d,"stroke-width")})};return b}(h);l=function(a){function b(){return D=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype._make=function(a){return a.path()};b.prototype.attr=function(a,
b,d,e,f){var g,h,k,m;g=e.x;h=g[0];g=g[1];m=e.y;k=m[0];m=m[1];this._checkPointUndefined(h,k,"Bar");this._checkPointUndefined(g,m,"Bar");e.x=[h,h,g,g];e.y=[k,m,m,k];g=b.getXY(f,e);h=g.x;k=g.y;f=g.r;g=g.t;d=this._applyOffset(h,k,d);h=d.x;k=d.y;b.flip&&(h.push(h.splice(0,1)[0]),k.push(k.splice(0,1)[0]),f.push(f.splice(0,1)[0]),g.push(g.splice(0,1)[0]));2*Math.PI-Math.abs(g[1]-g[0])<c["const"].epsilon?(b="M "+h[0]+" "+k[0]+" A "+f[0]+" "+f[0]+" 0 1 1 "+h[0]+" "+(k[0]+2*f[0])+" A "+f[1]+" "+f[1]+" 0 1 1 "+
h[1]+" "+k[1],b+="M "+h[2]+" "+k[2]+" A "+f[2]+" "+f[2]+" 0 1 0 "+h[2]+" "+(k[2]+2*f[2])+" A "+f[3]+" "+f[3]+" 0 1 0 "+h[3]+" "+k[3]+" Z"):(d=Math.abs(g[1]-g[0])>Math.PI?1:0,b="M "+h[0]+" "+k[0]+" A "+f[0]+" "+f[1]+" 0 "+d+" 1 "+h[1]+" "+k[1],d=Math.abs(g[3]-g[2])>Math.PI?1:0,b+="L "+h[2]+" "+k[2]+" A "+f[2]+" "+f[3]+" 0 "+d+" 0 "+h[3]+" "+k[3]+" Z");d=this._maybeApply(a,e,e.stroke?"stroke":"color");return this._shared(a,e,{path:b,fill:this._maybeApply(a,e,"color"),stroke:d,"stroke-width":this._maybeApply(a,
e,"stroke-width")})};return b}(h);h=function(a){function b(){return C=b.__super__.constructor.apply(this,arguments)}J(b,a);b.prototype._make=function(a){return a.text()};b.prototype.attr=function(a,b,c,d,e){var f;e=b.getXY(e,d);b=e.x;e=e.y;this._checkPointUndefined(b,e,"Text");c=this._applyOffset(b,e,c);b=c.x;e=c.y;return this._shared(a,d,{x:b,y:e,r:10,text:this._maybeApply(a,d,"text"),"font-size":this._maybeApply(a,d,"size"),"text-anchor":null!=(f=d["text-anchor"])?f:"left",fill:this._maybeApply(a,
d,"color")||"black"})};return b}(h);m={cartesian:{circle:new s,line:new d,pline:new d,area:new n,path:new b,text:new h,rect:new e,spline:new k},polar:{circle:new s,path:new b,line:new d,pline:new a,area:new n,text:new h,rect:new l,spline:new k}}}).call(this);(function(){var n=[].indexOf||function(c){for(var l=0,d=this.length;l<d;l++)if(l in this&&this[l]===c)return l;return-1};c.handler={};c.handler.tooltip=function(){var n,l,d,b,a,e,h;a={};l=n=b=d=null;h=function(b){b=c.getXY(d,b);if(null!=a.text)return e(a,
b)};e=function(a,b){var c,d,e,f,g,h;d=[b.x,b.y];f=d[0];d=d[1];if(null!=a.text)return e=a.text.getBBox().height,f={x:f,y:d-e/2-20},a.text.attr(f),e=a.text.getBBox(),g=e.x,h=e.y,c=e.width,e=e.height,c={x:g-5,y:h-5,width:c+10,height:e+10},0>c.y&&(c.y=h+30+e,f.y=d+e/2+15),c.x+c.width>n&&(d=c.x+c.width-n,c.x-=d/2,f.x-=d/2),c.x<l&&(f.x+=l-c.x,c.x=l),a.text.attr(f),a.box.attr(c),a};return function(k,m,t,p){var r,f;d=c.offset(p.dom);b=m.paper;n=p.dims.chartWidth+p.dims.guideLeft+p.dims.paddingLeft;l=p.dims.guideLeft+
p.dims.paddingLeft;if("mover"===k||"mout"===k)if(null!=a.text&&(a.text.remove(),a.box.remove()),a={},"mover"===k&&m.tooltip)return k=c.getXY(d,t),m.getBBox(),t=[k.x,k.y],r=t[0],t=t[1],a.text=b.text(r,t,m.tooltip(p.scaleSet.scales)).attr({"text-anchor":"middle",fill:"white"}),p=a.text.getBBox(),p=p.height,a.text.attr({y:t-p/2-20}),p=a.text.getBBox(),r=p.x,f=p.y,t=p.width,p=p.height,a.box=b.rect(r-5,f-5,t+10,p+10,10),a.box.attr({fill:"#213"}),a.text.toFront(),a=e(a,k),m.mousemove(h)}};c.handler.drilldown=
function(s,l,d){var b,a;null==d&&(d={});if(!_.isArray(l))throw c.error.input("Parameter `levels` should be an array.");if(0>n.call(c["const"].aes,s))throw c.error.input("Unknown aesthetic "+s+".");b=0;a=[d];return function(c,d,k,m){var n,p;if("reset"===c&&0<b){d=m.spec;a.pop();c=a.unshift();b--;p=d.layers;k=0;for(n=p.length;k<n;k++)d=p[k],d.filter=c,d[s]=l[b],d.id=l[b];return m.make(m.spec)}if("click"===c&&b<l.length-1&&(c=d.evtData,d=m.spec,k=c[l[b]])){c={};c[l[b]]=k;b++;c=_.extend(_.clone(a[a.length-
1]),c);p=d.layers;k=0;for(n=p.length;k<n;k++)d=p[k],d.filter=c,d[s]=l[b],d.id=l[b];a.push(c);return m.make(m.spec)}}};c.handler.zoom=function(n,l){var d,b,a,e,h,k;null==l&&(l={x:!0,y:!0});if(null==n)throw c.error.input("Initial specification missing.");b={x:_.clone(null!=(e=n.guides)?e.x:void 0),y:_.clone(null!=(h=n.guides)?h.y:void 0)};a=void 0;d=["x","y"];k=function(a){return function(b,c,d,e){return"reset"===b?_.isFunction(a)?a("resetZoom",c,d,e):a.handle("resetZoom",c,d,e):_.isFunction(a)?a(b,
c,d,e):a.handle(b,c,d,e)}};return function(e,h,p,r){var f,g,q,n,s,D,C,z,J;null==a&&(a=_.clone(r.handlers));if("cartesian"===r.coord.type){if("resetZoom"===e){f=r.spec;g=0;for(q=d.length;g<q;g++)p=d[g],f.guides[p]=_.clone(b[p]);r.handlers=_.clone(a);r.make(r.spec)}if("select"===e){h=h.evtData;f=r.spec.guides;C=r.spec.layers;J=[];q=0;for(s=C.length;q<s;q++){g=C[q];n=0;for(D=d.length;n<D;n++)p=d[n],l[p]&&null!=g[p]&&(e=c.parser.unbracket(g[p]["var"]),("num"===(z=r.axes.domains[p].type)||"date"===z)&&
h[e].le-h[e].ge>c["const"].epsilon&&(null==f[p]&&(f[p]={min:null,max:null}),f[p].min=h[e].ge,f[p].max=h[e].le),"cat"===r.axes.domains[p].type&&0!==h[e]["in"].length&&(null==f[p]&&(f[p]={levels:null}),f[p].levels=h[e]["in"]));r.handlers=_.map(r.handlers,k);J.push(r.make(r.spec))}return J}}}}}).call(this);(function(){var n,s=[].indexOf||function(c){for(var d=0,b=this.length;d<b;d++)if(d in this&&this[d]===c)return d;return-1};c.facet={};c.facet.make=function(){return new n};n=function(){function l(){this.type=
"none";this.mapping={};this.specgroups=[];this.groups=[];this.panes={};this.deletedPanes=[]}l.prototype.make=function(d){var b,a;this.spec=d;d=this._getMappings(this.spec.facet);this.type=d.type;this.mapping=a=d.mapping;this.groups=_.values(this.mapping);this.specgroups={};for(b in a)d=a[b],this.spec.facet[b]&&(d=c.parser.normalize(d),this.specgroups[d]=this.spec.facet[b]);this.spec.facet.formatter&&(this.formatter=this.spec.facet.formatter);this.style={};this.spec.facet.size&&(this.style.size=this.spec.facet.size);
if(this.spec.facet.color)return this.style.color=this.spec.facet.color};l.prototype.calculate=function(d,b){var a,e,h,k,m;a=this._makeIndices(d,this.specgroups);this.values=a.values;this.indices=a.indices;"none"===this.type?this.rows=this.cols=1:(this.cols=this.spec.facet.cols,this.rows=this.spec.facet.rows,"wrap"===this.type?(a=this.values[this.mapping["var"]].length,this.cols||this.rows||(this.cols=Math.min(3,a)),this.cols?this.rows=Math.ceil(a/this.cols):this.rows&&(this.cols=Math.ceil(a/this.rows))):
(this.rows=this.mapping.y?this.values[this.mapping.y].length:1,this.cols=this.mapping.x?this.values[this.mapping.x].length:1));this.datas=this._groupData(d,this.indices);a=c.compare(_.keys(this.panes),_.keys(this.indices));e=a.deleted;a=a.added;k=0;for(m=e.length;k<m;k++)h=e[k],this.deletedPanes.push(this.panes[h]),delete this.panes[h];k=0;for(m=a.length;k<m;k++)h=a[k],e=this.formatter?this.formatter(this.indices[h]):h,this.panes[h]=c.pane.make(this.indices[h],_.extend({title:e},this.style));a=this.indices;
e=[];for(h in a)e.push(this.panes[h].make(this.spec,this.datas[h],b));return e};l.prototype.render=function(c,b,a){var e,h,k,m,l,p;if(0<this.deletedPanes.length){e=c({},!1,!1);p=this.deletedPanes;k=0;for(l=p.length;k<l;k++)m=p[k],m.dispose(e);this.deletedPanes=[]}l=this.panes;p=[];for(h in l)m=l[h],k=this.getOffset(b,h),e=a.clipping(k),p.push(m.render(c,k,e,b));return p};l.prototype.dispose=function(c){var b,a,e,h;e=this.panes;for(b in e)a=e[b],this.deletedPanes.push(a),delete this.panes[b];if(c){h=
this.deletedPanes;b=0;for(e=h.length;b<e;b++)a=h[b],a.dispose(c);return this.deletedPanes=[]}};l.prototype.getGrid=function(){return{cols:this.cols,rows:this.rows}};l.prototype.getOffset=function(c,b){var a;a=this._getRowCol(b);return{x:c.paddingLeft+c.guideLeft+(c.eachWidth+c.horizontalSpacing)*a.col,y:c.paddingTop+c.guideTop+(c.eachHeight+c.verticalSpacing)*a.row+c.verticalSpacing}};l.prototype.edge=function(c){var b,a,e,h,k,m,l,p,n=this;if("none"===this.type)return function(){return!0};"grid"===
this.type?(p=function(a){return _.indexOf(n.values[n.mapping.y],n.indices[a][n.mapping.y])},b=function(a){return _.indexOf(n.values[n.mapping.x],n.indices[a][n.mapping.x])}):(b=function(a){return _.indexOf(n.values[n.mapping["var"]],n.indices[a][n.mapping["var"]])%n.cols},p=function(a){return Math.floor(_.indexOf(n.values[n.mapping["var"]],n.indices[a][n.mapping["var"]])/n.cols)});if("none"===c)return function(){return!1};if("out"===c)return function(){return!0};e="top"===c||"bottom"===c?b:p;l="top"===
c?p:"bottom"===c?function(a){return-p(a)}:"left"===c?b:"right"===c?function(a){return-b(a)}:void 0;c={};for(h in this.indices)if(m=e(h),k=l(h),!c[m]||k<c[m].v)c[m]={v:k,k:h};a=_.pluck(c,"k");return function(b){return 0<=s.call(a,b)}};l.prototype.getEvtData=function(c,b){var a,e,h,k;h={};k=this.mapping;for(a in k)e=k[a],h[e]="x"===a||"y"===a?{"in":this.values[e][c]}:{"in":this.values[e][this.rows*b+c]};return h};l.prototype.getFacetInfo=function(d,b,a,e){var h,k,m;if(e){if(null==e.col||null==e.row)throw c.error.impl("Preset rows & columns are not present.");
h=e.col;m=e.row}else h=(b-d.paddingLeft-d.guideLeft)/(d.eachWidth+d.horizontalSpacing),h=Math.floor(h),m=(a-d.paddingTop-d.guideTop-d.verticalSpacing)/(d.eachHeight+d.verticalSpacing),m=Math.floor(m);if(0>h||h>=this.cols||0>m||m>=this.rows)return null;k={x:d.paddingLeft+d.guideLeft+(d.eachWidth+d.horizontalSpacing)*h,y:d.paddingTop+d.guideTop+(d.eachHeight+d.verticalSpacing)*m+d.verticalSpacing};b={x:b-k.x,y:a-k.y};if(!e&&(b.x>d.eachWidth||b.y>d.eachHeight))return null;b.x=Math.max(Math.min(b.x,d.eachWidth),
0);b.y=Math.max(Math.min(b.y,d.eachHeight),0);return{row:m,col:h,offset:k,adjusted:b,evtData:this.getEvtData(h,m)}};l.prototype._getMappings=function(d){var b;b={type:"none",mapping:{}};if(_.isObject(d))if("wrap"===d.type){b.type="wrap";if(!d["var"])throw c.error.defn("You didn't specify a variable to facet on.");d["var"]&&(b.mapping["var"]=c.parser.normalize(d["var"]["var"]))}else if("grid"===d.type){b.type="grid";if(!d.x&&d.y)throw c.error.defn("You didn't specify a variable to facet on.");d.x&&
(b.mapping.x=c.parser.normalize(d.x["var"]));d.y&&(b.mapping.y=c.parser.normalize(d.y["var"]))}return b};l.prototype._makeIndices=function(d,b){var a,e,h,k,m,l,p,n;n={};for(a in b)if(e=b[a],m=c.parser.normalize(e["var"]),e.levels)n[m]=e.levels;else{l=[];for(h in d){e=d[h];if(k=e.metaData[m])!k||"num"!==(p=k.type)&&"date"!==p||c.type.compare(k.type);l=_.uniq(_.union(l,_.pluck(e.statData,m)))}n[m]=l}a=c.cross(n);h={};k=_.pluck(b,"var");l=[];p=0;for(e=k.length;p<e;p++)m=k[p],l.push(c.parser.normalize(m));
m=c.stringify(l);e=0;for(k=a.length;e<k;e++)p=a[e],h[m(p)]=p;return{values:n,indices:h}};l.prototype._groupData=function(d,b){var a,e,h,k,m,l,p;e=c.groupProcessedData(d,this.groups);a={};p=this.indices;for(h in p){k=p[h];for(m=e;!0===m.grouped;)l=k[m.key],m=m.values[l];a[h]=m}return a};l.prototype._getRowCol=function(c){var b;b={row:0,col:0};"wrap"===this.type?(c=this.indices[c][this.mapping["var"]],c=_.indexOf(this.values[this.mapping["var"]],c),b.col=c%this.cols,b.row=Math.floor(c/this.cols)):"grid"===
this.type&&(b.row=_.indexOf(this.values[this.mapping.y],this.indices[c][this.mapping.y]),b.col=_.indexOf(this.values[this.mapping.x],this.indices[c][this.mapping.x]));return b};return l}();c.groupProcessedData=function(l,d){var b,a,e,h,k,m,n,p,r;if(0===d.length)return l;b=d.splice(0,1)[0];m=[];for(e in l)a=l[e],b in a.metaData&&(m=_.union(m,_.uniq(_.pluck(a.statData,b))));k={grouped:!0,key:b,values:{}};p=0;for(r=m.length;p<r;p++){n=m[p];h={};for(e in l)a=l[e],h[e]={metaData:a.metaData},h[e].statData=
b in a.metaData?c.filter(a.statData,b,n):_.clone(a.statData);k.values[n]=c.groupProcessedData(h,_.clone(d))}return k}}).call(this);(function(){var n,s,l,d=function(b,a){return function(){return b.apply(a,arguments)}};l=function(b){var a,d,h,k,l,n,p,r,f,g;l=["row","column","value"];d=0;for(k=l.length;d<k;d++)a=l[d],b[a+"s"]||(b[a+"s"]=[],null!=b[a]&&b[a+"s"].push(b[a]));f=["rows","columns","values"];l=0;for(p=f.length;l<p;l++)for(a=f[l],g=b[a],d=n=0,r=g.length;n<r;d=++n)k=g[d],_.isString(k)&&(b[a][d]=
{"var":k});null==b.full&&(b.full=!1);null==b.formatter&&(b.formatter={});d=b.formatter;for(h in d)a=d[h],h=c.parser.normalize(h),b.formatter[h]=a;return b};s=function(){function b(a,b,h){var k,l,n,p,r;this.statData=a;this.ticks=b;this.spec=h;this.get=d(this.get,this);this.makeFormatters=d(this.makeFormatters,this);this.makeHeaders=d(this.makeHeaders,this);this.rows=function(){var a,b,d,e;d=this.spec.rows;e=[];a=0;for(b=d.length;a<b;a++)k=d[a],e.push(c.parser.unbracket(k["var"]));return e}.call(this);
this.columns=function(){var a,b,d,e;d=this.spec.columns;e=[];a=0;for(b=d.length;a<b;a++)k=d[a],e.push(c.parser.unbracket(k["var"]));return e}.call(this);b=this.rows.concat(this.columns);a=this.columns;this.dataIndexByRows={};this.dataIndexByCols={};n=function(a,b,c){var d,e,h,k,l;a=e=a;h=0;for(k=b.length;h<k;h++)d=b[h],null==a[l=c[d]]&&(a[l]={}),e=a,a=e[c[d]];return e[c[d]]=c};r=this.statData;l=0;for(p=r.length;l<p;l++)h=r[l],n(this.dataIndexByRows,b,h),n(this.dataIndexByCols,a,h)}b.prototype.makeHeaders=
function(){var a,b,c=this;a=this.spec.full;b=function(d,l,n,p){var r,f,g;if(0===n.length)return d.push(l);r=n[0];f=n.slice(1);g=_.keys(p);return _.each(c.ticks[r].ticks,function(c,h){var n;if(a||_.contains(g,""+c.location))return n=_.clone(l),n[r]=c.value,b(d,n,f,p[c.location])})};this.rowHeaders=[];this.colHeaders=[];b(this.rowHeaders,{},this.rows,this.dataIndexByRows);b(this.colHeaders,{},this.columns,this.dataIndexByCols);return{rowHeaders:this.rowHeaders,colHeaders:this.colHeaders}};b.prototype.makeFormatters=
function(){var a,b,d,k,l,n,p;n=this.spec.values;p=[];k=0;for(l=n.length;k<l;k++)d=n[k],p.push(c.parser.unbracket(d["var"]));d={};l=0;for(n=p.length;l<n;l++)k=p[l],d[k]=k in this.spec.formatter?this.spec.formatter[k]:(b=c.format.getExp(_.min(_.pluck(this.statData,k))),a=b,c.format.number(a));p=this.columns.concat(this.rows);a=0;for(b=p.length;a<b;a++)k=p[a],k in this.spec.formatter&&(d[k]=this.spec.formatter[k]);return d};b.prototype.get=function(a,b,c){var d,l,n,p,r;l=this.dataIndexByRows;r=this.rows;
n=0;for(p=r.length;n<p;n++)d=r[n],d=this.ticks[d].ticks[a[d]].location,null!=l&&null!=l[d]&&(l=l[d]);p=this.columns;a=0;for(n=p.length;a<n;a++)d=p[a],d=this.ticks[d].ticks[b[d]].location,null!=l&&null!=l[d]&&(l=l[d]);if(null!=l&&null!=l[c])return l[c]};return b}();n=function(){function b(a,b,h){this.callback=b;this.prepare=h;this.render=d(this.render,this);this.generateTicks=d(this.generateTicks,this);if(null==a)throw c.error.defn("No pivot table specification is passed in!");this.make(a)}b.prototype.make=
function(a){this.spec=l(a);return(new c.DataProcess(this.spec,[],this.spec.strict,c.spec.pivotToData)).make(this.spec,[],this.render)};b.prototype.generateTicks=function(a,b,d){var k,l,n,p,r,f,g,q,s,v,D;f={};v=["rows","columns"];g=0;for(q=v.length;g<q;g++)for(k=v[g],D=a[k],k=0,s=D.length;k<s;k++)r=D[k],r=c.parser.unbracket(r["var"]),p=d[r],n=_.pluck(b,r),n=c.domain.single(n,d[r],{}),p="cat"===p.type?{ticks:n.levels}:"num"===p.type?{numticks:(n.max-n.min)/p.bw}:(l=c["const"].approxTimeInSeconds[p.bw],
{numticks:(n.max-n.min)/l}),n=c.tick.make(n,p,d[r].type),f[r]=n;return f};b.prototype.render=function(a,b,d){var k,l,n,p,r,f,g,q,u,v,D,C;a=this.generateTicks(this.spec,b,d);b=new s(b,a,this.spec);d=b.makeHeaders();a=d.rowHeaders;d=d.colHeaders;g=b.makeFormatters();k=this.spec.columns.length;l=this.spec.rows.length;n=this.spec.values.length;if(!$)throw c.error.depn("Pivot Tables require jQuery!");C=$("<table></table>").attr("border","1px solid black");C.attr("cellspacing",0);C.attr("cellpadding",0);
for(q=0;q<k;){D=$("<tr></tr>");r=c.parser.unbracket(this.spec.columns[q]["var"]);0===q&&1<l&&(u=$("<td></td>"),u.attr("rowspan",k),u.attr("colspan",l-1),D.append(u));D.append($("<th>"+r+":</th>").attr("align","right"));for(u=0;u<d.length;){p=d[u][r];for(f=1;u+f<d.length&&p===d[u+f][r];)f++;g[r]&&(p=g[r](p));p=$("<td class='heading'>"+p+"</td>").attr("colspan",f*n);p.attr("align","center");D.append(p);u+=f}C.append(D);q++}D=$("<tr></tr>");0===l&&(u=$("<td class='spacing'></td>"),u.attr("rowspan",a.length+
1),D.append(u));for(q=0;q<l;)r=c.parser.unbracket(this.spec.rows[q]["var"]),D.append($("<th>"+r+"</th>").attr("align","center")),q++;for(q=0;q<d.length;){k=this.spec.values;u=0;for(r=k.length;u<r;u++)p=k[u],p=$("<td class='heading'>"+c.parser.unbracket(p["var"])+"</td>"),p.attr("align","center"),D.append(p);q++}C.append(D);for(q=0;q<a.length;){D=$("<tr></tr>");l=this.spec.rows;u=0;for(k=l.length;u<k;u++)if(r=l[u],r=c.parser.unbracket(r["var"]),p=a[q][r],0===q||p!==a[q-1][r]){for(n=1;q+n<a.length&&
p===a[q+n][r];)n++;g[r]&&(p=g[r](p));p=$("<td class='heading'>"+p+"</td>").attr("rowspan",n);p.attr("align","center");p.attr("valign","middle");D.append(p)}for(u=0;u<d.length;){r=d[u];k=a[q];f=this.spec.values;l=0;for(n=f.length;l<n;l++)p=f[l],v=c.parser.unbracket(p["var"]),p=(p=b.get(k,r,v))?g[v](p):"-",D.append($("<td class='value'>"+p+"</td>").attr("align","right"));u++}C.append(D);q++}this.prepare&&this.prepare(this);this.spec.width&&C.attr("width",this.spec.width);this.spec.height&&C.attr("height",
this.spec.height);this.dom=_.isString(this.spec.dom)?$("#"+this.spec.dom):$(this.spec.dom);this.dom.empty();this.dom.append(C);if(this.callback)return this.callback(null,this)};return b}();c.pivot=function(b,a,c){return new n(b,a,c)}}).call(this);(function(){var n,s,l=function(b,a){return function(){return b.apply(a,arguments)}},d=[].indexOf||function(b){for(var a=0,c=this.length;a<c;a++)if(a in this&&this[a]===b)return a;return-1};s=function(b){_.isString(b.value)&&(b.value={"var":b.value});return b};
n=function(){function b(a,b,d){this.render=l(this.render,this);this.handleEvent=l(this.handleEvent,this);if(null==a)throw c.error.defn("No numeral specification is passed in!");this.handlers=[];this.callback=b;this.prepare=d;this.make(a)}b.prototype.make=function(a){if(!a.value)throw c.error.defn("No value defined in numeral.");this.spec=s(a);return(new c.DataProcess(this.spec,[],this.spec.strict,c.spec.numeralToData)).make(this.spec,[],this.render)};b.prototype.handleEvent=function(a){var b;b=this;
return _.throttle(function(d){var k,l,n,p,r;"guide-title"===a&&(d=c.event.make(a,this),d.dispatch(b.dom));p=b.handlers;r=[];l=0;for(n=p.length;l<n;l++)k=p[l],_.isFunction(k)?r.push(k(a,this,d,b)):r.push(k.handle(a,this,d,b));return r},300)};b.prototype.addHandler=function(a){if(0>d.call(this.handlers,a))return this.handlers.push(a)};b.prototype.render=function(a,b,d){var k,l,n,p;if(null!=a)console.error(a);else{a=c.parser.normalize(this.spec.value["var"]);this.value=b[0][a];this.title=null!=(n=this.spec.title)?
n:a;b=0<(l=this.value)&&1>l?void 0:0===this.value%1?0:-1;this.value=c.format.number(b)(this.value);if(_.isNaN(this.value)||"NaN"===this.value)this.value="Not a Number";null!=this.prepare&&this.prepare(this);this.dom=this.spec.dom;this.width=null!=(k=this.spec.width)?k:200;this.height=null!=(p=this.spec.height)?p:100;null==this.paper&&(this.paper=this._makePaper(this.dom,this.width,this.height,this));null==this.titleObj&&(this.titleObj=this.paper.text(this.width/2,10,""));this.titleObj.attr({text:this.title,
"font-size":"12px"});this.titleObj.click(this.handleEvent("guide-title"));this.titleObj.hover(this.handleEvent("tover"),this.handleEvent("tout"));null==this.textObj&&(this.textObj=this.paper.text(this.width/2,this.height/2,""));this.textObj.attr({x:this.width/2,y:7+this.height/2,text:this.value});k=this.textObj.getBBox();l=k.width;k=k.height;l=Math.min(0.9*this.width/l,0.9*(this.height-14)/k);this.textObj.transform("s"+l);this.callback&&this.callback(null,this)}};b.prototype._makePaper=function(a,
b,d,k){return c.paper(a,b,d,{numeral:k},!1)};return b}();c.numeral=function(b,a,d){try{return new n(b,a,d)}catch(h){console.log(h);if(null!=a)return a(h,null);throw c.error.defn("Bad specification.");}}}).call(this);(function(){var n,s,l,d={}.hasOwnProperty,b=function(a,b){function c(){this.constructor=a}for(var k in b)d.call(b,k)&&(a[k]=b[k]);c.prototype=b.prototype;a.prototype=new c;a.__super__=b.prototype;return a};s=function(){function a(a,b,c){null==a&&(a="polyjsEvent");this.eventName=a;this.cancelable=
this.bubbles=!0;this.detail={type:c,data:b}}a.prototype.dispatch=function(a){var b;b=new CustomEvent(this.eventName,{detail:this.detail});if(null!=a)return a.dispatchEvent(b)};return a}();l=function(a){function c(a,b){c.__super__.constructor.call(this,"title-click",a,b)}b(c,a);return c}(s);n=function(a){function c(a,b){c.__super__.constructor.call(this,"legend-click",a,b)}b(c,a);return c}(s);c.event={};c.event.make=function(a,b){if("guide-title"===a||"guide-titleH"===a||"guide-titleV"===a)return new l(b,
a);if("legend-label"===a||"legend-title"===a)return new n(b,a);throw c.error.defn("No such event "+a+".");}}).call(this);(function(){var n,s=function(c,b){return function(){return c.apply(b,arguments)}},l=[].indexOf||function(c){for(var b=0,a=this.length;b<a;b++)if(b in this&&this[b]===c)return b;return-1};n=function(){function d(b,a,d){null==a&&(a=null);null==d&&(d=null);this.handleEvent=s(this.handleEvent,this);this.render=s(this.render,this);this.mergeDomains=s(this.mergeDomains,this);this.merge=
s(this.merge,this);this.maybeDispose=s(this.maybeDispose,this);if(null==b)throw c.error.defn("No graph specification is passed in!");this.handlers=[];this.coord=this.paper=this.dims=this.legends=this.axes=this.scaleSet=null;this.facet=c.facet.make();this.dataSubscribed=[];this.callback=a;this.prepare=d;this.showTooltip=!(null!=b.tooltip&&!b.tooltip);this.showZoom=!(null!=b.zoom&&!b.zoom);this.make(b);this.showTooltip&&this.addHandler(c.handler.tooltip());this.showZoom&&this.addHandler(c.handler.zoom(b))}
d.prototype.maybeDispose=function(b){var a;a=c.render(this.handleEvent,this.paper,this.scaleSet.scales,this.coord);a=a();if(this.coord&&!_.isEqual(this.coord.spec,b.coord))return this.scaleSet&&(this.scaleSet.disposeGuides(a),this.scaleSet=null),this.coord=null};d.prototype.make=function(b){var a,d,h,k,l,n,p,r,f,g=this;null!=b?(b=c.spec.toStrictMode(b),c.spec.check(b),this.spec=b):b=this.spec;this.scaleSet&&this.maybeDispose(b);null==this.coord&&(this.coord=c.coord.make(this.spec.coord));this.facet.make(b);
d=this.handleEvent("data");h=function(){var a,c,d,e;d=b.layers;e=[];k=a=0;for(c=d.length;a<c;k=++a)l=d[k],e.push(l.data);return e}();f=_.difference(h,this.dataSubscribed);p=0;for(r=f.length;p<r;p++)a=f[p],a.subscribe(d);this.dataSubscribed=h;n=_.after(b.layers.length,this.merge);this.dataprocess={};this.processedData={};return _.each(b.layers,function(a,d){var e;b=g.spec.layers[d];e=_.values(g.facet.specgroups);g.dataprocess[d]=new c.DataProcess(b,e,b.strict);return g.dataprocess[d].make(b,e,function(a,
b,e){if(null!=a)if(console.error(a),null!=g.callback)g.callback(a,null);else throw c.error.defn("Error processing data!");g.processedData[d]={statData:b,metaData:e};return n()})})};d.prototype.merge=function(){var b=this;this.layers=_.map(this.spec.layers,function(a){return c.layer.make(a,b.spec.strict,b.spec.guides)});this.facet.calculate(this.processedData,this.layers);this.mergeDomains();return this.render()};d.prototype.mergeDomains=function(){var b,a,d;b=_.map(this.facet.panes,function(a){return a.domains});
b=c.domain.merge(b);this.scaleSet||(a=c.dim.guess(this.spec,this.facet.getGrid()),this.coord.make(a),d=this.coord.ranges(),this.scaleSet=c.scaleset(d,this.coord));this.scaleSet.make(this.spec.guides,b,this.layers);this.dims=this._makeDimensions(this.spec,this.scaleSet,this.facet,a);this.coord.make(this.dims);this.ranges=this.coord.ranges();return this.scaleSet.setRanges(this.ranges)};d.prototype.render=function(){var b,a;if(null==this.spec.render||!1!==this.spec.render)if(b=this.scaleSet.scales,this.coord.setScales(b),
this.scaleSet.coord=this.coord,a=this.scaleSet.makeGuides(this.spec,this.dims),this.axes=a.axes,this.titles=a.titles,this.legends=a.legends,null!=this.prepare&&this.prepare(this),this.dom=this.spec.dom,null==this.paper&&(this.paper=this._makePaper(this.dom,this.dims.width,this.dims.height,this)),b=c.render(this.handleEvent,this.paper,b,this.coord),this.facet.render(b,this.dims,this.coord),this.scaleSet.renderGuides(this.dims,b,this.facet),null!=this.callback)return this.callback(null,this)};d.prototype.addHandler=
function(b){if(0>l.call(this.handlers,b))return this.handlers.push(b)};d.prototype.removeHandler=function(b){return this.handlers.splice(_.indexOf(this.handlers,b),1)};d.prototype.handleEvent=function(b){var a;a=this;return _.throttle(function(d){var h,k,l,n,p;if("touchstart"===b||"touchmove"===b||"touchend"===b||"touchcancel"===b)c.touch(b,this,d,a);else if("select"===b){k=d.start;h=d.end;k=a.facet.getFacetInfo(a.dims,k.x,k.y);if(!k)return;n=k.col;p=k.row;l=k.adjusted;k=_.clone(l);l=a.facet.getFacetInfo(a.dims,
h.x,h.y,{col:n,row:p}).adjusted;h=_.clone(l);this.evtData="cartesian"===a.coord.type?a.scaleSet.fromPixels(k,h):null}else if("data"===b)this.evtData={};else if("reset"===b||"click"===b||"mover"===b||"mout"===b||"tover"===b||"tout"===b||"gover"===b||"gout"===b||"guide-click"===b)this.tooltip=this.data("t"),this.evtData=this.data("e"),"guide-click"===b&&"text"===this.type&&null!=this.evtData&&(d="legendTitle"===this.evtData.value?c.event.make("legend-title",this):c.event.make("legend-label",this),d.dispatch(a.dom));
else if("guide-title"===b||"guide-titleH"===b||"guide-titleV"===b)this.tooltip=this.data("t"),this.evtData=this.data("e"),d=c.event.make(b,this),d.dispatch(a.dom);p=a.handlers;l=[];k=0;for(n=p.length;k<n;k++)h=p[k],_.isFunction(h)?l.push(h(b,this,d,a)):l.push(h.handle(b,this,d,a));return l},300)};d.prototype._makeScaleSet=function(b,a,d){b=this.coord.ranges();return c.scaleset(b,this.coord)};d.prototype._makeDimensions=function(b,a,d,h){a.makeGuides(b,h);return c.dim.make(b,a,d.getGrid())};d.prototype._makePaper=
function(b,a,d,h){return c.paper(b,a,d,{graph:h},this.showZoom)};return d}();c.chart=function(d,b,a,e){null==e&&(e=!0);if(e)return new n(d,b,a);try{return new n(d,b,a)}catch(h){if(null!=b)return b(h,null);throw c.error.defn("Bad specification.");}}}).call(this)}return{data:c.data,chart:c.chart,pivot:c.pivot,numeral:c.numeral,handler:c.handler,parser:{bracket:c.parser.bracket,unbracket:c.parser.unbracket,parse:c.parser.parse,getExpression:c.parser.getExpression,escape:c.parser.escape,unescape:c.parser.unescape},
debug:c}}(window.polyjs);
