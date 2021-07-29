def alter_meta(meta):
    if 'en' in meta:
        for key in meta['en']:
            if meta['en'][key] is not None and isinstance(meta['en'][key], str):
                meta['en'][key] = meta['en'][key].replace("'", "&#39;")
    for key in meta:
        if meta[key] is not None and isinstance(meta[key], str):
            meta[key] = meta[key].replace("'", "&#39;")

    return meta