import { z, defineCollection } from "astro:content";

const publicationSchema = z.object({
    id: z.string(),
    title: z.string(),
    authors: z.array(z.string()),
    pages: z.string(),
    year: z.string(),
    volume: z.string().optional(),
    booktitle: z.string().optional(),
    journal: z.string().optional(),
    type: z.enum(["conference", "journal", "workshop"]),
    bibType: z.enum(["article", "inproceedings"]),
    url: z.string().optional(),
    doi: z.string().optional(),
    tr: z.string().optional(),
    code: z.string().optional(),
    artifact: z.string().optional(),
});

const newsSchema = z.object({
    date: z.coerce.date(),
});

export type PublicationSchema = z.infer<typeof publicationSchema>;
export type NewsSchema = z.infer<typeof newsSchema>;

const publicationCollection = defineCollection({ schema: publicationSchema });
const newsCollection = defineCollection({ schema: newsSchema });

export const collections = {
    'publication': publicationCollection,
    'news': newsCollection
}
