import { loadFont } from "@remotion/google-fonts/BreeSerif";
import { Audio } from "@remotion/media";
import { AbsoluteFill, Sequence, staticFile, useVideoConfig } from "remotion";
import { z } from "zod";
import { FPS, INTRO_DURATION } from "../lib/constants";
import { TimelineSchema } from "../lib/types";
import { calculateFrameTiming } from "../lib/utils";
import { Background } from "./Background";
import Subtitle from "./Subtitle";

export const aiVideoSchema = z.object({
  timeline: TimelineSchema.nullable(),
});

const { fontFamily } = loadFont();

export const AIVideo: React.FC<z.infer<typeof aiVideoSchema>> = ({ timeline }) => {
  if (!timeline) throw new Error("Expected timeline data");
  const { id } = useVideoConfig();

  return (
    <AbsoluteFill style={{ backgroundColor: "white" }}>
      <Sequence durationInFrames={INTRO_DURATION}>
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", display: "flex", zIndex: 10 }}>
          <div style={{ fontSize: 80, color: "black", fontFamily, backgroundColor: "yellow", padding: 20, border: "5px solid black" }}>
            {timeline.shortTitle}
          </div>
        </AbsoluteFill>
      </Sequence>

      {timeline.elements.map((element, index) => {
        const { startFrame, duration } = calculateFrameTiming(element.startMs, element.endMs, { includeIntro: index === 0 });
        return (
          <Sequence key={`el-${index}`} from={startFrame} durationInFrames={duration}>
            <Background project={id} item={element} />
          </Sequence>
        );
      })}

      {timeline.text.map((element, index) => {
        const { startFrame, duration } = calculateFrameTiming(element.startMs, element.endMs, { addIntroOffset: true });
        return (
          <Sequence key={`txt-${index}`} from={startFrame} durationInFrames={duration}>
            <Subtitle text={element.text} />
          </Sequence>
        );
      })}

      {timeline.audio.map((element, index) => {
        const { startFrame, duration } = calculateFrameTiming(element.startMs, element.endMs, { addIntroOffset: true });
        return (
          <Sequence key={`aud-${index}`} from={startFrame} durationInFrames={duration}>
            {}
            <Audio src={staticFile(`content/${id}/audio/${element.audioUrl}`)} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};